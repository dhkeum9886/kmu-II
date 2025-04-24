import sys
from konlp.kma.klt2023 import klt2023
from collections import Counter, defaultdict

#
# simple_txt = "내 눈을 본다면 밤하늘의 별이 되는 기분을 느낄 수 있을 거야"
# print(u'\n0. KLT2000 분석 결과')
# print(k.pos(simple_txt))
# print(k.morphs(simple_txt))
# print(k.nouns(simple_txt))


def text_mining(lines):
    result = []
    klt = klt2023()
    for line in lines:
        result.extend(klt.nouns(line))
    return result


def read():
    def input_file(filename):
        lines = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, start=1):
                    if len(line.strip()) > 0:
                        lines.append(line.strip())
        except FileNotFoundError:
            print(f"Error: 파일을 찾을 수 없습니다 -> {filename}")
            sys.exit(1)
        finally:
            return lines

    input_path = sys.argv[1]
    return input_file(input_path)


# def top_words_in_dict(word_list, dictionary, top_n: int = 100):
#     dict_set = set(dictionary)
#     filtered = [word for word in word_list if word in dict_set]
#
#     counter = Counter(filtered)
#     return counter.most_common(top_n)


def init_dict():
    def dict_file(filename):
        emo_dict = {}
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, start=1):
                    if len(line.strip()) > 0:
                        # lines.append(line.strip())
                        print(line.strip())
                        splited = line.strip().split('\t')
                        emo_dict[splited[0]] = {
                            'cat': splited[1],
                            'con': splited[2],
                        }

        except FileNotFoundError:
            print(f"Error: 파일을 찾을 수 없습니다 -> {filename}")
            sys.exit(1)
        finally:
            return emo_dict

    dict_path = sys.argv[2]
    return dict_file(dict_path)


def analyze_emotions(word_list, emo_dict, top_n: int = 100):
    # 1) emo_dict에 있는 단어만 필터링
    filtered = [w for w in word_list if w in emo_dict]

    # 2) 단어별 등장 횟수 집계
    counts = Counter(filtered)

    # 3) 단어→카테고리 매핑
    word_cat = {w: emo_dict[w]['cat'] for w in counts}

    # 4) Top N 단어와 카테고리 함께 묶기
    most_common = counts.most_common(top_n)
    top_words = [(w, cnt, word_cat[w]) for w, cnt in most_common]

    # 5) 카테고리별 등장 횟수 집계
    cat_counts = Counter(word_cat[w] for w in filtered)
    cat_counts_list = cat_counts.most_common()

    return top_words, cat_counts_list


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <emotion_dict_file>")
        sys.exit(1)

    # input file
    lines = read()
    word_list = text_mining(lines)

    # emo file
    emo_dict = init_dict()
    # print('----------')
    # print(emo_dict)
    # word_list = ['황송스럽다', '황송스럽다', '훼손하다']

    top_words, cat_counts = analyze_emotions(word_list, emo_dict)

    # ◼ Top words by frequency (단어, count, 카테고리)
    print("⏫ Top words by frequency:")
    for word, count, cat in top_words:
        print(f"{word}: {count} ({cat})")

    # ◼ Category counts
    print("\n🏷 Category counts:")
    for cat, count in cat_counts:
        print(f"{cat}: {count}")

    ## TODO 각 파트 별 감정 파이차트
    ## 파트별 그래프 감정 그래프