import sys
from konlp.kma.klt2023 import klt2023
from konlpy.tag import Okt
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from kiwipiepy import Kiwi
import os

# 1) 사용할 한글 폰트 파일 경로 지정 (Windows 예시: 맑은고딕)
font_path = r"C:\Windows\Fonts\malgun.ttf"
# Mac: font_path = "/Library/Fonts/AppleGothic.ttf"
# Linux: font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

# 2) 폰트를 matplotlib에 등록
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지는 경우 방지

# exclude_list = ['마음', '생각', '꿈', '한', '원', '열', '소원', '신', '불']
exclude_list = []

ALL_CATEGORIES = ["기쁨", "슬픔", "분노", "불안", "혐오", "사랑", "놀람", "희망"]
category_colors = {
    "기쁨": "#FFD700", "슬픔": "#1E90FF", "분노": "#FF4500", "불안": "#FFA500",
    "혐오": "#8B008B", "사랑": "#FF69B4", "놀람": "#00FA9A", "희망": "#32CD32",
}

kiwi = Kiwi()

# 텍스트를 형태소 분석하여 결과를 반환하는 함수
def analyze_text(text):
    result = kiwi.analyze(text)
    return result

# 형태소 분석 결과에서 명사를 추출하는 함수
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
        print(extract_nouns(line))
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    # input file
    lines = read()
    text_mining(lines)
