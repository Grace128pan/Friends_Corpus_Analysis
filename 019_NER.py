import spacy
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

# Load spaCy English model with NER
nlp = spacy.load('en_core_web_sm')

# File paths for character lines
characters_lines_paths = {
    'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
    'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
    'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
    'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
    'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
    'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
}

# Path to the Analysis folder
analysis_folder = 'C:\\Users\\grace\\Desktop\\Analysis'
os.makedirs(analysis_folder, exist_ok=True)

# Function to perform NER analysis for a character's lines
def perform_ner_analysis(character, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    entities_count = defaultdict(int)

    for line in lines:
        doc = nlp(line)
        for ent in doc.ents:
            entities_count[ent.label_] += 1

    return entities_count

# Perform NER analysis for each character
characters_entities = {}

for character, file_path in characters_lines_paths.items():
    entities_count = perform_ner_analysis(character, file_path)
    characters_entities[character] = entities_count

# Create a DataFrame for better plotting
import pandas as pd

df = pd.DataFrame(characters_entities).fillna(0).transpose()

# Visualize the NER analysis results in a single graph
plt.figure(figsize=(12, 8))

sns.set_palette("husl")  # Use a different color palette for better distinguishability
df.plot(kind='bar', stacked=True)
plt.title('NER Analysis Comparison Between Characters')
plt.xlabel('Character')
plt.ylabel('Frequency')
plt.legend(title='Entity Types', bbox_to_anchor=(1, 1))
plt.tight_layout()

# Save the graph to a file
graph_file_path = os.path.join(analysis_folder, 'NER_Analysis_Comparison_All_Characters.png')
plt.savefig(graph_file_path)
plt.show()

# Save the detailed results to a text file
result_file_path = os.path.join(analysis_folder, 'NER_Analysis_Comparison_All_Characters.txt')
df.to_csv(result_file_path, sep='\t')

print(f"NER analysis comparison results saved to: {result_file_path}")
print(f"Graph saved to: {graph_file_path}")



