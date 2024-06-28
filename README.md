# NLP and Sentiment Analysis Project

This project performs NLP and sentiment analysis on customer chat data. The project involves preprocessing text data, performing sentiment analysis, and visualizing the results to gain insights into customer sentiments.

## Project Structure
- `data/`: Contains the customer chat data.
- `scripts/`: Python scripts for data preprocessing, sentiment analysis, and visualization.
- `outputs/`: Directory to save output files like plots and reports.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Provides an overview of the project and setup instructions.

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
2. Install the required packages:

   ```bash

    pip install -r requirements.txt

## Usage

1. Place the customer chat data file (e.g., `customer_chat_data.csv`) in the `data/` directory.

2. Run the data preprocessing script to clean and preprocess the data:
   ```bash
   python scripts/data_preprocessing.py

This will generate a cleaned data file (cleaned_chat_data.csv) in the data/ directory.

3. Perform sentiment analysis on the cleaned data:

   ```bash
   python scripts/sentiment_analysis.py

This will generate a sentiment analysis data file (sentiment_chat_data.csv) in the data/ directory.

4. Visualize the sentiment analysis results:

   ```bash
    python scripts/visualization.py

 This will generate output plots (e.g., sentiment_distribution.png and sentiment_score_distribution.png) in the outputs/ directory.

