import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

# Download NLTK resources if not already downloaded
nltk.download('vader_lexicon')


# Function to perform sentiment analysis on a list of lines
def analyze_sentiment(lines):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = [sid.polarity_scores(line)['compound'] for line in lines]
    return sentiment_scores


# Load lines for each character
characters = ['Rachel', 'Monica', 'Phoebe', 'Ross']
lines_paths = {
    'Rachel': r'C:\Users\grace\Desktop\Analysis\Character_Lines\Rachel_lines.txt',
    'Monica': r'C:\Users\grace\Desktop\Analysis\Character_Lines\Monica_lines.txt',
    'Phoebe': r'C:\Users\grace\Desktop\Analysis\Character_Lines\Phoebe_lines.txt',
    'Ross': r'C:\Users\grace\Desktop\Analysis\Character_Lines\Ross_lines.txt'
}

sentiment_data = {}

for character, path in lines_paths.items():
    with open(path, 'r', encoding='utf-8') as file:
        character_lines = file.readlines()

    sentiment_scores = analyze_sentiment(character_lines)
    sentiment_data[character] = sentiment_scores

    # Create a DataFrame for visualization and analysis
    df_character_sentiment = pd.DataFrame({'Sentiment Score': sentiment_scores})

    # Visualize the sentiment scores
    plt.figure(figsize=(10, 6))
    plt.plot(df_character_sentiment.index, df_character_sentiment['Sentiment Score'], marker='o', linestyle='-',
             color='b')
    plt.title(f'Sentiment Analysis of {character}\'s Lines')
    plt.xlabel('Line Number')
    plt.ylabel('Sentiment Score')
    plt.grid(True)
    plt.savefig(f'C:\\Users\\grace\\Desktop\\Analysis\\{character}_Sentiment_Analysis.png')
    plt.show()

# Save the sentiment scores to CSV files
for character, scores in sentiment_data.items():
    df_character_sentiment = pd.DataFrame({'Sentiment Score': scores})
    output_csv_path = f'C:\\Users\\grace\\Desktop\\Analysis\\{character}_Sentiment_Scores.csv'
    df_character_sentiment.to_csv(output_csv_path, index=False)
    print(f'Sentiment scores for {character} saved to {output_csv_path}')
