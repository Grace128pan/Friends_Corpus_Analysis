import os
import nltk
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
from nltk import bigrams, trigrams
from nltk.tokenize import word_tokenize
from collections import Counter

# Set the file paths for each character
file_paths = [
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt",
]

# Define the set of excluded words
exclude_words = set(
    stopwords.words('english') +
    ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", "hi", "janice"] +
    ['alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"] +
    ["danielle", "couldve", "couldnt", "whaddya", "dont", "yes", "guy"]
)

# Function to process lines and generate n-grams
def process_lines(file_path, n_value):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    tokens = [word.lower() for line in lines for word in word_tokenize(line) if word.isalpha() and len(word) > 6 and word.lower() not in exclude_words]
    ngrams = list(bigrams(tokens)) if n_value == 2 else list(trigrams(tokens))
    return Counter(ngrams)

# Process lines for each character and generate n-grams
character_ngrams_2 = {os.path.basename(file_path).split('_')[0]: process_lines(file_path, 2) for file_path in file_paths}
top_bigrams_all = {character: Counter(ngrams).most_common(30) for character, ngrams in character_ngrams_2.items()}
character_ngrams_3 = {os.path.basename(file_path).split('_')[0]: process_lines(file_path, 3) for file_path in file_paths}
top_trigrams_all = {character: Counter(ngrams).most_common(30) for character, ngrams in character_ngrams_3.items()}

# Prepare data for plotting
characters = list(top_bigrams_all.keys())
top_bigrams_data = {character: [bigram[0] for bigram in top_bigrams_all[character]] for character in characters}
top_trigrams_data = {character: [trigram[0] for trigram in top_trigrams_all[character]] for character in characters}

# Plotting bar charts for bigrams
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

for character, ax in zip(characters, axes):
    x = np.arange(len(top_bigrams_data[character]))
    y = [len(bigram[0]) for bigram in top_bigrams_all[character]]
    ax.bar(x, y, alpha=0.8, label=character)
    ax.set_xticks(x)
    ax.set_xticklabels(top_bigrams_data[character], rotation=45)
    ax.set_title(f'Top 30 Bigrams - {character}')
    ax.set_xlabel('Bigrams')
    ax.set_ylabel('Count')

plt.tight_layout()
plt.show()

# Plotting bar charts for trigrams
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

for character, ax in zip(characters, axes):
    x = np.arange(len(top_trigrams_data[character]))
    y = [len(trigram[0]) for trigram in top_trigrams_all[character]]
    ax.bar(x, y, alpha=0.8, label=character)
    ax.set_xticks(x)
    ax.set_xticklabels(top_trigrams_data[character], rotation=45)
    ax.set_title(f'Top 30 Trigrams - {character}')
    ax.set_xlabel('Trigrams')
    ax.set_ylabel('Count')

plt.tight_layout()
plt.show()



