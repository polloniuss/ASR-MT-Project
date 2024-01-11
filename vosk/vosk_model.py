#!/usr/bin/env python3

# Importing libraries
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import string
import pandas as pd
import re
import csv
import time
start_time = time.time()

SetLogLevel(0)

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
        sentence = re.sub(r"[—–«»…]", '', sentence)
        
        #Removes unecessary whitespaces
        sentence = sentence.split()
        sentence = " ".join(sentence)
        
        gold_values[path_file] = sentence
        
    list_data = gold_values.keys()
    
    with open(name, 'w') as f:
        for key in gold_values.keys():
            f.write("%s\t%s\n"%(key,gold_values[key]))
    
    return list_data, gold_values
    
train_data, truth_train = get_dataset('dataset_text/train.tsv', 'output_truth/truth_train.csv')
test_data, truth_test = get_dataset('dataset_text/test.tsv', 'output_truth/truth_test.csv')
val_data, truth_val = get_dataset('dataset_text/validated.tsv', 'output_truth/truth_val.csv')

def run_model(dataset, name):
    """Runs pre-trained model VOSK on dataset and returns performed speech to text.
    
    Parameters
    ----------
        data : list
        List of wav files.
        
        name : str
        Name for output file.
        
    Returns
    -------
        performed_values : dict
        Audio filename as key and its written transcription as value.
    """
    
    path_dataset = "dataset_audio/"
    performed_values = {}
    model = Model("model")
    
    for i, file in enumerate(dataset):
        print("Processing file",i,"of",len(dataset),"--- %s seconds" % round(time.time() - start_time, 2), end='\r')
        path_wav = os.path.join(path_dataset, file)
        wf = wave.open(path_wav, "rb")
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                #print(rec.Result())
                pass
            else:
                #print(rec.PartialResult())
                pass
        
        result = rec.FinalResult().split('"text" : "')[1]
        result = result.split('"')[0]
        
        performed_values[file] = result
    
    print(performed_values)
    
    with open(name, 'w') as f:
        for key in performed_values.keys():
            f.write("%s\t%s\n"%(key,performed_values[key]))
    
    return performed_values
    
#perfomed_train = run_model(train_data, "output_performed/performed_train.csv")
#perfomed_test = run_model(test_data, "output_performed/performed_test.csv")
perfomed_val = run_model(val_data, "output_performed/performed_val.csv")

"""
TO DO:

- write performed results in output file
- write new python code (jupyter notebook ?) and access the output files
- compute cosine similarity on results
- show results with matplotlib

"""
