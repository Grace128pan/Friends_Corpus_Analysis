import os
import matplotlib.pyplot as plt
from nltk import sent_tokenize

# Set the path to your text file
file_path = "C:/Users/grace/Desktop/Analysis/S10_Rachel/rachel_lines_season10.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Calculate the length of each sentence
    sentence_lengths = [len(sentence.split()) for sentence in sentences]

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(sentence_lengths, bins=range(1, max(sentence_lengths) + 1), edgecolor='black')
    plt.title("Sentence Length Distribution of Rachel's Lines in Season 10")
    plt.xlabel("Sentence Length")
    plt.ylabel("Number of Sentences")
    plt.grid(axis='y', alpha=0.75)
    plt.show()
