# 1. get rachel_lines_season1 txt file
# File paths
input_file_path = "C:/Users/grace/Desktop/Analysis/season1_friends.txt"
output_file_path = "C:/Users/grace/Desktop/Analysis/rachel_lines_season1.txt"

# Function to extract Rachel's lines
def extract_rachel_lines(script_text):
    lines = []
    rachel_speaking = False

    for line in script_text:
        # Detect when Rachel starts speaking
        if "Rachel:" in line:
            rachel_speaking = True
            lines.append(line)
        # Detect when another character starts speaking
        elif line.startswith(("Ross:", "Monica:", "Chandler:", "Joey:", "Phoebe:")):
            rachel_speaking = False
        # Append the line if Rachel is still speaking
        elif rachel_speaking:
            lines.append(line)

    return lines

# Read the script file
with open(input_file_path, 'r', encoding='utf-8') as file:
    script_lines = file.readlines()

# Extract Rachel's lines
rachel_lines = extract_rachel_lines(script_lines)

# Save Rachel's lines to a new file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(rachel_lines)

# 2. check word frequency and N-gram linguistic patterns
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
import string
import os

# Download the 'stopwords' resource
nltk.download('stopwords')

# File paths
input_file_path = "C:/Users/grace/Desktop/Analysis/rachel_lines_season1.txt"
output_file_path = "C:/Users/grace/Desktop/Analysis/Word_frequencies.txt"

# Read Rachel's lines from the file
with open(input_file_path, 'r', encoding='utf-8') as file:
    rachel_lines = file.read()

# Tokenize words
words = word_tokenize(rachel_lines)

# Remove punctuation and convert to lowercase
words = [word.lower() for word in words if word.isalnum()]

# Define stopwords and character names to exclude
stop_words = set(stopwords.words('english'))
character_names = ['rachel', 'monica', 'chandler', 'joey', 'phoebe', 'barry', 'ross']

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





