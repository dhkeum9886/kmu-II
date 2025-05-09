한글 위키 데이터셋 및 형태소 분석 결과 파일

- ko_wiki_text.txt -- 한글 위키 데이터셋 원본 텍스트(utf-8 인코딩)
- ko_wiki_text-KMA.txt -- ko_wiki_text.txt을 형태소 분석한 것(utf-8 인코딩)

- ko_wiki_text_cp949.txt -- 한글 위키 데이터셋 원본 텍스트(cp949 인코딩)
- ko_wiki_text-KMA-cp949.txt -- ko_wiki_text.txt을 형태소 분석한 것(cp949 인코딩)

[참고] 형태소 분석 과정
  C> iconv -c -f utf-8 -t cp949 < ko_wiki_text.txt > ko_wiki_text_cp949.txt
  C> index2018.exe -c ko_wiki_text_cp949.txt ko_wiki_text-KMA-cp949.txt
  C> iconv -c -f cp949 -t utf-8 < ko_wiki_text-KMA-cp949.txt > ko_wiki_text-KMA.txt

[참고] KLT2000 형태소 분석기 -- index2018.exe 사용법
   https://cafe.naver.com/nlpkang/3
   https://cafe.naver.com/nlpkang/41 -- 다운로드
