# Speech To Text work - Bérénice

Report on frameworks can be found at [report_frameworks.md](https://github.com/polloniuss/ASR-MT-project/blob/main/report_frameworks.md) .

## How to run Wav2Vec2 :
Some dependencies are needed in order to run Wav2Vec2. A demo can be found [here](https://github.com/egorsmkv/wav2vec2-uk-demo).

### Install dependencies:
```
pip install https://github.com/huggingface/transformers/archive/refs/tags/v4.16.2.zip
pip install https://github.com/kpu/kenlm/archive/master.zip
pip install torch==1.9.1 torchaudio==0.9.1 pyctcdecode==0.3.0
```

### Download dataset:
I used the Ukrainian dataset from Mozilla Common Voice (version Common Voice Corpus 8.0) that can be found [here]( https://commonvoice.mozilla.org/en/datasets). I converted it into`.wav` files.

## Wav2Vec Folder

The "wav2vec" folder contains essential scripts and files related to the Wav2Vec2 model for Automatic Speech Recognition (ASR) and Machine Translation (MT). Here's an overview of the contents:

### 1. w2v_model_live.py
   - This script utilizes the Wav2Vec2 model for ASR and MT on medical conversations.
   - Focuses on processing a given dataset, quantizing the model, and producing a CSV file with audio filenames and transcriptions.

### 2. compression_model.ipynb
   - Provides code for compressing the Wav2Vec2 model.
   - Exports and quantizes the Wav2Vec2 model, comparing sizes between the original and quantized versions.

### 3. cleaning_and_analysis.ipynb
   - This notebook includes extensive work on cleaning the dataset and analyzing errors.
   - Defines functions to identify different types of errors in model transcriptions.
   - Compares performance across different Wav2Vec2 models and provides detailed statistics on errors.
   - Generates visualizations for demographic and voting information related to the dataset.

#### Important Note:
All three files collectively contribute to the transcription and analysis workflow, showcasing the usage, compression, and detailed error analysis of the Wav2Vec2 model.

## To do list:
- commands / how to reproduce steps / how to compute code
- classification of errors (age ; up/down votes ; ...)
- speed rate for Wav2Vec
