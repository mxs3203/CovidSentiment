import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from transformers import AutoTokenizer
import json
import seaborn as sb
import matplotlib.pyplot as plt

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("classla/xlm-r-bertic")
df = pd.read_csv('bertic_finetune_dataset.csv', skiprows=1)

for row in df.iterrows():
    sentance = row[1]
    encoded_input = tokenizer(sentance, truncation=True, padding=True, max_length=512, return_tensors='pt')
    print(encoded_input['input_ids'])

