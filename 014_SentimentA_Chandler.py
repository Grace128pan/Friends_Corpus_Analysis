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

# Load lines for Chandler from the file
chandler_lines_path = r'C:\Users\grace\Desktop\Analysis\Character_Lines\Chandler_lines.txt'

with open(chandler_lines_path, 'r', encoding='utf-8') as file:
    chandler_lines = file.readlines()

# Perform sentiment analysis on Chandler's lines
chandler_sentiment_scores = analyze_sentiment(chandler_lines)

# Create a DataFrame for visualization and analysis
df_chandler_sentiment = pd.DataFrame({'Sentiment Score': chandler_sentiment_scores})

# Visualize the sentiment scores
plt.figure(figsize=(10, 6))
plt.plot(df_chandler_sentiment.index, df_chandler_sentiment['Sentiment Score'], marker='o', linestyle='-', color='b')
plt.title('Sentiment Analysis of Chandler\'s Lines')
plt.xlabel('Line Number')
plt.ylabel('Sentiment Score')
plt.grid(True)
plt.savefig(r'C:\Users\grace\Desktop\Analysis\Chandler_Sentiment_Analysis.png')
plt.show()

# Save the sentiment scores to a CSV file
output_csv_path = r'C:\Users\grace\Desktop\Analysis\Chandler_Sentiment_Scores.csv'
df_chandler_sentiment.to_csv(output_csv_path, index=False)

print(f'Sentiment scores for Chandler saved to {output_csv_path}')
