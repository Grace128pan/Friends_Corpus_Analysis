import os
import nltk
import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# File paths for character lines
characters_lines_paths = {
    'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
    'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
    'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
    'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
    'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
    'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
}

# Preprocess text data
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words and word not in string.punctuation]
    return tokens

# Build interaction networks
def build_interaction_networks(characters_lines_paths):
    networks = {}

    for character, file_path in characters_lines_paths.items():
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        character_network = nx.Graph()
        character_tokens = set()

        for line in lines:
            tokens = preprocess_text(line)
            character_tokens.update(tokens)

        for other_character, other_file_path in characters_lines_paths.items():
            if character != other_character:
                with open(other_file_path, 'r', encoding='utf-8') as other_file:
                    other_lines = other_file.readlines()

                other_character_tokens = set()

                for other_line in other_lines:
                    other_tokens = preprocess_text(other_line)
                    other_character_tokens.update(other_tokens)

                shared_tokens = character_tokens.intersection(other_character_tokens)
                if shared_tokens:
                    character_network.add_edge(character, other_character, weight=len(shared_tokens))

        networks[character] = character_network

    return networks

# Visualize the networks
def visualize_interaction_network(network, character, save_path):
    pos = nx.spring_layout(network)
    plt.figure(figsize=(8, 8))
    nx.draw(network, pos, with_labels=True, font_size=8, font_color='black', node_size=800, node_color='skyblue', edge_color='gray', linewidths=0.5)
    plt.title(f'Interaction Network for {character}')
    plt.savefig(save_path)
    plt.close()

# Analyze the networks
def analyze_networks(networks):
    for character, network in networks.items():
        print(f"\nAnalysis for {character}:")
        print(f"Number of nodes: {network.number_of_nodes()}")
        print(f"Number of edges: {network.number_of_edges()}")
        print(f"Average degree: {sum(dict(network.degree()).values()) / network.number_of_nodes()}")
        print(f"Clustering coefficient: {nx.average_clustering(network)}")
        print(f"Degree centrality: {nx.degree_centrality(network)}")

# Execute the analysis
def main():
    # Create the Analysis folder if it doesn't exist
    analysis_folder = 'C:\\Users\\grace\\Desktop\\Analysis'
    os.makedirs(analysis_folder, exist_ok=True)

    interaction_networks = build_interaction_networks(characters_lines_paths)
    analyze_networks(interaction_networks)

    # Visualize and save the interaction network for each character
    for character, network in interaction_networks.items():
        save_path = os.path.join(analysis_folder, f'Interaction_Network_{character}.png')
        visualize_interaction_network(network, character, save_path)

if __name__ == "__main__":
    main()
