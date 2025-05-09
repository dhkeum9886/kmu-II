import codecs


def load_pre_tokenized(filename):
    sentences = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # 토큰이 "단어/POS" 형식이면, 필요에 따라 split('/') 로 앞부분만 사용
            tokens = [ tok.split('/')[0] for tok in line.split() ]
            sentences.append(tokens)
    return sentences

def read_data(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
    data = data[1:]  # header 제외
    return data


train_data = read_data('ratings_train.txt')

from konlpy.tag import Okt
from konlp.kma.klt2023 import klt2023

tagger = klt2023()  # Okt()


def tokenize(doc):
    # return ['/'.join(t) for t in tagger.pos(doc)]
    return tagger.pos(doc)


print('KLT2000 -- morph analysis for 200K Naver movie reviews. Waiting several minutes...')
train_docs = [row[1] for row in train_data]
sentences = [tokenize(d) for d in train_docs]

from gensim.models import word2vec

model = word2vec.Word2Vec(sentences)
model.save('mytest.model')

model.init_sims(replace=True)
print(model.wv.similarity('배우', '여배우'))
print(model.wv.similarity('배우', '남자'))

print(model.wv.most_similar(positive=tokenize(['남자', '여배우']), negative=tokenize(u'배우'), topn=5))
