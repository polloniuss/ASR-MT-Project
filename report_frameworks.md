# Report

Comparison frameworks Vosk, Wav2Vec 2.0, DeepSpeech (Coqui STT)

| Framework | Version | Link | Ukrainian STT Model |
| --- | --- | --- | --- |
| Wav2Vec 2.0 | ... | [commit id](https://github.com/egorsmkv/wav2vec2-uk-demo/commit/0ef29022e939c43968465d1b8119915123a88be6) | [wav2vec2-xls-r-1b-uk-with-lm](https://huggingface.co/Yehor/wav2vec2-xls-r-1b-uk-with-lm) |
| Wav2Vec 2.0 | ... | unknown commid id | [wav2vec2-xls-r-300m-uk-with-lm](https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-lm) |
| Wav2Vec 2.0 | ... | [commid id](https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm/commit/bbee575bd90fd6b5fb6a1ae0a052aae56f49d8fa) | [wav2vec2-xls-r-300m-uk-with-small-lm](https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm) |
| Vosk | [v0.3.32](https://github.com/alphacep/vosk-api/tree/v0.3.32) | [commit id](https://github.com/alphacep/vosk-api/commit/a87f2e1e076a52ce0ec155319063251ce419b182) | [vosk-model-uk-v3](https://alphacephei.com/vosk/models) |
| DeepSpeech | [v0.5](https://github.com/robinhad/voice-recognition-ua/tree/v0.5) | [commit id](https://github.com/robinhad/voice-recognition-ua/commit/b2b69bd3287894765a8309857fc8ab8fbcce4f39) | [DeepSpeech v0.9.3](https://github.com/robinhad/voice-recognition-ua/releases/tag/v0.4) |

## Comparison models (in %):

| Models | WER | CER | MER | WIP |
| --- | --- | --- | --- | --- |
| Wav2Vec 2.0 1b with LM | 13.7 | 2.3 | 13.5 | 77.9 |
| Wav2Vec 2.0 300m with LM | 18.2 | 3.3 | 17.8 | 71 |
| **Wav2Vec 2.0 300m with small LM** | **5.6** | **1.1** | **5.6** | **90.1** |
| Vosk | 23.8 | 7.6 | 23.5 | 61.7 |

## Details:

I evaluated these models based on these four criteria, all scores range from 0.00 to 1.00:
- Word Error Rate (WER)
- Character Error Rate (CER)
- Match Error Rate (MER)
- Word Information Preserved (WIP)

When evaluating ASR performance, these metric tools are widely used and recommended by the US National Institute of Standards and Technology. They give a good idea of how well a model performs and the proportion of errors it does. These metrics compute the minimum-edit distance between the ground-truth sentence (i.e. original transcript) and the hypothesis sentence (i.e. produced transcript) of a speech-to-text API.

- **WER** is the proportion of transcritpion errors regarding the number of words in the ground-truth text. The calculation is based on the concept of Levenshtein distance. The lower the better (with 0 being a perfect score).
- **CER** is similar to WER but operates on character instead of word.
- **MER** is the proportion of input (ground-truth) / output (hypothesis) word matches which are errors.
- **WIP** is the proportion of information preserved (as opposed to Word Information Lost). The higher the better (with 1 being a perfect score).

I use the _JiWER_ python module that can be found here: https://github.com/jitsi/jiwer .

In order to conduct this experiment, I use the Ukrainian dataset from Mozilla Common Voice (version Common Voice Corpus 8.0) that can be found here: https://commonvoice.mozilla.org/en/datasets .

For memory reasons, I have conducted this experiment on a small sample of data. It consits on the 10 first .wav file from the training set. The models have been computed on the exact same sample of data.

## Models evaluated on a small sample (10 files):

**Model Wav2Vec2 1b with LM:** (Yehor/wav2vec2-xls-r-1b-uk-with-lm)

- Word Error Rate (WER) = 0.13636363636363635
- Character Error Rate (CER) = 0.015113350125944584
- Match Error Rate (MER) = 0.13432835820895522
- Word Information Preserved (WIP) = 0.7841491841491842

**Wav2Vec2 300m with LM:** (Yehor/wav2vec2-xls-r-300m-uk-with-lm)

- Word Error Rate (WER) = 0.07575757575757576
- Character Error Rate (CER) = 0.010075566750629723
- Match Error Rate (MER) = 0.07575757575757576
- Word Information Preserved (WIP) = 0.8673659673659673

**Wav2Vec2 300m with small LM:** (Yehor/wav2vec2-xls-r-300m-uk-with-small-lm)

- **Word Error Rate (WER) = 0.06060606060606061**
- **Character Error Rate (CER) = 0.010075566750629723**
- **Match Error Rate (MER) = 0.06060606060606061**
- **Word Information Preserved (WIP) = 0.8824609733700643**

**Model Vosk:**

- Word Error Rate (WER) = 0.3787878787878788
- Character Error Rate (CER) = 0.11335012594458438
- Match Error Rate (MER) = 0.36764705882352944
- Word Information Preserved (WIP) = 0.431002331002331

**Model DeepSpeech:**

- Word Error Rate (WER) = 0.4696969696969697
- Character Error Rate (CER) = 0.1712846347607053
- Match Error Rate (MER) = 0.45588235294117646
- Word Information Preserved (WIP) = 0.3241003787878788

## Models evaluated on training set (8915 files):

**Model Wav2Vec2 1b with LM:**

- Word Error Rate (WER) = 0.13752250040909836
- Character Error Rate (CER) = 0.023215803056330878
- Match Error Rate (MER) = 0.13543479662218785
- Word Information Preserved (WIP) = 0.7791868087568564

**Wav2Vec2 300m with LM:**

- Word Error Rate (WER) = 0.18267059401080019
- Character Error Rate (CER) = 0.03383325134362282
- Match Error Rate (MER) = 0.17845666874490432
- Word Information Preserved (WIP) = 0.7102410684438888

**Wav2Vec2 300m with small LM:**

- **Word Error Rate (WER) = 0.05691376206840124**
- **Character Error Rate (CER) = 0.011090971749064133**
- **Match Error Rate (MER) = 0.05651425043060024**
- **Word Information Preserved (WIP) = 0.9015561407465607**

**Model Vosk:**

- Word Error Rate (WER) = 0.23858615611192932
- Character Error Rate (CER) = 0.07681200587037826
- Match Error Rate (MER) = 0.23539668700959024
- Word Information Preserved (WIP) = 0.61722316027047
