from jiwer import wer, cer, mer, wip
import csv

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
    
def asr_evaluation(truth, performed, txt):
    ground_truths = list(truth.values())
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
    

print("Evaluation")
truth = get_dataset("output_truth/truth_train.csv")
performed = get_dataset("output_performed_wav2vec2/w2v_performed_train.csv")
asr_evaluation(truth,performed,"Wav2Vec2")
