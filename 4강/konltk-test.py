# https://konlpy.org/ko/v0.5.2/references/
# https://konlpy.org/ko/v0.5.2/#api


from konlp.kma.klt2023 import klt2023
k = klt2023()
simple_txt = "내 눈을 본다면 밤하늘의 별이 되는 기분을 느낄 수 있을 거야"
print(u'\n0. KLT2000 분석 결과')
print(k.pos(simple_txt))
print(k.morphs(simple_txt))
print(k.nouns(simple_txt))


from konlpy.utils import pprint

from konlpy.tag import Okt
okt = Okt()
print(u'\n1. Okt 분석 결과')
print(okt.morphs(u'단독입찰보다 복수입찰의 경우'))
print(okt.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요'))
print(okt.phrases(u'날카로운 분석과 신뢰감 있는 진행으로'))
print(okt.pos(u'이것도 되나욬ㅋㅋ'))

from konlpy.tag import Kkma
kkma = Kkma()
print(u'\n2. Kkma 분석 결과')
pprint(kkma.sentences(u'네 , 안녕하세요. 반갑습니다.'))
pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요'))
pprint(kkma.pos(u'오류보고는 실행환경 , 에러메세지와함께 설명을 최대한상세히!^^'))

from konlpy.tag import Komoran
#komoran = Komoran(userdic='/tmp/dic.txt')
komoran = Komoran()
print(u'\n3. Komoran 분석 결과')
print(komoran.morphs(u'우왕 코모란도 오픈소스가 되었어요'))
print(komoran.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요!'))
print(komoran.pos(u'혹시 바람과 함께 사라지다 봤어?'))

from konlpy.tag import Hannanum
hannanum = Hannanum()
print(u'\n4. Hannanum 분석 결과')
print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.morphs(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요'))
print(hannanum.pos(u'웃으면 더 행복합니다!'))
