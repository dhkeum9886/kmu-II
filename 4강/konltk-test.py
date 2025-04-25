# https://konlpy.org/ko/v0.5.2/references/
# https://konlpy.org/ko/v0.5.2/#api


from konlp.kma.klt2023 import klt2023
k = klt2023()
simple_txt = "이날이야말로 동소문 안에서 인력거꾼 노릇을 하는 김 첨지에게는 오래간만에도 닥친 운수 좋은 날이었다. 문안에(거기도 문밖은 아니지만) 들어간답시는 앞집 마나님을 전찻길까지 모셔다 드린 것을 비롯으로 행여나 손님이 있을까 하고 정류장에서 어정어정하며 내리는 사람 하나하나에게 거의 비는 듯한 눈결을 보내고 있다가 마침내 교원인 듯한 양복장이를 동광학교(東光學校)[7]까지 태워다 주기로 되었다."
print(u'\n0. KLT2000 분석 결과')
print(k.pos(simple_txt))
print(k.morphs(simple_txt))
print(k.nouns(simple_txt))


from konlpy.utils import pprint

from konlpy.tag import Okt
okt = Okt()
print(u'\n1. Okt 분석 결과')
print(okt.morphs(simple_txt))
print(okt.nouns(simple_txt))
print(okt.phrases(simple_txt))
print(okt.pos(simple_txt))

from konlpy.tag import Kkma
kkma = Kkma()
print(u'\n2. Kkma 분석 결과')
pprint(kkma.sentences(simple_txt))
pprint(kkma.nouns(simple_txt))
pprint(kkma.pos(simple_txt))

from konlpy.tag import Komoran
#komoran = Komoran(userdic='/tmp/dic.txt')
komoran = Komoran()
print(u'\n3. Komoran 분석 결과')
print(komoran.morphs(simple_txt))
print(komoran.nouns(simple_txt))
print(komoran.pos(simple_txt))

from konlpy.tag import Hannanum
hannanum = Hannanum()
print(u'\n4. Hannanum 분석 결과')
print(hannanum.analyze(simple_txt))
print(hannanum.morphs(simple_txt))
print(hannanum.nouns(simple_txt))
print(hannanum.pos(simple_txt))
