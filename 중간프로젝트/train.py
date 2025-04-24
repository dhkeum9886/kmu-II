import sentencepiece as spm

# train
spm.SentencePieceTrainer.train(
    '--input=kowikitext_20200920.train --model_prefix=kowikitext --vocab_size=50000 --character_coverage=0.9995'
)

