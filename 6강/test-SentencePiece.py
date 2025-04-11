import sentencepiece as spm

# train
# spm.SentencePieceTrainer.train(
#     '--input=kowikitext_20200920.test --model_prefix=kowikitext --vocab_size=8000 --character_coverage=0.9995'
# )


# en/decoding
sp = spm.SentencePieceProcessor()
sp.load('kowikitext.model')


text = "국민대학교 소프트웨어융합대학원 K2025029 금동환 인공지능기초응용II 6주차 과제입니다."
print(sp.encode_as_pieces(text))
print(sp.encode_as_ids(text))
print('-----------------------------------')
print(sp.decode_pieces(sp.encode_as_pieces(text)))
print(sp.decode_ids(sp.encode_as_ids(text)))
