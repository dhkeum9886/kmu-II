from gensim.models import Word2Vec
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("C> wv_test.py word2vec.model")
        exit()
    print("Loading Korean word embedding vectors for 'KMA tokenized text file'.\n")
    model_name = sys.argv[1]
    # Word2Vec model -- 'word2vec-kowiki.model'
    model = Word2Vec.load(model_name)
    print(model.wv.get_vector(u'배우'))
    print(model.wv.get_vector(u'여배우'))
    print(model.wv.similarity(u'배우', u'여배우'))
    print(model.wv.similarity(u'배우', u'남자'))
    print(model.wv.similarity(u'남자', u'여배우'))
    print(model.wv.most_similar(positive=[u'남자'], topn=5))
    print(model.wv.most_similar(positive=[u'남자', u'여배우'], negative=[u'배우'], topn=5))
