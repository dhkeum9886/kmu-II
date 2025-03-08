import os
import nltk
from collections import Counter
from soynlp.noun import LRNounExtractor
nltk.download('punkt')
nltk.download('punkt_tab')

def analyze_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    text = ''.join(lines)

    # 기본 텍스트 분석
    byte_size = os.path.getsize(file_path)  # 파일 바이트 크기
    char_count = len(text)  # 문자 수
    word_count = len(nltk.word_tokenize(text))  # 단어 수 (nltk 토크나이저 사용)
    line_count = len(lines)  # 라인 수

    # 형태소 분석 (soynlp를 사용한 명사 추출)
    noun_extractor = LRNounExtractor()
    nouns = noun_extractor.train_extract([text])
    sorted_nouns = sorted(nouns.items(), key=lambda x: x[1], reverse=True)[:10]  # 상위 10개 명사 추출

    # 결과 출력
    print(f"파일: {file_path}")
    print(f"바이트 크기: {byte_size} bytes")
    print(f"문자 수: {char_count}")
    print(f"단어 수: {word_count}")
    print(f"라인 수: {line_count}\n")

    print("상위 10개 명사:")
    for word, score in sorted_nouns:
        print(f"{word}: {score}")

file_path = "콩쥐팥쥐전.txt"  # 분석할 파일 경로
analyze_text_file(file_path)
