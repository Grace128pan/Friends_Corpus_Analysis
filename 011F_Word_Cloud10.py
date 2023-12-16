import os
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import download

# Download the necessary resources
download('averaged_perceptron_tagger')
download('stopwords')

# Set the path to your text file
file_path = "C:/Users/grace/Desktop/Analysis/S10_Rachel/rachel_lines_season10.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    words = word_tokenize(text)

    # Set up stopwords
    custom_stopwords = set(stopwords.words('english'))
    custom_stopwords.update(['rachel', 'monica', 'chandler', 'ross', 'joey', 'phoebe', 'hi', 'hello', 'guy', 'kinda'])

    # Filter words based on length, stopwords, and names
    filtered_words = [word.lower() for word in words if len(word) > 6 and word.lower() not in custom_stopwords]

    # Create a string from the filtered words
    filtered_text = ' '.join(filtered_words)

    # Generate WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)

    # Plot the WordCloud image
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
