import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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

# Collect data for comparative analysis
data = {'Character': [], 'Sentence Length': [], 'Sentence Complexity': []}

for character, file_path in characters_lines_paths.items():
    lengths, complexities = analyze_lines(character, file_path)
    data['Character'].extend([character] * len(lengths))
    data['Sentence Length'].extend(lengths)
    data['Sentence Complexity'].extend(complexities)

# Create a DataFrame
df = pd.DataFrame(data)

# Plot comparative scatter plot for sentence length vs. sentence complexity
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Sentence Length', y='Sentence Complexity', hue='Character', palette=['red', 'orange', 'green', 'grey', 'blue', 'purple'], alpha=0.7)
plt.title('Comparative Analysis of Sentence Length vs. Sentence Complexity')
plt.xlabel('Sentence Length')
plt.ylabel('Sentence Complexity')
plt.legend(title='Character')
plt.show()

# Plot comparative scatter plot for sentence complexity vs. character
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Sentence Complexity', y='Character', palette=['red', 'orange', 'green', 'grey', 'blue', 'purple'], alpha=0.7)
plt.title('Comparative Analysis of Sentence Complexity vs. Character')
plt.xlabel('Sentence Complexity')
plt.ylabel('Character')
plt.show()

# Plot comparative scatter plot for sentence length vs. character
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Sentence Length', y='Character', palette=['red', 'orange', 'green', 'grey', 'blue', 'purple'], alpha=0.7)
plt.title('Comparative Analysis of Sentence Length vs. Character')
plt.xlabel('Sentence Length')
plt.ylabel('Character')
plt.show()
