import ast
import json
import csv
import re
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForMaskedLM

with open("data/News_sentiment_CRO_1.json-final.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
tokenizer = AutoTokenizer.from_pretrained("classla/xlm-r-bertic")
def clean_and_tokenize(text):
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt", max_length=4)

    return tokens

text = []
label = []

# Process each document
for doc in data['documents']:
    print(doc['id'])
    sentiment_label = None
    for sentiment in doc['General sentiment']:
        if len(sentiment) == 3:
            if sentiment[0] == 'induced_final':
                sentiment_label = sentiment[1]
                text.append(clean_and_tokenize(doc['headline']))
                label.append(clean_and_tokenize(sentiment_label))
print()
model = AutoModelForMaskedLM.from_pretrained("classla/xlm-r-bertic")
model.eval()
device = torch.device('cpu' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Perform inference
with torch.no_grad():
    outputs = model(**text[0])

# Get predictions
logits = outputs.logits
predictions = torch.argmax(logits, dim=-1).cpu().numpy()

# Print or return the predictions alongside the actual labels
for i, (pred, lbl) in enumerate(zip(predictions, label)):
    print(f"Text: {text[i]}")
    print(f"Predicted Sentiment: {pred}")
    print(f"Actual Sentiment: {lbl}")
    print("---")