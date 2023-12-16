import os
import matplotlib.pyplot as plt
from nltk import sent_tokenize

# Set the path to your text file
file_path = "C:/Users/grace/Desktop/Analysis/S1_Rachel/rachel_lines_season1.txt"

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

    # Sort sentence lengths in descending order
    sorted_lengths = sorted(sentence_lengths, reverse=True)

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(sorted_lengths, bins=range(1, max(sorted_lengths) + 1), edgecolor='black')
    plt.title("Sentence Length Distribution of Rachel's Lines in Season 1")
    plt.xlabel("Sentence Length")
    plt.ylabel("Number of Sentences")
    plt.grid(axis='y', alpha=0.75)
    plt.show()
