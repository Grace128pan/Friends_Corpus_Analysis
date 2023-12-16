import os
import string
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources if not already downloaded
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# File paths
rachel_lines_file_path = r'C:\Users\grace\Desktop\Analysis\Character_Lines\Rachel_lines.txt'
analysis_folder_path = r'C:\Users\grace\Desktop\Analysis'

# Stopwords and names to exclude
exclude_words_common = set(
    stopwords.words('english') +
    ['Monica', 'Chandler', 'Ross', 'Phoebe', 'Joey', 'Rachel', "Monicas", "Rachels", "Tribbiani", "Franzblau"] +
    ['monica', 'chandler', 'ross', 'phoebe', 'joey', 'rachel', "tribbiani", "franzblau", "rachels", "hi", "janice"] +
    ['alright', 'youre', 'gonna', 'right', 'thats', 'going', 'susan', 'yknow', 'carol', 'alright', 'sorry', 'could'] +
    ["chandlers", "wouldnt", "already", "uh", "im", "oh", "well", "yeah", "ursula", "hes", "well", "okay", "um", "monicas"] +
    ["theyre", "nina", "theres", "paolo", "shes", "paul", "hello", "hey", "whats", "mindy", "didnt", "David", "wanna"] +
    ["danielle", "couldve", "couldnt", "whaddya", "dont", "yes", "guy"] + ["pacinos", "lorraine", "whereve", "mississippi"] +
    ["notnotmine", "notmine"]
)

# Function to clean and tokenize text
def clean_and_tokenize(text, exclude_words):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    tokens = word_tokenize(cleaned_text)
    return [token for token in tokens if token not in exclude_words and len(token) > 6]

# Read Rachel's lines
with open(rachel_lines_file_path, 'r', encoding='utf-8') as file:
    rachel_lines = file.read()

# Tokenize the text for common exclude words
tokens_common = clean_and_tokenize(rachel_lines, exclude_words_common)

# Calculate word frequencies for common exclude words
word_freq_common = Counter(tokens_common)

# Get the top 80 most frequent words for common exclude words
top_80_words_common = dict(word_freq_common.most_common(80))

# Plot the word frequency distribution for common exclude words
plt.figure(figsize=(15, 8))
plt.bar(top_80_words_common.keys(), top_80_words_common.values())
plt.title('Top 80 Word Frequency Distribution for Rachel (Common Exclude Words)')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot for common exclude words
common_exclude_output_path = os.path.join(analysis_folder_path, 'rachel_word_frequency_common_exclude_plot.png')
plt.savefig(common_exclude_output_path)

# Generate and plot the word cloud for common exclude words
text_for_wordcloud_common = ' '.join(tokens_common)
wordcloud_common = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud_common)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_common, interpolation='bilinear')
plt.title('Word Cloud for Rachel (Common Exclude Words)')
plt.axis('off')
plt.tight_layout()

# Save the word cloud for common exclude words
common_exclude_wordcloud_output_path = os.path.join(analysis_folder_path, 'rachel_wordcloud_common_exclude.png')
plt.savefig(common_exclude_wordcloud_output_path)

# Show the plots (optional)
plt.show()
