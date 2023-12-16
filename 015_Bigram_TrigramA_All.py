import os
import nltk
import networkx as nx
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import bigrams, trigrams
from nltk.tokenize import word_tokenize
from collections import Counter

# Define file paths and exclude words
file_paths = [
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt",
    "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt",
]

exclude_words = set(
    stopwords.words('english') +
    ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", "hi", "janice"] +
    ['alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"] +
    ["danielle", "couldve", "couldnt", "whaddya", "dont", "yes", "guy"]
)

# Function to process a character's file
def process_character_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = [word.lower() for line in lines for word in word_tokenize(line) if len(word) > 6 and word.lower() not in exclude_words and word.isalnum()]
        bigram_list = list(bigrams(words))
        trigram_list = list(trigrams(words))

    top_bigrams = Counter(bigram_list).most_common(30)
    top_trigrams = Counter(trigram_list).most_common(30)

    return top_bigrams, top_trigrams

# Create and save network graphs for each character
colors = ['red', 'orange', 'blue', 'green', 'gray', 'lightpink']  # Change Rachel's color to light pink

for i, file_path in enumerate(file_paths):
    character_name = os.path.basename(file_path).split('_')[0]  # Extract character name from file path
    top_bigrams, top_trigrams = process_character_file(file_path)

    # Create and save network graph for bigrams
    bigram_graph = nx.Graph()
    bigram_graph.add_edges_from(top_bigrams)

    plt.figure(figsize=(15, 12))
    pos = nx.kamada_kawai_layout(bigram_graph)
    nx.draw_networkx_nodes(bigram_graph, pos, node_size=1000, node_color=colors[i], alpha=0.8)
    nx.draw_networkx_edges(bigram_graph, pos, width=1.5, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(bigram_graph, pos, font_size=10, font_color='black', font_family='sans-serif')
    plt.title(f'Top 30 Bigrams Network Graph for {character_name}')
    plt.savefig(os.path.join(os.path.expanduser("~"), "Desktop", f"{character_name}_top_bigrams_network.png"))
    plt.show()

    # Create and save network graph for trigrams
    trigram_graph = nx.Graph()
    trigram_graph.add_edges_from(top_trigrams)

    plt.figure(figsize=(15, 12))
    pos = nx.kamada_kawai_layout(trigram_graph)
    nx.draw_networkx_nodes(trigram_graph, pos, node_size=1000, node_color=colors[i], alpha=0.8)
    nx.draw_networkx_edges(trigram_graph, pos, width=1.5, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(trigram_graph, pos, font_size=10, font_color='black', font_family='sans-serif')
    plt.title(f'Top 30 Trigrams Network Graph for {character_name}')
    plt.savefig(os.path.join(os.path.expanduser("~"), "Desktop", f"{character_name}_top_trigrams_network.png"))
    plt.show()


