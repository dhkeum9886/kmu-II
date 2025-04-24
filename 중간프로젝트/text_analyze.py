import sys
from konlp.kma.klt2023 import klt2023
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 1) 사용할 한글 폰트 파일 경로 지정 (Windows 예시: 맑은고딕)
font_path = r"C:\Windows\Fonts\malgun.ttf"
# Mac: font_path = "/Library/Fonts/AppleGothic.ttf"
# Linux: font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

# 2) 폰트를 matplotlib에 등록
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지는 경우 방지

ALL_CATEGORIES = ["기쁨", "슬픔", "분노", "불안", "혐오", "사랑", "놀람", "희망"]
category_colors = {
    "기쁨": "#FFD700", "슬픔": "#1E90FF", "분노": "#FF4500", "불안": "#FFA500",
    "혐오": "#8B008B", "사랑": "#FF69B4", "놀람": "#00FA9A", "희망": "#32CD32",
}

datas = {
    "total": {
        "Top_words": [('마음', 21, '슬픔'), ('생각', 17, '슬픔'), ('신', 12, '분노'), ('한', 7, '분노'), ('소원', 4, '기쁨'),
                      ('꿈', 3, '기쁨'), ('설움', 2, '놀람'), ('안심', 2, '불안'), ('편안', 2, '기쁨'), ('동정', 2, '혐오'),
                      ('원망', 2, '분노'), ('호의', 2, '사랑'), ('태평', 2, '분노'), ('탄복', 2, '기쁨'), ('위신', 1, '분노'),
                      ('적막', 1, '놀람'), ('흥', 1, '기쁨'), ('원', 1, '분노'), ('감복', 1, '기쁨'), ('동요', 1, '사랑'),
                      ('위엄', 1, '기쁨'), ('애석', 1, '사랑'), ('죽음', 1, '기쁨'), ('감동', 1, '기쁨'), ('순종', 1, '기쁨'),
                      ('측은', 1, '슬픔'), ('흉악', 1, '분노'), ('애', 1, '사랑')],
        "Category_counts": [('슬픔', 39),
                            ('분노', 26), ('기쁨', 17), ('사랑', 5), ('놀람', 3), ('불안', 2), ('혐오', 2), ('희망', 0)]
        ,
    },
    "1": {
        "Top_words": [('마음', 6, '슬픔'), ('꿈', 2, '기쁨'), ('생각', 2, '슬픔'), ('위신', 1, '분노'), ('적막', 1, '놀람'),
                      ('흥', 1, '기쁨')],
        "Category_counts": [('슬픔', 8), ('기쁨', 3), ('분노', 1), ('놀람', 1), ('불안', 0), ('혐오', 0), ('사랑', 0), ('희망', 0)],
    },
    "2": {
        "Top_words": [('마음', 9, '슬픔'), ('생각', 5, '슬픔'), ('한', 4, '분노'), ('설움', 2, '놀람'), ('소원', 2, '기쁨'),
                      ('원망', 2, '분노'), ('안심', 1, '불안'), ('편안', 1, '기쁨'), ('동정', 1, '혐오')]
        ,
        "Category_counts": [('슬픔', 14), ('분노', 6), ('기쁨', 3), ('놀람', 2), ('불안', 1), ('혐오', 1), ('사랑', 0), ('희망', 0)]
        ,
    },
    "3": {
        "Top_words": [('호의', 1, '사랑'), ('마음', 1, '슬픔'), ('동정', 1, '혐오'), ('원', 1, '분노')]
        ,
        "Category_counts": [('슬픔', 1), ('분노', 1), ('혐오', 1), ('사랑', 1), ('기쁨', 0), ('불안', 0), ('놀람', 0), ('희망', 0)]
        ,
    },
    "4": {
        "Top_words": [('신', 10, '분노'), ('생각', 6, '슬픔'), ('소원', 2, '기쁨'), ('감복', 1, '기쁨'), ('동요', 1, '사랑'),
                      ('위엄', 1, '기쁨'), ('꿈', 1, '기쁨'), ('애석', 1, '사랑'), ('죽음', 1, '기쁨'), ('감동', 1, '기쁨'),
                      ('마음', 1, '슬픔'), ('순종', 1, '기쁨'), ('한', 1, '분노')]
        ,
        "Category_counts": [('분노', 11), ('기쁨', 8), ('슬픔', 7), ('사랑', 2), ('불안', 0), ('혐오', 0), ('놀람', 0), ('희망', 0)]
        ,
    },
    "5": {
        "Top_words": [('마음', 4, '슬픔'), ('생각', 4, '슬픔'), ('한', 2, '분노'), ('신', 2, '분노'), ('태평', 2, '분노'),
                      ('탄복', 2, '기쁨'), ('편안', 1, '기쁨'), ('호의', 1, '사랑'), ('측은', 1, '슬픔'), ('흉악', 1, '분노'),
                      ('애', 1, '사랑'), ('안심', 1, '불안')]
        ,
        "Category_counts": [('슬픔', 9), ('분노', 7), ('기쁨', 3), ('사랑', 2), ('불안', 1), ('혐오', 0), ('놀람', 0), ('희망', 0)]
        ,
    }
}


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

    # 2) 단어별 등장 횟수
    counts = Counter(filtered)

    # 3) 단어→카테고리 매핑
    word_cat = {w: emo_dict[w]['cat'] for w in counts}

    # 4) Top N 단어와 카테고리 함께 묶기
    most_common = counts.most_common(top_n)
    top_words = [(w, cnt, word_cat[w]) for w, cnt in most_common]

    # 5) 카테고리별 등장 횟수 집계
    raw_cat_counts = Counter(word_cat[w] for w in filtered)
    # 없는 카테고리는 0으로 채우기
    full_cat_counts = [(cat, raw_cat_counts.get(cat, 0)) for cat in ALL_CATEGORIES]
    # 등장 횟수 기준 내림차순 정렬 (0인 것들은 뒤에서 ALL_CATEGORIES 순으로)
    cat_counts_list = sorted(full_cat_counts, key=lambda x: x[1], reverse=True)

    return top_words, cat_counts_list


def pie_charts(top_words, cat_counts):
    # 1) Top words 빈도 파이차트 (labels 숨기고 legend 사용)
    labels = [w for w, cnt, cat in top_words]
    sizes = [cnt for w, cnt, cat in top_words]
    fig1, ax1 = plt.subplots()
    wedges1, texts1, autotexts1 = ax1.pie(
        sizes,
        labels=None,  # 조각 위 라벨 숨기기
        autopct='%1.1f%%',
        startangle=90
    )
    ax1.legend(
        wedges1,
        labels,
        title="Top Words",
        loc="upper right",
        bbox_to_anchor=(1.3, 1),
        fontsize='small',
        frameon=False
    )
    ax1.set_title('Top Words')
    plt.tight_layout()
    plt.show()

    # 2) Category counts 파이차트 (labels 숨기고 legend 사용)
    cat_labels = [cat for cat, cnt in cat_counts]
    cat_sizes = [cnt for cat, cnt in cat_counts]
    colors = [category_colors.get(cat, "#CCCCCC") for cat in cat_labels]
    fig2, ax2 = plt.subplots()
    wedges2, texts2, autotexts2 = ax2.pie(
        cat_sizes,
        labels=None,  # 조각 위 라벨 숨기기
        autopct='%1.1f%%',
        colors=colors,
        startangle=90
    )
    ax2.legend(
        wedges2,
        cat_labels,
        title="Categories",
        loc="upper right",
        bbox_to_anchor=(1.3, 1),
        fontsize='medium',
        frameon=False
    )
    ax2.set_title('Category Counts')
    plt.tight_layout()
    plt.show()

def line_graph():
    datas = {
        "1": {
            "Category_counts": [('슬픔', 8), ('기쁨', 3), ('분노', 1), ('놀람', 1), ('불안', 0), ('혐오', 0), ('사랑', 0), ('희망', 0)],
        },
        "2": {
            "Category_counts": [('슬픔', 14), ('분노', 6), ('기쁨', 3), ('놀람', 2), ('불안', 1), ('혐오', 1), ('사랑', 0),
                                ('희망', 0)],
        },
        "3": {
            "Category_counts": [('슬픔', 1), ('분노', 1), ('혐오', 1), ('사랑', 1), ('기쁨', 0), ('불안', 0), ('놀람', 0), ('희망', 0)],
        },
        "4": {
            "Category_counts": [('분노', 11), ('기쁨', 8), ('슬픔', 7), ('사랑', 2), ('불안', 0), ('혐오', 0), ('놀람', 0),
                                ('희망', 0)],
        },
        "5": {
            "Category_counts": [('슬픔', 9), ('분노', 7), ('기쁨', 3), ('사랑', 2), ('불안', 1), ('혐오', 0), ('놀람', 0), ('희망', 0)],
        }
    }

    # Define parts and categories
    parts = ["1", "2", "3", "4", "5"]

    # Compute proportions for each category across parts
    proportions = {cat: [] for cat in ALL_CATEGORIES}
    for part in parts:
        counts_dict = dict(datas[part]["Category_counts"])
        total = sum(counts_dict.values()) or 1
        for cat in ALL_CATEGORIES:
            proportions[cat].append(counts_dict.get(cat, 0) / total)

    # Plot line chart with specified colors
    plt.figure()
    x = list(map(int, parts))
    for cat in ALL_CATEGORIES:
        vals = proportions[cat]
        plt.plot(x, vals, marker='o', label=cat, color=category_colors.get(cat))

    plt.xticks(x)
    plt.xlabel("단계")
    plt.ylabel("비율")
    plt.title("내러티브 아크 단계별 감정 변화")
    plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

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
    print(f"\nTop_words\n{top_words}")
    for word, count, cat in top_words:
        print(f"{word}: {count} ({cat})")

    # ◼ Category counts
    print(f"\nCategory_counts\n{cat_counts}")
    for cat, count in cat_counts:
        print(f"{cat}: {count}")

    # pie_charts(top_words, cat_counts)
    line_graph()
