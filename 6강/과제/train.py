import sentencepiece as spm

sp = spm.SentencePieceProcessor()

input_file = 'ITnews1000.txt'
model_prefix = 'mymodel'

vocab_size = 8000
model_type = 'unigram'

spm.SentencePieceTrainer.Train(input=input_file, model_prefix=model_prefix, model_type=model_type, vocab_size=vocab_size)

