import os
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Set the paths to the text files
file_paths = [
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt",
]

# Set stopwords and exclude words
exclude_words = set(
    stopwords.words('english') +
    ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", "hi", "janice"] +
    ['alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"] +
    ["danielle", "couldve", "couldnt", "whaddya", "dont", "yes", "guy"]
)

# Process each character's file
character_word_counts = {}
for path in file_paths:
    character_name = os.path.splitext(os.path.basename(path))[0].split('_')[0]
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = [word.lower() for line in lines for word in word_tokenize(line) if len(word) > 6 and word.lower() not in exclude_words]
        word_counts = Counter(words)
        character_word_counts[character_name] = word_counts

# Get the top 30 words for each character
top_words = {character: counts.most_common(20) for character, counts in character_word_counts.items()}

# Plot the word frequencies for each character
plt.figure(figsize=(15, 10))
for character, words in top_words.items():
    words, counts = zip(*words)
    plt.barh(words, counts, label=character)

plt.xlabel('Word Frequency')
plt.ylabel('Words')
plt.title('Top 20 Word Frequencies for Each Character')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
