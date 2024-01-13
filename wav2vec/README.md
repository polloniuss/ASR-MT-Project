# Wav2Vec2 Transcription and Translation

## Overview

This script utilizes the Wav2Vec2 model for Automatic Speech Recognition (ASR) and Machine Translation (MT). It focuses on processing a given dataset, quantizing the model, and producing a CSV file with audio filenames and transcriptions.

## Requirements

- Ensure all requirements are installed: `pip install torch torchaudio transformers soundfile pandas re csv string difflib operator collections numpy matplotlib`
- Update the dataset path, model name, and other parameters in the scripts.

## Scripts

### 1. **Wav2Vec2 Transcription and Translation**

#### File: [w2v_model_live.py](https://github.com/polloniuss/ASR-MT-Project/blob/main/wav2vec/w2v_model_live.py)

- Utilizes the Wav2Vec2 model for ASR and Machine Translation.
- Text processing for transcription, including punctuation removal.
- Processes a given dataset, and produces CSV files with audio filenames and transcriptions.

### 2. **Wav2Vec2 Compression (Shrinking Bigfoot paper)**

#### File: [compression_model.ipynb](https://github.com/polloniuss/ASR-MT-Project/blob/main/wav2vec/compression_model.ipynb)

- Provides code for compressing the Wav2Vec2 model.
- Exports and quantizes the Wav2Vec2 model.
- Comparison of model sizes (original vs. quantized).

### 3. **ASR Evaluation and Error Analysis**

#### File: [classification_translations.ipynb](https://github.com/polloniuss/ASR-MT-Project/blob/main/wav2vec/classification_translations.ipynb)

- Evaluates ASR performance and conducts an in-depth analysis of transcription errors.
- Cleans the dataset by identifying and categorizing various types of errors, such as mismatching letters, added or missing letters, and positional errors in sentences.
- Provides statistical insights into the distribution and types of errors in different ASR models.
- Generates visualizations of error proportions by gender, age, upvotes, and downvotes.
- Implements functions like `tell_diff` to display differences between ground truth and performed sentences.
- Implements `understanding_only_one_error` to analyze words with only one mismatching letter.
- Implements `show_scores` to visualize error proportions by different attributes.
- Implements `create_csv` to generate CSV files of ground truth and performed sentences, as well as errors-only CSV files.

### Example Output:

**Output and statistics for Wav2Vec 2.0 1b with LM**
| Matching translations | Wrong translations because of split words | Wrong translations that are being reviewed | Only one wrong word in sentence | Positional error in sentence * |
|---------|----------|----------|---------|----------|
| 56.04 % | 9.23 % | 9.10 % | 14.98 % | 9.07 % |

*(For example if a word is split into two words, it will lead to a positional error in sentence.)* *

**Output and statistics for Wav2Vec 2.0 300m with small LM**
| Matching translations | Wrong translations because of split words | Wrong translations that are being reviewed | Only one wrong word in sentence | Positional error in sentence * |
|---------|----------|----------|---------|----------|
| 77.75 % | 1.79 % | 3.94 % | 10.06 % | 4.00 % |

**Output and statistics for Wav2Vec 2.0 300m with small LM (compressed)**
| Matching translations | Wrong translations because of split words | Wrong translations that are being reviewed | Only one wrong word in sentence | Positional error in sentence * |
|---------|----------|----------|---------|----------|
| 78.03 % | 1.68 % | 3.94 % | 9.90 % | 3.90 % |

# Important Note:

All letters from original annotations and performed output seem to be encoded in a specific form. It could affect the result of Speech To Text to Machine Translation.

