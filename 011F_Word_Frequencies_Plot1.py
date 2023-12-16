# 3. plot show the word frequencies
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
import string
import os
import matplotlib.pyplot as plt

# Download the 'stopwords' resource
nltk.download('stopwords')

# File paths
input_file_path = "C:/Users/grace/Desktop/Analysis/S1_rachel/rachel_lines_season1.txt"
output_folder = "C:/Users/grace/Desktop/Analysis"
output_file_path = os.path.join(output_folder, "Word_frequencies.txt")

# Read Rachel's lines from the file
with open(input_file_path, 'r', encoding='utf-8') as file:
    rachel_lines = file.read()

# Tokenize words
words = word_tokenize(rachel_lines)

# Remove punctuation and convert to lowercase
words = [word.lower() for word in words if word.isalnum()]

# Define stopwords and character names to exclude
stop_words = set(stopwords.words('english'))
character_names = ['rachel', 'monica', 'chandler', 'joey', 'phoebe', 'barry', 'ross', "mindy", "marcel", "paolo", "pheebs"]

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

# Plotting word frequencies
plt.figure(figsize=(10, 5))
filtered_word_frequencies = {word: freq for word, freq in word_frequencies.items() if freq > 8}
sorted_word_frequencies = dict(sorted(filtered_word_frequencies.items(), key=lambda item: item[1], reverse=True))
plt.bar(sorted_word_frequencies.keys(), sorted_word_frequencies.values())
plt.title('Word Frequencies (Over 8)')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
word_freq_plot_path = os.path.join(output_folder, "Word_Frequencies_Plot.png")
plt.savefig(word_freq_plot_path)
plt.show()

# Plotting bigram frequencies
plt.figure(figsize=(12, 5))
filtered_bigram_frequencies = {tuple(bigram): freq for bigram, freq in bigram_frequencies.items() if freq > 2}
sorted_bigram_frequencies = dict(sorted(filtered_bigram_frequencies.items(), key=lambda item: item[1], reverse=True))
plt.bar([str(bigram) for bigram in sorted_bigram_frequencies.keys()], sorted_bigram_frequencies.values())
plt.title('Bigram Frequencies (Over 2)')
plt.xlabel('Bigrams')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
bigram_freq_plot_path = os.path.join(output_folder, "Bigram_Frequencies_Plot.png")
plt.savefig(bigram_freq_plot_path)
plt.show()

# Plotting trigram frequencies
plt.figure(figsize=(15, 5))
filtered_trigram_frequencies = {tuple(trigram): freq for trigram, freq in trigram_frequencies.items() if freq > 2}
sorted_trigram_frequencies = dict(sorted(filtered_trigram_frequencies.items(), key=lambda item: item[1], reverse=True))
plt.bar([str(trigram) for trigram in sorted_trigram_frequencies.keys()], sorted_trigram_frequencies.values())
plt.title('Trigram Frequencies (Over 2)')
plt.xlabel('Trigrams')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
trigram_freq_plot_path = os.path.join(output_folder, "Trigram_Frequencies_Plot.png")
plt.savefig(trigram_freq_plot_path)
plt.show()

print(f"Plots saved to {output_folder}")


