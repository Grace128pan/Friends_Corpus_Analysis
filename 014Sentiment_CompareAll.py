import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment import SentimentIntensityAnalyzer

# Set the paths to the text files
file_paths = [
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt",
]

# Load the lines into a DataFrame
data = {'Character': [], 'Lines': []}
for path in file_paths:
    character_name = os.path.splitext(os.path.basename(path))[0].split('_')[0]  # Extract character name correctly
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        data['Character'].extend([character_name] * len(lines))
        data['Lines'].extend(lines)

df = pd.DataFrame(data)

# Perform sentiment analysis on each sentence
sia = SentimentIntensityAnalyzer()
df['Sentiment'] = df['Lines'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Calculate average sentiment scores for each character
average_sentiments = df.groupby('Character')['Sentiment'].mean().reset_index()

# Set the color palette for characters
colors = {'Chandler': 'red', 'Ross': 'orange', 'Joey': 'blue', 'Monica': 'green', 'Phoebe': 'gray', 'Rachel': 'black'}
average_sentiments['Color'] = average_sentiments['Character'].map(colors)

# Plot the bar chart for average sentiment scores
plt.figure(figsize=(10, 6))
sns.barplot(x='Character', y='Sentiment', data=average_sentiments, palette=colors)

plt.title('Average Sentiment Scores for Each Character')
plt.xlabel('Character')
plt.ylabel('Average Sentiment Score')

# Show the plot
plt.show()


