import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    if not isinstance(text, str):
        text = ''
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

def tokenize_and_remove_stopwords(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data['cleaned_text'] = data['Text'].apply(clean_text)
    data['filtered_text'] = data['cleaned_text'].apply(tokenize_and_remove_stopwords)
    return data

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file = os.path.join(base_dir, 'data', 'customer_chat_data.csv')
    output_file = os.path.join(base_dir, 'data', 'cleaned_chat_data.csv')
    
    data = preprocess_data(input_file)
    data.to_csv(output_file, index=False)
    print(f"Data preprocessing completed and saved to '{output_file}'")

