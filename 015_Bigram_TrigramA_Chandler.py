import os
import nltk
import networkx as nx
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import bigrams, trigrams
from nltk.tokenize import word_tokenize
from collections import Counter

# Set the path to Chandler's text file
file_path_chandler = "C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt"

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

# Process Chandler's file
with open(file_path_chandler, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    words = [word.lower() for line in lines for word in word_tokenize(line) if len(word) > 6 and word.lower() not in exclude_words and word.isalnum()]
    bigram_list = list(bigrams(words))
    trigram_list = list(trigrams(words))

# Get the top 30 bigrams and trigrams for Chandler
top_chandler_bigrams = Counter(bigram_list).most_common(30)
top_chandler_trigrams = Counter(trigram_list).most_common(30)

# Create and save network graphs for Chandler's bigrams and trigrams
chandler_bigram_graph = nx.Graph()
chandler_bigram_graph.add_edges_from(top_chandler_bigrams)

plt.figure(figsize=(15, 12))
pos = nx.spring_layout(chandler_bigram_graph, seed=42, k=0.4, iterations=50)
nx.draw_networkx_nodes(chandler_bigram_graph, pos, node_size=1000, node_color='skyblue', alpha=0.8)
nx.draw_networkx_edges(chandler_bigram_graph, pos, width=1.5, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(chandler_bigram_graph, pos, font_size=10, font_color='black', font_family='sans-serif')
plt.title('Top 30 Bigrams Network Graph for Chandler')
plt.savefig(os.path.join(os.path.expanduser("~"), "Desktop", "Chandler_top_bigrams_network.png"))
plt.show()

chandler_trigram_graph = nx.Graph()
chandler_trigram_graph.add_edges_from(top_chandler_trigrams)

plt.figure(figsize=(15, 12))
pos = nx.spring_layout(chandler_trigram_graph, seed=42, k=0.4, iterations=50)
nx.draw_networkx_nodes(chandler_trigram_graph, pos, node_size=1000, node_color='lightcoral', alpha=0.8)
nx.draw_networkx_edges(chandler_trigram_graph, pos, width=1.5, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(chandler_trigram_graph, pos, font_size=10, font_color='black', font_family='sans-serif')
plt.title('Top 30 Trigrams Network Graph for Chandler')
plt.savefig(os.path.join(os.path.expanduser("~"), "Desktop", "Chandler_top_trigrams_network.png"))
plt.show()




