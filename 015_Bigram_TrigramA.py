import os
import nltk
import networkx as nx
import matplotlib.pyplot as plt
from nltk import bigrams, trigrams, FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define the characters and their corresponding lines paths
characters_lines_paths = {
    'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
    'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
    'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
    'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
    'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
    'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
}

# Additional stopwords and words to exclude
exclude_words = set([
    'hi', 'janice', 'pacinos', 'lorraine', 'whereve', 'mississippi', 'notnotmine', 'notmine'
] + list(stopwords.words('english')) + ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", 'alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um", "monicas"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"] +
    ["danielle", "couldve", "couldnt", "whaddya", "dont", "yes", "guy"])

# Function to create and visualize network graph for limited bigrams and trigrams
def visualize_network_graph(character_name, lines_path, n=20):
    with open(lines_path, 'r', encoding='utf-8') as file:
        lines = file.read()

    # Tokenize the text
    tokens = word_tokenize(lines)

    # Remove stopwords, specific words, and punctuations
    filtered_tokens = [word for word in tokens if word.lower() not in exclude_words and word not in punctuation]

    # Get bigrams and trigrams
    bigram_list = list(bigrams(filtered_tokens))[:n]
    trigram_list = list(trigrams(filtered_tokens))[:n]

    # Create a network graph for bigrams
    bigram_graph = nx.Graph()
    bigram_graph.add_edges_from(bigram_list)

    # Create a network graph for trigrams
    trigram_graph = nx.Graph()
    trigram_graph.add_edges_from((node1, node2) for node1, node2, _ in trigram_list)

    # Visualize and save the network graphs
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    nx.draw(bigram_graph, with_labels=True, font_size=8, font_color='black', node_size=1000, alpha=0.7)
    plt.title(f'Top {n} Bigrams for {character_name}')
    plt.text(0.5, -0.15, f'Top {n} Bigrams', ha='center', va='center', transform=plt.gca().transAxes)

    plt.subplot(1, 2, 2)
    nx.draw(trigram_graph, with_labels=True, font_size=8, font_color='black', node_size=1000, alpha=0.7)
    plt.title(f'Top {n} Trigrams for {character_name}')
    plt.text(0.5, -0.15, f'Top {n} Trigrams', ha='center', va='center', transform=plt.gca().transAxes)

    plt.tight_layout()

    # Save the network graphs
    output_path = f'C:\\Users\\grace\\Desktop\\Analysis\\{character_name}_network_graphs.png'
    plt.savefig(output_path)
    plt.show()

# Analyze and visualize network graphs for top bigrams and trigrams for each character
for character, lines_path in characters_lines_paths.items():
    visualize_network_graph(character, lines_path)




