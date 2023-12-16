from wordcloud import WordCloud
import matplotlib.pyplot as plt

# File path for Rachel's lines in season 1
file_path = "C:/Users/grace/Desktop/Analysis/S1_Rachel/rachel_lines_season1.txt"

# Read Rachel's lines from the file
with open(file_path, 'r', encoding='utf-8') as file:
    rachel_lines = file.read()

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(rachel_lines)

# Plot the WordCloud image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Rachel\'s Lines in Season 1')
plt.show()
