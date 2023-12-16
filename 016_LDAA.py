import os
import nltk
import gensim
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
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

# Function to perform topic modeling using LDA
def perform_lda(character_name, lines_path, num_topics=5, num_words=5):
    with open(lines_path, 'r', encoding='utf-8') as file:
        lines = file.read()

    # Tokenize the text
    tokens = word_tokenize(lines)

    # Remove stopwords, specific words, and punctuations
    filtered_tokens = [word for word in tokens if word.lower() not in exclude_words and word not in punctuation]

    # Create a dictionary and corpus for LDA
    dictionary = gensim.corpora.Dictionary([filtered_tokens])
    corpus = [dictionary.doc2bow(filtered_tokens)]

    # Perform LDA
    lda_model = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

    # Visualize the results using pyLDAvis
    vis_data = gensimvis.prepare(lda_model, corpus, dictionary)

    # Save the pyLDAvis visualization
    output_path = f'C:\\Users\\grace\\Desktop\\Analysis\\{character_name}_lda_visualization.html'
    pyLDAvis.save_html(vis_data, output_path)

# Apply LDA for each character and visualize the results
for character, lines_path in characters_lines_paths.items():
    perform_lda(character, lines_path)

