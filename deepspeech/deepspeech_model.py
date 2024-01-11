from jiwer import wer, cer, mer, wip
import csv
import subprocess

"""
['common_voice_uk_24017714.wav', 'common_voice_uk_24017716.wav', 'common_voice_uk_24017717.wav', 'common_voice_uk_24017732.wav', 'common_voice_uk_24017755.wav', 'common_voice_uk_24017768.wav', 'common_voice_uk_24017770.wav', 'common_voice_uk_24017771.wav', 'common_voice_uk_24017773.wav', 'common_voice_uk_24017774.wav']
"""

"""
{'dataset_audio/common_voice_uk_24017714.wav': "ти розпитав як до подоїти",
 'dataset_audio/common_voice_uk_24017716.wav': "у поході брали участь андрій олександр так званий невська",
 'dataset_audio/common_voice_uk_24017717.wav': "чого ради",
 'dataset_audio/common_voice_uk_24017732.wav': "а петро з по грецькому камінь а від твого",
 'dataset_audio/common_voice_uk_24017755.wav': "один узяв пиво й погоні заселив меч назад",
 'dataset_audio/common_voice_uk_24017768.wav': "розумний сидіти хвоста зав’язати",
 'dataset_audio/common_voice_uk_24017770.wav': "хоч ближче махнув до нього маленькі ставши у довгій не підперезані сорочці",
 'dataset_audio/common_voice_uk_24017771.wav': "жодну перепитав орест але гатило повторювати не любив",
 'dataset_audio/common_voice_uk_24017773.wav': "за на господар",
 'dataset_audio/common_voice_uk_24017774.wav': "я єсьм великий княже"}

"""

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

def main(list_train):
    
    print(list(list_train.keys())[:10])
    dict_val = {'dataset_audio/common_voice_uk_24017714.wav': "ти розпитав як до подоїти",
 'dataset_audio/common_voice_uk_24017716.wav': "у поході брали участь андрій олександр так званий невська",
 'dataset_audio/common_voice_uk_24017717.wav': "чого ради",
 'dataset_audio/common_voice_uk_24017732.wav': "а петро з по грецькому камінь а від твого",
 'dataset_audio/common_voice_uk_24017755.wav': "один узяв пиво й погоні заселив меч назад",
 'dataset_audio/common_voice_uk_24017768.wav': "розумний сидіти хвоста зав’язати",
 'dataset_audio/common_voice_uk_24017770.wav': "хоч ближче махнув до нього маленькі ставши у довгій не підперезані сорочці",
 'dataset_audio/common_voice_uk_24017771.wav': "жодну перепитав орест але гатило повторювати не любив",
 'dataset_audio/common_voice_uk_24017773.wav': "за на господар",
 'dataset_audio/common_voice_uk_24017774.wav': "я єсьм великий княже"}
    """
    for key in list_train.keys():
    
        !deepspeech --model uk.pbmm --scorer kenlm.scorer --audio dataset_audio/key
        
    print(len(list_train.keys()))
    """
    return dict_val

def asr_evaluation(truth, performed, txt):
    ground_truths = list(truth.values())[:10]
    hypothesis = list(performed.values())
    
    print("Model",txt,":\n")
    
    wer_score = wer(truth=ground_truths, hypothesis=hypothesis)
    print(f"Word Error Rate (WER) = {wer_score}")

    cer_score = cer(truth=ground_truths, hypothesis=hypothesis)
    print(f"Character Error Rate (CER) = {cer_score}")
    
    mer_score = mer(truth=ground_truths, hypothesis=hypothesis)
    print(f"Match Error Rate (MER) = {mer_score}")
    
    wip_score = wip(truth=ground_truths, hypothesis=hypothesis)
    print(f"Word Information Preserved (WIP) = {wip_score}")
    
def model(dict_truth):
    dataset = list(dict_truth.keys())
    
    path_dataset = "dataset_audio/"
    performed_values = {}
    #model = Model("model")
    
    for i, files in enumerate(dataset):
        print("Processing file",i,"of",len(dataset),"--- %s seconds" % round(time.time() - start_time, 2), end='\r')
        path_wav = os.path.join(path_dataset, files)
        
        
        
        process = subprocess.Popen(['deepspeech --model model.pbmm --scorer kenlm.scorer --audio', '...'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        stdout, stderr
        
        performed_values[files] = result
    
    print(performed_values)
    
    with open(name, 'w') as f:
        for key in performed_values.keys():
            f.write("%s\t%s\n"%(key,performed_values[key]))
    
    return performed_values
    

#print("Evaluation")
truth = get_dataset("output_truth/truth_train.csv")
model(truth)
#performed = main(truth)
#asr_evaluation(truth,performed,"DeepSpeech")
