import argparse
import torch
import torchaudio
from pathlib import Path
import string
import csv
import os
import pandas as pd
import re
from transformers import Wav2Vec2ProcessorWithLM, Wav2Vec2ForCTC
import time
start_time = time.time()

def get_dataset(data, name):
    """Gets and returns filename and sentences from a dataset.
    
    Parameters
    ----------
        data : str
        Path to tsv file.
        
        name : str
        Name for output file.
        
    Returns
    -------
        list_data : list
        List of filenames belonging to the dataset.
        
        gold_values : dict
        Audio filename as key and its written transcription as value.
    """

    tsv_data = pd.read_csv(data, sep='\t')
    gold_values = {}
    
    for i, path_file in enumerate(tsv_data['path']):
        sentence = tsv_data['sentence'][i]
        
        #Removes punctuation
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        sentence = re.sub(r"[—–«»…’՚“”]", '', sentence)
        
        #Removes unecessary whitespaces
        sentence = sentence.lower().split()
        
        #We look for a special character that can not be stored in a string
        #(Why? I don't know, it is an accent probably not compatible with
        #other apostrophes. It can not be stored alone by itself, it needs
        #either a space before or a letter to go on. However, I can not
        #remove this accent if there is any other character around, there
        #won't be any match with other words, or otherwise it would probably
        #be over specific and potentially not match other characters that I
        #haven't thought of.)
        # ́
        
        for count, word in enumerate(sentence):
            if word.isalpha() == False:
                for letter in word:
                    if letter.isalpha() == False:
                        word = re.sub(letter, '', word)
                        sentence[count] = word
        
        sentence = " ".join(sentence)
        gold_values[path_file] = sentence
        
    list_data = gold_values.keys()
    
    with open(name, 'w') as f:
        for key in gold_values.keys():
            f.write("%s\t%s\n"%(key,gold_values[key]))  
    
    return list_data, gold_values

def main(data,name,files_path):
    """Process Wav2Vec2 model on a dataset and returns .
    
    Parameters
    ----------
        data : list
        List of filenames belonging to the train, test or validation dataset.
        
        name : str
        Name for output file.
        
        files_path : str
        Path to folder containing .wav files from Mozilla Common Voice Corpus (8.0)
        
    Produces
    -------
        csv file
        List of audio filenames and their translation.
    """
    
    processor = Wav2Vec2ProcessorWithLM.from_pretrained("Yehor/wav2vec2-xls-r-1b-uk-with-lm")
    model = Wav2Vec2ForCTC.from_pretrained("Yehor/wav2vec2-xls-r-1b-uk-with-lm")
    model.to('cpu')
    
    performed_values = {}
    
    for i, file in enumerate(data):
        print("Processing file",i,"of",len(data),"--- %s seconds" % round(time.time() - start_time, 2))
        
        wav_file_path = os.path.join(files_path, file)
        waveform, sample_rate = torchaudio.load(wav_file_path)

        if sample_rate != 16000:
            resample = torchaudio.transforms.Resample(
                sample_rate, 16000, resampling_method='sinc_interpolation')
            speech_array = resample(waveform)
            sp = speech_array.squeeze().numpy()
        else:
            sp = waveform.squeeze().numpy()

        input_values = processor(sp,
                                 sample_rate=16000,
                                 return_tensors="pt").input_values

        with torch.no_grad():
            logits = model(input_values).logits

        prediction = processor.batch_decode(logits.numpy()).text
        #print(prediction[0])
        
        performed_values[file] = prediction[0]
        
    with open(name, 'w') as f:
        for key in performed_values.keys():
            f.write("%s\t%s\n"%(key,performed_values[key]))
        f.close()


train_data, truth_train = get_dataset('../dataset_text/train.tsv', '../ground_truth/truth_train.csv')
#test_data, truth_test = get_dataset('../dataset_text/test.tsv', '../ground_truth/truth_test.csv')
#val_data, truth_val = get_dataset('../dataset_text/validated.tsv', '../ground_truth/truth_val.csv')

main(train_data,"w2v_performed_train.csv","/srv/data/guslegbe/stt/dataset_audio/")
#main(test_data,"w2v_performed_test.csv","/srv/data/guslegbe/stt/dataset_audio/")
#main(val_data,"w2v_performed_val.csv","/srv/data/guslegbe/stt/dataset_audio/")


