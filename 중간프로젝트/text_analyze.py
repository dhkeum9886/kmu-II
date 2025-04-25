import sys
from kiwipiepy import Kiwi
from collections import Counter, defaultdict
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

font_path = r"C:\Windows\Fonts\malgun.ttf"

font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지는 경우 방지

exclude_list = []

ALL_CATEGORIES = ["기쁨", "슬픔", "분노", "불안", "혐오", "사랑", "놀람", "희망"]
category_colors = {
    "기쁨": "#FFD700", "슬픔": "#1E90FF", "분노": "#FF4500", "불안": "#FFA500",
    "혐오": "#8B008B", "사랑": "#FF69B4", "놀람": "#00FA9A", "희망": "#32CD32",
}

datas = {
    "total": {
        "Top_words": [('자기', 10, '사랑'), ('마음', 7, '슬픔'), ('재미', 3, '슬픔'), ('불행', 3, '기쁨'), ('원망', 2, '분노'),
                      ('생각', 2, '슬픔'), ('요행', 2, '놀람'), ('불길', 1, '분노'), ('안심', 1, '불안'), ('가락', 1, '희망')]
        ,
        "Category_counts": [('슬픔', 12), ('사랑', 10), ('기쁨', 3), ('분노', 3), ('놀람', 2), ('불안', 1), ('희망', 1), ('혐오', 0)]

        ,
    },
    "1": {
        "Words": ['새침', '이날', '소문', '인력거', '노릇', '첨지', '오래간만', '운수', '문안', '거기', '앞집', '마나님', '전찻길', '정류장', '사람', '하나',
                  '하나', '눈결', '교원', '양복', '동광학교', '삼십', '둘째', '오십', '아침', '댓바람', '수가', '열흘', '동안', '구경', '첨지', '통화',
                  '다섯', '손바닥', '눈물', '만큼', '이날', '이때', '팔십', '유용', '모주', '아내', '설렁탕', '그릇', '아내', '기침', '달포', '조밥', '형',
                  '재미', '자기', '신조', '어디', '충실', '의사', '중증', '중증', '열흘', '때문', '그때', '첨지', '오래간만', '좁쌀', '나무', '첨지',
                  '의지', '오라', '천방지축', '남비', '마음', '불길', '오라', '숟가락', '주먹', '덩이', '누구', '듯이', '저녁', '가슴', '지랄', '그때',
                  '첨지', '오라', '첨지', '이슬', '첨지', '눈시울', '환자', '사흘', '설렁탕', '국물', '남편', '오라', '조밥', '설렁탕', '지랄', '야단',
                  '마음', '설렁탕', '어미', '개똥이', '먹이', '팔십', '첨지', '마음', '행운', '그거', '빗물', '목덜미', '기름', '주머니', '수건', '학교',
                  '인력거', '소리',
                  '자기', '사람', '학교', '학생', '첨지', '짐작', '학생', '남대문', '정거장', '얼마', '학교', '기숙사', '동기', '방학', '이용', '귀향',
                  '작정', '첨지', '구두', '고구라', '양복', '망정', '노박', '첨지', '남대문', '정거장', '말씀', '첨지', '주저', '우중', '우장', '둘째',
                  '만족', '이상', '꼬리', '행운', '아내', '부탁', '마음', '앞집', '마나님', '병인', '얼굴', '유일', '생물', '움폭', '애걸', '오늘', '덕분',
                  '모기', '소리', '걸그렁걸그렁', '그때', '첨지', '대수', '듯이', '압다', '소리', '누구', '환자', '듯이', '소리', '정거장', '순간', '경련',
                  '아내', '얼굴', '첨지', '눈앞', '남대문', '정거장', '얼마', '학생', '초조', '인력거', '얼굴', '혼잣말', '인천', '다음', '오십', '사이',
                  '첨지', '액수', '금액', '얼마', '용기', '병자', '염려', '오늘', '행운', '갑절', '행운', '오십', '학생', '고개', '여기', '거기', '사오리',
                  '차부', '얼굴', '기쁨', '대로'],

        "Top_words": [('마음', 4, '슬픔'), ('자기', 2, '사랑'), ('재미', 1, '슬픔'), ('불길', 1, '분노')]
        ,
        "Category_counts": [('슬픔', 5), ('사랑', 2), ('분노', 1), ('기쁨', 0), ('불안', 0), ('혐오', 0), ('놀람', 0), ('희망', 0)]
        ,
    },
    "2": {
        "Words": ['학생', '첨지', '다리', '이상', '달음', '바퀴', '얼음', '스케이트', '모양', '다리', '자기', '까닭', '염려', '가슴', '오늘', '병자',
                  '원망', '듯이', '자기', '개똥이', '곡성', '소리', '기차', '초조', '첨지', '인력거', '복판', '첨지', '달음', '첨지', '걸음', '시작',
                  '다리', '자기', '머리', '근심', '걱정', '듯이', '정거장', '오십', '생각', '듯이', '졸부', '듯이', '자식', '허리', '인력거', '우중',
                  '노동', '창자', '한기', '오십', '정거장', '발길', '하나', '온몸', '당장', '자리', '인력거', '할미', '상판', '누구', '반항', '듯이',
                  '즈음', '머리', '광명',
                  '그것', '근처', '생각', '운수', '괴상', '요행', '누구', '보증', '꼬리', '행운', '자기', '내기', '믿음', '정거장', '인력거', '등쌀',
                  '정거장', '이전', '정거장', '전차', '정류장', '사람', '전찻길', '인력거', '자기', '근처', '형세', '관망', '얼마', '기차', '수십', '정류류',
                  '물색', '첨지', '머리', '뒤축', '구두', '망토', '기생', '퇴물', '난봉', '여학생', '여편네', '모양', '슬근슬근', '여자', '아씨', '인력거',
                  '타시랍시', '여학생', '한참', '입술', '첨지', '첨지', '구걸', '무엇', '기색', '아씨', '정거장', '어디', '추근', '여자', '일본식', '버들',
                  '고리짝', '소리', '벽력', '첨지', '어랍시', '전차', '첨지', '원망', '전차', '예감', '전차', '사람', '시작', '하나', '가방', '차장장',
                  '눈치', '첨지', '인력거', '한동안', '승강이', '육십', '인사동', '인력거', '이상', '인력거', '이번', '마음', '초조', '광경', '눈앞', '요행',
                  '여유', '나무', '등걸', '무엇', '다리', '저놈', '인력거', '사람', '걱정', '걸음', '하늘', '황혼', '창경원', '걸음', '걸음', '걸음',
                  '가까', '마음', '괴상', '누그러웠', '안심', '자기', '불행', '박두', '마음', '불행', '시간', '얼마쯤', '기적', '벌이', '기쁨', '사면',
                  '모양', '자기', '불행', '다리', '누구', '즈음', '길가', '선술집', '친구', '치삼이', '얼굴', '주홍', '구레나룻', '얼굴', '여기저기', '고랑',
                  '수염', '턱밑', '솔잎', '송이', '첨지', '풍채', '대상', '첨지', '자네', '모양', '뚱뚱보', '말라깽이', '목소리', '몸짓', '딴판', '첨지',
                  '친구', '자기', '은인', '무엇', '자네', '모양', '자네', '재미', '첨지', '얼굴', '재미', '자네', '물독', '새앙쥐', '선술집', '추어탕',
                  '뚜껑', '석쇠', '뻐지짓뻐지짓', '너비아니', '제육', '콩팥', '북어', '빈대떡', '안주', '탁자', '첨지', '거기', '먹이', '위선', '분량',
                  '빈대떡', '추어탕', '그릇', '창자', '음식', '순식간', '두부', '미꾸리', '그릇', '세째', '그릇', '걸이', '곱배기', '창자', '얼굴', '곱배기',
                  '첨지', '개개', '시작', '석쇠', '곱배기', '의아', '듯이', '첨지', '우리', '사십', '주의', '사십', '운수', '얼마', '삼십', '삼십', '상관',
                  '오늘', '산더미', '사람', '이놈', '이거', '치삼', '다섯', '대가리', '이놈', '야단', '대가리', '문의', '듯이', '주정', '눈치', '에미',
                  '오라', '이놈', '허리춤', '훔칫훔칫', '대가리', '사품', '은전', '그랑', '일변', '첨지', '거처', '듯이', '불시', '듯이', '고개', '다리',
                  '뼉다구', '치삼', '원수', '육시', '양푼', '듯이', '곱배기', '겨를', '첨지', '입술', '수염', '만족', '듯이', '솔잎', '송이', '수염',
                  '첨지', '어깨', '웃음', '소리', '술집', '첨지', '이야기', '하나', '정거장', '오기', '전차', '정류장', '어름', '어름', '하나', '궁리',
                  '거기', '마나님', '여학생', '요새', '어디', '논다니', '아가씨', '구별', '망토', '슬근슬근', '인력거', '타시랍시요', '손가방', '소리', '꾀꼬리',
                  '소리', '첨지', '꾀꼬리', '소리', '사람', '일시', '깍쟁이', '누구', '소리', '처신', '웃음', '소리', '웃음', '소리', '첨지', '시작',
                  '주정뱅', '지랄', '첨지', '우리', '마누라', '마누라', '이놈', '언제', '오늘', '엑기', '거짓말', '거짓말', '마누라', '시체', '뻐들', '첨지',
                  '소리', '얼굴', '사람', '참말', '거짓말', '가세', '첨지', '눈물', '누구', '득의', '양양', '오라', '어린애', '모양', '손뼉', '사람',
                  '치삼이', '불안', '듯이', '첨지', '첨지', '확신', '소리', '소리', '가락', '어치', '곱배기', '첨지', '취중', '설렁탕', '셋집', '전체',
                  '행랑', '만일', '첨지', '주기', '대문', '그곳', '지배', '정적', '폭풍우', '바다', '정적', '다리']
        ,
        "Top_words": [('자기', 8, '사랑'), ('마음', 3, '슬픔'), ('불행', 3, '기쁨'), ('원망', 2, '분노'), ('생각', 2, '슬픔'),
                      ('요행', 2, '놀람'), ('재미', 2, '슬픔'), ('안심', 1, '불안'), ('가락', 1, '희망')]

        ,
        "Category_counts": [('사랑', 8), ('슬픔', 7), ('기쁨', 3), ('분노', 2), ('놀람', 2), ('불안', 1), ('희망', 1), ('혐오', 0)]

        ,
    },
    "3": {
        "Words": ['기침', '소리', '그르렁거리', '숨소리', '무덤', '침묵', '침묵', '소리', '어린애', '소리', '청각', '소리', '따름', '소리', '짐작', '첨지',
                  '침묵', '짐작', '대문', '난장', '남편', '오라', '고함', '고함', '엄습', '허장성세', '까닭', '첨지', '방문', '구역', '추기', '삿자리',
                  '먼지', '기저귀', '오줌', '가지각색', '케케히', '병인', '추기', '첨지', '설렁탕', '한구석', '사이', '주정', '목청', '대로', '호통', '오라',
                  '주야', '장천', '누워', '남편', '소리', '발길', '다리', '발길', '사람', '나무', '등걸', '느낌', '이때', '소리', '소리', '개똥이', '얼굴',
                  '표정', '소리', '뱃속', '기운', '차도', '보람', '남편', '아내', '머리맡', '까치집', '환자', '머리', '오라', '이것', '이년', '대답',
                  '눈깔', '눈깔', '천정', '사람', '눈물', '얼굴', '어룽어룽', '첨지', '듯이', '얼굴', '얼굴', '설렁탕', '오늘', '운수'],

        "Top_words": []

        ,
        "Category_counts": []

        ,
    }
}

kiwi = Kiwi()


def analyze_text(text):
    result = kiwi.analyze(text)
    return result


def extract_nouns(text):
    nouns = []
    result = analyze_text(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and (pos.startswith('N') or pos.startswith('SL')):
            nouns.append(token)
    return nouns


def text_mining(lines):
    result = []
    for line in lines:
        result.extend(extract_nouns(line))
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


def init_dict():
    def dict_file(filename):
        emo_dict = {}
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, start=1):
                    if len(line.strip()) > 0:
                        # lines.append(line.strip())
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
    filtered = [
        w for w in word_list
        if w in emo_dict
           and w not in exclude_list
        # and len(w) > 1
    ]

    # 2) 단어별 등장 횟수
    counts = Counter(filtered)

    # 3) 단어→카테고리, 단어→신뢰도 매핑
    word_cat = {w: emo_dict[w]['cat'] for w in counts}
    word_conf = {w: float(emo_dict[w]['con']) for w in counts}

    # 4) Top N 단어 (count 기준)
    most_common = counts.most_common(top_n)
    top_words = [(w, cnt, word_cat[w]) for w, cnt in most_common]

    # 5) 카테고리별 누적 등장 횟수 (기존)
    cat_count = Counter(word_cat[w] for w in filtered)
    cat_counts_list = sorted(
        [(cat, cat_count.get(cat, 0)) for cat in ALL_CATEGORIES],
        key=lambda x: x[1], reverse=True
    )

    # 6) 카테고리별 누적 신뢰도 합계 (new)
    cat_conf = defaultdict(float)
    for w, cnt in counts.items():
        cat = word_cat[w]
        # word_conf[w]은 단어당 1회 신뢰도, 곱하기 cnt 회수
        cat_conf[cat] += word_conf[w] * cnt

    cat_confs_list = sorted(
        [(cat, cat_conf.get(cat, 0.0)) for cat in ALL_CATEGORIES],
        key=lambda x: x[1], reverse=True
    )

    return top_words, cat_counts_list, cat_confs_list


def pie_charts(top_words, cat_counts):
    # ---------- NEW : 0-division 방지 ----------
    if sum(cnt for _, cnt in cat_counts) == 0:
        print("※ 시각화 생략: 해당 구간에서 사전에 매핑된 감정 단어가 없습니다.")
        return
    # -------------------------------------------
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
    parts = ["1", "2", "3"]

    # 카테고리별 백분율(%)
    proportions = {cat: [] for cat in ALL_CATEGORIES}
    for part in parts:
        counts_dict = dict(datas[part]["Category_counts"])
        total = sum(counts_dict.values()) or 1
        for cat in ALL_CATEGORIES:
            # ▼ 비율(0~1) 대신 백분율(0~100)
            proportions[cat].append( counts_dict.get(cat, 0) / total * 100 )

    plt.figure()
    x = list(map(int, parts))
    for cat in ALL_CATEGORIES:
        plt.plot(x, proportions[cat], marker='o',
                 label=cat, color=category_colors.get(cat))

    plt.xticks(x)
    plt.ylim(0, 100)
    plt.xlabel("단계")
    plt.ylabel("백분율(%)")
    plt.title("서사 구조 단계별 감정 변화")
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
    print(word_list)

    # emo file
    emo_dict = init_dict()
    # print('----------')
    # print(emo_dict)
    # word_list = ['황송스럽다', '황송스럽다', '훼손하다']

    top_words, cat_counts, cat_confs = analyze_emotions(word_list, emo_dict)

    # ◼ Top words by frequency (단어, count, 카테고리)
    print(f"\nTop_words\n{top_words}")
    for word, count, cat in top_words:
        print(f"{word}: {count} ({cat})")

    # ◼ Category conf
    print(f"\nCategory_confs\n{cat_confs}")
    for cat, total_conf in cat_confs:
        print(f"{cat}: {total_conf:.3f}")

    # ◼ Category counts
    print(f"\nCategory_counts\n{cat_counts}")
    for cat, total_cnt in cat_counts:
        print(f"{cat}: {total_cnt:.3f}")

    # pie_charts(top_words, cat_counts)
    line_graph()
