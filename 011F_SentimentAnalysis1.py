import nltk

# Download the vader_lexicon resource
nltk.download('vader_lexicon')
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download the vader_lexicon resource
nltk.download('vader_lexicon')

# Set the path to your text file
file_path = "C:/Users/grace/Desktop/Analysis/S1_Rachel/rachel_lines_season1.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Initialize SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Analyze sentiment for each sentence
    sentiment_scores = [sia.polarity_scores(sentence)['compound'] for sentence in sentences]

    # Plot the sentiment distribution
    plt.figure(figsize=(10, 6))
    plt.hist(sentiment_scores, bins=20, edgecolor='black')
    plt.title("Sentiment Distribution of Rachel's Lines in Season 1")
    plt.xlabel("Compound Sentiment Score")
    plt.ylabel("Number of Sentences")
    plt.grid(axis='y', alpha=0.75)
    plt.show()

