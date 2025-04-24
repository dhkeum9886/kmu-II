
# 1. Install required packages
# !pip install -U pip
# !pip install -U transformers datasets scikit-learn
# python 2genLargeEmoLexicon-file.py


from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import torch

# Load model and tokenizer
model_path = "./kcbert-emotion"  # <-- update this path as needed
# model_path = "./emotion_model"  # <-- update this path as needed
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)
model.eval()

# Define emotion labels
labels = ["기쁨", "슬픔", "분노", "불안", "혐오", "사랑", "놀람", "희망"]

# Emotion classification function
def classify_emotion(word):
    inputs = tokenizer(word, return_tensors="pt", truncation=True, max_length=16)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1).numpy()[0]
    top = probs.argmax()
    return labels[top], round(probs[top], 3)

# Input/output file paths
input_file = "465emoNouns-wordOnly.txt"       # UTF-8 encoded file, one word per line
output_file = "emo_words_output.txt"     # Output will also be UTF-8 encoded

# Read, classify, and write results
with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    # fout.write("단어\t감정\t신뢰도\n")
    for line in fin:
        word = line.strip()
        if word:
            emotion, confidence = classify_emotion(word)
            fout.write(f"{word}\t{emotion}\t{confidence}\n")

print(f"✅ 분류 완료! 결과가 '{output_file}'에 저장되었습니다.")
