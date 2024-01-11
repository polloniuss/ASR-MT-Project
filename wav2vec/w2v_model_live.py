# Importing librairies

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
from collections import Counter
import numpy as np
import operator
import soundfile

from torchaudio.models.wav2vec2.utils import import_huggingface_model
import torch.quantization
import torch.nn as nn

import torchvision
from torch.utils.mobile_optimizer import optimize_for_mobile

#from pyctcdecode import build_ctcdecoder
#import multiprocessing

#access_token = "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"
#!export HF_DATASETS_CACHE="/media/berenice/Healthy_Windows/Users/berenice/Documents/Storage/work/mission/wav2vec_model_storage"

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
        
    list_data = list(gold_values.keys())[707:]

    with open(name, 'w') as f:
        for key in gold_values.keys():
            f.write("%s\t%s\n"%(key,gold_values[key]))
    
    return list_data, gold_values

def get_model(name):
    
    #original = Wav2Vec2ForCTC.from_pretrained("Yehor/wav2vec2-xls-r-300m-uk-with-small-lm", cache_dir="/media/berenice/Healthy_Windows/Users/berenice/Documents/Storage/work/mission/wav2vec_model_storage")
    original = Wav2Vec2ForCTC.from_pretrained("Yehor/wav2vec2-xls-r-300m-uk-with-small-lm").to('cpu')
    original.config.return_dict = False
    model = import_huggingface_model(original)
    scripted_model = torch.jit.script(model)
    print_size_of_model(model,"Original model")
    
    model.eval()
    quantized_model = torch.quantization.quantize_dynamic(
        model, {nn.Linear}, dtype=torch.qint8
    )
    print_size_of_model(quantized_model,"Quantized model")
    quantized_model.to('cpu')
    
    torch.save(quantized_model.state_dict(), name)
    
    quantized_model.load_state_dict(torch.load(name))
    
    return quantized_model
    
def print_size_of_model(model, label=""):
    torch.save(model.state_dict(), "temp.p")
    size=os.path.getsize("temp.p")
    print("model: ",label,' \t','Size (KB):', size/1e3)
    os.remove('temp.p')
    return size

def main(data,name,files_path,model):
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
    
    #model = Wav2Vec2ForCTC.from_pretrained("Yehor/wav2vec2-xls-r-300m-uk-with-small-lm")
    processor = Wav2Vec2ProcessorWithLM.from_pretrained("Yehor/wav2vec2-xls-r-300m-uk-with-small-lm")
    model.to('cpu')
    
    performed_values = {}
    
    """
    unigrams_file = 'unigrams.txt'
    kenlm_model_path = '5gram.arpa'
    unigrams = []
    labels = ["'", "-", "", "\u2047", " ", "\u0430", "\u0431", "\u0432", "\u0433", "\u0434", "\u0435", "\u0436", "\u0437", "\u0438", "\u0439", "\u043a", "\u043b", "\u043c", "\u043d", "\u043e", "\u043f", "\u0440", "\u0441", "\u0442", "\u0443", "\u0444", "\u0445", "\u0446", "\u0447", "\u0448", "\u0449", "\u044c", "\u044e", "\u044f", "\u0454", "\u0456", "\u0457", "\u0491", "<s>", "</s>"]
    
    with open(unigrams_file, 'r') as file:
        unigrams = [it.strip() for it in file.readlines()]
        file.close()
    
    decoder = build_ctcdecoder(
        labels,
        kenlm_model_path=kenlm_model_path,
        unigrams=unigrams,
        alpha=0.5,
        beta=1.5,
        unk_score_offset=-10.0,
        lm_score_boundary=True,
    )
    """
    
    with open(name, 'w') as f:
    
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

            #Processor combines feature extractor and tokenizer
            #Feature extractor processes speech signal to the model's input format
            #Tokenizer processes the model's output format to text
            input_values = processor(sp,
                                     sample_rate=16000,
                                     return_tensors="pt").input_values

            with torch.no_grad():
                #logits, _ = model(input_values).logits
                logits = model(input_values)[0].numpy()

            #with multiprocessing.get_context("fork").Pool() as pool:
            #    prediction = decoder.decode_batch(pool, logits)

            prediction = processor.batch_decode(logits).text#.numpy().text

            performed_values[file] = prediction[0]
            f.write("%s\t%s\n"%(file,performed_values[file]))
            
        f.close()

    """
    with open(name, 'w') as f:
        for key in performed_values.keys():
            f.write("%s\t%s\n"%(key,performed_values[key]))
        f.close()
    """

train_data, truth_train = get_dataset('../dataset_translations/train.tsv', '../ground_truth/truth_train.csv')
#test_data, truth_test = get_dataset('../dataset_translations/test.tsv', '../ground_truth/truth_test.csv')
#val_data, truth_val = get_dataset('../dataset_translations/validated.tsv', '../ground_truth/truth_val.csv')

model = get_model("w2v_model_live.pth")
#main(train_data,"w2v_performed_live_model_test.csv","../dataset_audio/train",model)
main(train_data,"w2v_performed_live_model.csv","/srv/data/guslegbe/dataset_audio/",model)
#main(test_data,"w2v_performed_test.csv","/srv/data/guslegbe/stt/dataset_audio/")
#main(val_data,"w2v_performed_val.csv","/srv/data/guslegbe/stt/dataset_audio/")


