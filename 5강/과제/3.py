import sys

from konlp.kma.klt2023 import klt2023
from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Komoran


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return "\n".join(f.readlines())


if __name__ == '__main__':
    text = None
    if len(sys.argv) == 2:
        textFile = sys.argv[1]
        outputFile = textFile.replace('.txt', '-KMA.txt')
        text = load_file(textFile)

    print('------------------- klt2023')
    konltk = klt2023()
    print(konltk.pos(text))
    print(konltk.morphs(text))
    print(konltk.nouns(text))
    print('------------------- Okt')
    okt = Okt()
    print(okt.pos(text))
    print(okt.morphs(text))
    print(okt.nouns(text))
    print('------------------- Kkma')
    khma = Kkma()
    print(khma.pos(text))
    print(khma.morphs(text))
    print(khma.nouns(text))
    print('------------------- Komoran')
    komoran = Komoran()
    print(komoran.pos(text))
    print(komoran.morphs(text))
    print(komoran.nouns(text))
