# 1. word frequencies for whole season1
import os
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# Download NLTK resources if not already downloaded
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# File path
file_path = r'C:\Users\grace\Desktop\Analysis\season1_friends.txt'
output_path = r'C:\Users\grace\Desktop\Analysis\word_frequency_plot.png'

# Stopwords and names to exclude
exclude_words = set(
    stopwords.words('english') +
    ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", "hi", "janice"] +
    ['alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"]
)

# Function to clean and tokenize text
def clean_and_tokenize(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    tokens = word_tokenize(cleaned_text)
    return [token for token in tokens if token not in exclude_words and len(token) > 8]

# Read the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text
tokens = clean_and_tokenize(text)

# Calculate word frequencies
word_freq = Counter(tokens)

# Get the top 50 most frequent words
top_80_words = dict(word_freq.most_common(80))

# Plot the word frequency distribution
plt.figure(figsize=(15, 8))
plt.bar(top_80_words.keys(), top_80_words.values())
plt.title('Top 80 Word Frequency Distribution (Words > 6 letters)')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot
plt.savefig(output_path)

# Show the plot (optional)
plt.show()

# 2. wordcloud show
import os
import string
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources if not already downloaded
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# File path
file_path = r'C:\Users\grace\Desktop\Analysis\season1_friends.txt'
output_path = r'C:\Users\grace\Desktop\Analysis\wordcloud_season1.png'

# Stopwords and names to exclude
exclude_words = set(
    stopwords.words('english') +
    ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", "hi", "janice"] +
    ['alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"] +
    ["gonna", "steve", "cant","wasnt", "angela", "isnt", "huh", "pheebs", "marcel", "wow", "whos", "ok", "barry"] +
    ["wan na", "gon", "na", "guy", "dont", "yes", "doesnt", "ooh", "ethan", "kinda"]

)

# Function to clean and tokenize text
def clean_and_tokenize(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    tokens = word_tokenize(cleaned_text)
    return [token for token in tokens if token not in exclude_words]

# Read the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text
tokens = clean_and_tokenize(text)

# Combine tokens into a single string for word cloud
text_for_wordcloud = ' '.join(tokens)

# Generate and plot the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud for Season 1 (Excluding Specified Words)')
plt.axis('off')
plt.tight_layout()

# Save the word cloud
plt.savefig(output_path)

# Show the word cloud (optional)
plt.show()


