# Train_Korean_Emotion_Classifier.ipynb (for Google Colab)

# 1. Install required packages
# !pip install -U pip
# !pip install -U transformers datasets scikit-learn pandas

# 2. Load Libraries
import pandas as pd
from datasets import Dataset
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
import torch

# 3. Load and Prepare Data (adjust path or upload CSV to Colab)
data = pd.read_csv("[2]590_emotional_nouns_categorized-sort.txt", sep="\t")  # Requires
label_list = ['기쁨', '슬픔', '분노', '불안', '혐오', '사랑', '놀람', '희망']
label2id = {label: i for i, label in enumerate(label_list)}
id2label = {i: label for label, i in label2id.items()}
data['labels'] = data['label'].map(label2id)  # This is the correct column for HuggingFace

# 3.2 매핑되지 않은(=NaN) 행 제거
before = len(data)
data = data.dropna(subset=['labels'])
after  = len(data)
print(f">>> dropped {before-after} rows with unmapped labels.")

# 3.3 정수형으로 안전하게 캐스팅
data['labels'] = data['labels'].astype('int64')

# 4. Train-Test Split
df_train, df_val = train_test_split(data, test_size=0.1, random_state=42)
train_dataset = Dataset.from_pandas(df_train[['word', 'labels']])
val_dataset = Dataset.from_pandas(df_val[['word', 'labels']])

# 5. Tokenizer and Model
model_name = "beomi/kcbert-base"
tokenizer = BertTokenizerFast.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(label_list))
model.config.problem_type = "single_label_classification"

def tokenize(batch):
    return tokenizer(batch['word'], padding=True, truncation=True, max_length=16)

train_dataset = train_dataset.map(tokenize, batched=True)
val_dataset = val_dataset.map(tokenize, batched=True)
train_dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'], output_all_columns=True)
val_dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'], output_all_columns=True)

# 6. Training
training_args = TrainingArguments(
    output_dir="./emotion_model_dict_based",
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=4,
    save_steps=500,
    logging_dir="./logs",
)

def compute_metrics(eval_pred):
    from sklearn.metrics import accuracy_score
    logits, labels = eval_pred
    preds = torch.argmax(torch.tensor(logits), dim=1)
    return {"accuracy": accuracy_score(labels, preds)}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics
)

trainer.train()

# 7. Save Model
model.save_pretrained("kcbert-emotion")
tokenizer.save_pretrained("kcbert-emotion")
