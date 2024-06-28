import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sentiment(file_path):
    data = pd.read_csv(file_path)
    
    plt.figure(figsize=(10, 6))
    sns.countplot(x='sentiment_label', data=data)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, 'sentiment_distribution.png'))
    plt.show()
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data['sentiment'], bins=30, kde=True)
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, 'sentiment_score_distribution.png'))
    plt.show()

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file = os.path.join(base_dir, 'data', 'sentiment_chat_data.csv')
    output_dir = os.path.join(base_dir, 'outputs')
    
    visualize_sentiment(input_file)
    print(f"Visualizations saved in '{output_dir}'")

