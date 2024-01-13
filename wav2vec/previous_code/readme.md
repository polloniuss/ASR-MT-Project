# ⚠️ Important Note

## README has not yet been updated to the most recent code

Inside `w2v_model.py` please change the third parameter of line [133](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L133) to your path to folder containing .wav files from Mozilla Common Voice Corpus.

### Process train, test or validation datasets:

- Lines [133](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L133) and [137](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L137) are used for `train` dataset.
- Lines [134](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L134) and [138](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L138) are used for `test` dataset.
- Lines [135](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L135) and [139](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L139) are used for `val` dataset.


In order to process train, test or validation dataset, please comment and uncomment lines [133](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L133), [134](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L135) or [135](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L135) according to your wishes.

Update your path to dataset in lines [133](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L133), [134](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L134) and [135](https://github.com/polloniuss/ASR-MT-project/blob/dc672f024b8fdcf36e7ab056e00c91f200b09973/wav2vec/previous_code/w2v_model.py#L135).


#### For example if you want to process `test` dataset:

Uncomment lines 133 and 137, change the path in the third parameters and comment lines 134, 135, 138 and 139.

### Run Wav2Vec:
From wav2vec folder, run `python w2v_model.py`.
