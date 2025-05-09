from gensim.models import word2vec
import sys


def wv_train_tokens(filename):
    print(f"Training word embedding vectors for <{filename}>.")
    f = open(filename, "r", encoding='utf-8')
    text = f.readlines()
    f.close()
    tokens = []
    for sent in text:
        tokens.append(sent.split())
    model = word2vec.Word2Vec(sentences=tokens, vector_size=300, window=5, min_count=2, workers=4)
    return model


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("C> wv_train_tokens.py token-list.txt")
        exit()

    tokenized_file = sys.argv[1]
    model_file = tokenized_file[:-4] + '.model'
    model = wv_train_tokens(tokenized_file)
    # 'KMA tokenized text file'
    model.save(model_file)
    print(f"--> Model file <{model_file}> was created!\n")
