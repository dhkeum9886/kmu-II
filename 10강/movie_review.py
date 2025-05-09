import nltk

nltk.download('movie_reviews')
from nltk.corpus import movie_reviews

sentences = [list(s) for s in movie_reviews.sents()]
from gensim.models.word2vec import Word2Vec

model = Word2Vec(sentences)
model.save('mytest.model')
model.init_sims(replace=True)
model.wv.similarity('actor', 'actress')
model.wv.most_similar("accident")
model.wv.most_similar(positive=['she', 'actor'], negative='actress', topn=5)
model.wv.get_vector('actor')   # a vector for ‘actor’
model.wv.get_vector('actress') # a vector for ‘actress’

