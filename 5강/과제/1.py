from konlp.kma.klt2023 import klt2023
from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Komoran

text = "안녕하세요. 국민대학교 소프트웨어융합대학원 인공지능응용 K2025029 금동환입니다."

print('------------------- klt2023')
konltk=klt2023()
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


