#1. get rachel lines in season10
import os

# File paths
input_file_path = "C:/Users/grace/Desktop/Analysis/season10_friends.txt"
output_folder = "C:/Users/grace/Desktop/Analysis"
output_file_path = os.path.join(output_folder, "rachel_lines.txt")

# Read content from the input file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# Filter lines spoken by Rachel
rachel_lines = [line.strip() for line in lines if line.lower().startswith('rachel')]

# Save Rachel's lines to a new file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(rachel_lines))

print(f"Rachel's lines saved to {output_file_path}")

# 2. get the word frequencies
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter

# Download the 'stopwords' resource
nltk.download('stopwords')

# File paths
input_file_path = "C:/Users/grace/Desktop/Analysis/rachel_lines.txt"
output_folder = "C:/Users/grace/Desktop/Analysis"
output_file_path = os.path.join(output_folder, "rachel_word_frequencies.txt")

# Read content from the input file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    rachel_lines = input_file.read()

# Tokenize words
words = word_tokenize(rachel_lines)

# Remove punctuation and convert to lowercase
words = [word.lower() for word in words if word.isalnum()]

# Define stopwords and character names to exclude
stop_words = set(stopwords.words('english'))
character_names = ['phoebe', 'ross', 'monica', 'chandler', 'rachel', 'joey']

# Remove stopwords and character names, and filter words longer than 4 letters
filtered_words = [word for word in words if word not in stop_words and word not in character_names and len(word) > 4]

# Calculate word frequencies
word_frequencies = Counter(filtered_words)

# Function to extract n-grams
def extract_ngrams(text, n):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalnum()]
    ngrams_list = list(ngrams(tokens, n))
    return ngrams_list

# Extract bigrams and trigrams
filtered_rachel_lines = ' '.join(filtered_words)
bigrams = extract_ngrams(filtered_rachel_lines, 2)
trigrams = extract_ngrams(filtered_rachel_lines, 3)

# Calculate n-gram frequencies
bigram_frequencies = Counter(bigrams)
trigram_frequencies = Counter(trigrams)

# Save results to a text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write("Word Frequencies:\n")
    output_file.write(str(word_frequencies))

    output_file.write("\n\nBigram Frequencies:\n")
    output_file.write(str(bigram_frequencies))

    output_file.write("\n\nTrigram Frequencies:\n")
    output_file.write(str(trigram_frequencies))

print(f"Results saved to {output_file_path}")
