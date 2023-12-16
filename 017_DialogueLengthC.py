import nltk
import matplotlib.pyplot as plt

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

characters_lines_paths = {
    'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
    'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
    'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
    'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
    'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
    'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
}

def analyze_lines(character, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Calculate sentence length
    sentence_lengths = [len(nltk.word_tokenize(line)) for line in lines]

    # Calculate sentence complexity (average POS tags per sentence)
    complexity_scores = []
    for line in lines:
        tokens = nltk.word_tokenize(line)
        pos_tags = nltk.pos_tag(tokens)
        complexity_scores.append(len(set(tag for word, tag in pos_tags)) / len(tokens))

    return sentence_lengths, complexity_scores

def plot_distribution(data, title, xlabel, ylabel):
    plt.hist(data, bins=20, alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Iterate through characters and analyze lines
for character, file_path in characters_lines_paths.items():
    lengths, complexities = analyze_lines(character, file_path)

    # Plot sentence length distribution
    plot_distribution(lengths, f'{character} Sentence Length Distribution', 'Sentence Length', 'Frequency')

    # Plot complexity analysis distribution
    plot_distribution(complexities, f'{character} Sentence Complexity Distribution', 'Sentence Complexity', 'Frequency')
