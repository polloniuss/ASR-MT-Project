# Speech To Text work - Bérénice

Report on frameworks can be found at [report_frameworks.md](https://github.com/mabelai/speech-to-text/blob/master/report_frameworks.md) .

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


Inside `w2v_model.py` please change the third parameter of line [126](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L126) to your path to folder containing .wav files from Mozilla Common Voice Corpus.

### Process train, test or validation datasets:

- Lines [122](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L122) and [126](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L126) are used for `train` dataset.
- Lines [123](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L123) and [127](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L127) are used for `test` dataset.
- Lines [124](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L124) and [128](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L128) are used for `val` dataset.


In order to process train, test or validation dataset, please comment and uncomment lines [122](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L122), [123](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L123) or [124](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L124) according to your wishes.

Update your path to dataset in lines [126](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L126), [127](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L127) and [128](https://github.com/mabelai/speech-to-text/blob/5d00c8df1384bceee7d055459847cab509c52cee/wav2vec/w2v_model.py#L128).


#### For example if you want to process `test` dataset:

Uncomment lines 123 and 127, change the path in the third parameters or lines 127 and comment lines 122, 124, 126 and 128.

### Run Wav2Vec:
From wav2vec folder, run `python w2v_model.py`.


## To do list:
- commands / how to reproduce steps / how to compute code
- classification of errors (age ; up/down votes ; ...)
- speed rate for Wav2Vec
