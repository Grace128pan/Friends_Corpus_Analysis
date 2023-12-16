import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import pyLDAvis.gensim_models
import warnings

# Disable warnings for better clarity
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Download NLTK resources (if not already downloaded)
nltk.download('stopwords')
nltk.download('punkt')

# File paths for character lines
characters_lines_paths = {
    'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
    'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
    'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
    'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
    'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
    'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
}

# Path to the Analysis folder on the desktop
analysis_folder = 'C:\\Users\\grace\\Desktop\\Analysis'
os.makedirs(analysis_folder, exist_ok=True)


# Function to preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    character_names = ['chandler', 'monica', 'phoebe', 'rachel', 'ross', 'joey']

    tokens = word_tokenize(text.lower())

    # Exclude stopwords, character names, and punctuations
    filtered_tokens = [word for word in tokens if
                       word.isalpha() and word not in stop_words and word not in character_names and len(word) > 6]

    return filtered_tokens


# Tokenize and preprocess character lines
character_lines = {}

for character, file_path in characters_lines_paths.items():
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        character_lines[character] = [preprocess_text(line) for line in lines]

# Flatten the list of tokens for each character
character_lines_flat = {character: [token for tokens in tokens_list for token in tokens]
                        for character, tokens_list in character_lines.items()}

# Create a dictionary representation of the documents
dictionary = Dictionary(character_lines_flat.values())

# Create a corpus (bag of words) representation of the documents
corpus = [dictionary.doc2bow(doc) for doc in character_lines_flat.values()]

# Train the LDA model
lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15, random_state=42)

# Save LDA model
lda_model.save(os.path.join(analysis_folder, 'lda_model_filtered'))

# Visualize the LDA results
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(vis, os.path.join(analysis_folder, 'lda_visualization_filtered.html'))

print(f"LDA analysis results (filtered) saved to: {analysis_folder}")
