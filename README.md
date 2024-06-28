# NLP and Sentiment Analysis Project

This project performs NLP and sentiment analysis on customer chat data.

## Project Structure
- `data/`: Contains the customer chat data.
- `scripts/`: Python scripts for data preprocessing, sentiment analysis, and visualization.
- `notebooks/`: Jupyter notebook for interactive analysis.
- `models/`: Directory to save trained models.
- `outputs/`: Directory to save output files like plots and reports.

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/nlp_sentiment_analysis.ipynb
   ```

## Usage
1. Place the customer chat data in the `data/` directory.
2. Run the scripts for preprocessing, analysis, and visualization.

## Scripts
- `data_preprocessing.py`: Script for data cleaning and preprocessing.
- `sentiment_analysis.py`: Script for performing sentiment analysis.
- `visualization.py`: Script for visualizing the analysis results.
