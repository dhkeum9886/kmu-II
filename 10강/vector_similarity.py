from sklearn.metrics.pairwise import cosine_similarity
import math

cosine_similarity([[1, 0, -1]], [[-1, -1, 0]])


# Compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
def cosine_similarity(v1, v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)


v1, v2 = [3, 45, 7, 2], [2, 54, 13, 15]
print(v1, v2, cosine_similarity(v1, v2))

print('-------------------------------------')

from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from gensim.models.word2vec import Word2Vec
model = Word2Vec.load("mytest.model")

va = model.wv.get_vector('actor').reshape(1, -1)  # a vector for 'actor'
vb = model.wv.get_vector('actress').reshape(1, -1)  # a vector for 'actress'

print(va, vb, cosine_similarity(va, vb)[0,0])