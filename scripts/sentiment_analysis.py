import os
import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    if not isinstance(text, str):
        return 0.0  # or any default value you prefer for non-string entries
    blob = TextBlob(text)
    return blob.sentiment.polarity

def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def perform_sentiment_analysis(file_path):
    data = pd.read_csv(file_path)
    data['sentiment'] = data['filtered_text'].apply(get_sentiment)
    data['sentiment_label'] = data['sentiment'].apply(classify_sentiment)
    return data

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file = os.path.join(base_dir, 'data', 'cleaned_chat_data.csv')
    output_file = os.path.join(base_dir, 'data', 'sentiment_chat_data.csv')
    
    data = perform_sentiment_analysis(input_file)
    data.to_csv(output_file, index=False)
    print(f"Sentiment analysis completed and saved to '{output_file}'")

