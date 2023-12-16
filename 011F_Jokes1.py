import os
import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

nltk.download('vader_lexicon')


def is_potential_joke(sentence):
    # Define keywords that may indicate a joke
    joke_keywords = ['laugh', 'funny', 'haha', 'joke', 'humor', "hilarious", "amusing", "chuckle", "comical"]

    # Tokenize and check for the presence of joke-related keywords
    tokens = nltk.word_tokenize(sentence.lower())
    return any(keyword in tokens for keyword in joke_keywords)


def extract_jokes(script_path):
    jokes = []
    sia = SentimentIntensityAnalyzer()

    with open(script_path, 'r', encoding='utf-8') as file:
        script = file.read()

    sentences = sent_tokenize(script)

    for i, sentence in enumerate(sentences):
        # Check if the sentence contains potential joke keywords
        if is_potential_joke(sentence):
            sentiment_score = sia.polarity_scores(sentence)['compound']

            # Assume a sentence is a joke if it has positive sentiment
            if sentiment_score > 0:
                jokes.append({
                    'Character': 'Unknown',  # In this basic example, we don't identify characters
                    'Line': sentence,
                    'JokeNumber': len(jokes) + 1
                })

    return jokes


def save_to_csv(jokes, output_path):
    df = pd.DataFrame(jokes)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    script_path = "C:/Users/grace/Desktop/Analysis/season1_friends.txt"
    output_csv_path = "C:/Users/grace/Desktop/Analysis/jokes_output.csv"

    jokes_data = extract_jokes(script_path)
    save_to_csv(jokes_data, output_csv_path)
