#!/usr/bin/env python3

# Importing libraries
import nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('stopwords_uk.txt') as f:
    lines = f.readlines()
    f.close()

stopwords = []
for word in lines:
    stopwords.append(word)
    
def get_dataset(data):
    """Gets and returns filename and sentences from a dataset.
    
    Parameters
    ----------
        data : str
        Path to csv file.
        
    Returns
    -------
        dict_values : dict
        Audio filename as key and its written transcription as value.
    """
    dict_values = {}
    
    with open(data, newline='') as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|')
        for row in reader:
            row = ' '.join(row).split('\t')
            dict_values[row[0]] = row[1].lower()
            
        f.close()
    
    return dict_values
    
truth_train = get_dataset("output_truth/truth_train.csv")
#truth_test = get_dataset("output_truth/truth_test.csv")
#truth_val = get_dataset("output_truth/truth_val.csv")

performed_train = get_dataset("output_performed/performed_train.csv")
#performed_test = get_dataset("output_performed/performed_test.csv")
#performed_val = get_dataset("output_performed/performed_val.csv")

def cosine_similarity(truth, performed):
    """Computes cosine similarity between truth and performed values on dataset.
    
    Parameters
    ----------
        truth : dict
        Audio filename as key and its written transcription as value.
        
        performed : dict
        Audio filename as key and its written transcription as value.
        
    Returns
    -------
        dict_values : dict
        Audio filename as key and its written transcription as value.
    """
    
    dict_similarity = {}
    total_cosine = 0
    count = 0
    
    for key, truth_sent in truth.items():
        t_list = []
        p_list = []
        
        performed_sent = performed[key]
        
        """
        LEMMATIZATION TO DO
        """
        
        # Tokenization
        truth_sent = word_tokenize(truth_sent)
        performed_sent = word_tokenize(performed_sent)
        
        # Remove stopwords from sentences
        truth_sent = {word for word in truth_sent if not word in stopwords} 
        performed_sent = {word for word in performed_sent if not word in stopwords}
        
        # Form a set containing keywords of both sentences 
        rvector = truth_sent.union(performed_sent)
        
        for word in rvector:
            if word in truth_sent:
                t_list.append(1)
            else:
                t_list.append(0)
            if word in performed_sent:
                p_list.append(1)
            else:
                p_list.append(0)
            
        c = 0
        
        for i in range(len(rvector)):
            c += t_list[i]*p_list[i]
        try:
            cosine = c / float((sum(t_list)*sum(p_list))**0.5)
            total_cosine += cosine
            count += 1
        except ZeroDivisionError:
            cosine = "Division Error"
            print("Truth sentence:",truth_sent,"\nPerformed sentence:",performed_sent)
        
        #print("Truth sentence:",truth_sent,"\nPerformed sentence:",performed_sent,"\nSimilarity:", cosine)
    print(total_cosine/count)
    
    #return dict_similarity

cosine_similarity(truth_train, performed_train)
