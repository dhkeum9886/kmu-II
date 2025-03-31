import sentencepiece as spm
sp = spm.SentencePieceProcessor()

spm.SentencePieceTrainer.Train('--input=ITnews1000.txt --model_prefix=ITnews --vocab_size=8000')
#spm.SentencePieceTrainer.Train('--input=gtlee.txt --model_prefix=gtlee --vocab_size=16000')
#spm.SentencePieceTrainer.Train('--input=ko_wiki_text.txt --model_prefix=kowiki --vocab_size=64000')

sp.load('ITnews.model')
#sp.load('gtlee.model')
#sp.load('kowiki.model')

# encode: text => id
text='행정안전부는 오는 20일부터 버스·전철 등 대중교통과 마트 등 대형시설 안의 개방형 약국에서 마스크 착용 의무를 해제한다고 밝혔습니다.'
print(sp.encode_as_pieces(text))
print(sp.encode_as_ids(text))

text2='전세계적으로 ‘챗봇 돌풍’을 일으킨 생성형 인공지능(AI) 챗GPT 개발사인 오픈AI가 14일(현지시간) 더욱 강력해신 새로운 인공지능 툴인 GPT-4를 공개했다. AI 기술을 놓고 구글과 무한 경쟁에 돌입한 마이크로소프트(MS)는 즉각 자사 검색엔진에 GPT-4 탑재를 선언, 구글과의 격차 벌리기에 나섰다.'
print(sp.encode_as_pieces(text2))
print(sp.encode_as_ids(text2))

# decode: id => text
#print(sp.decode_pieces(['_This', '_is', '_a', '_t', 'est']))
#print(sp.decode_ids([212, 32, 10, 587, 446]))
