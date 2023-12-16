import spacy
import pandas as pd

# Download the spaCy English model
spacy.cli.download("en_core_web_sm")

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")


def detect_humor_entities(script_path):
    with open(script_path, 'r', encoding='utf-8') as file:
        script = file.read()

    # Process the entire script with spaCy
    doc = nlp(script)

    # Extract sentences with entities related to humor
    humor_data = [{'Sentence': sent.text, 'HumorEntities': ', '.join(
        [ent.text for ent in sent.ents if "comedy" in ent.text.lower() or "joke" in ent.text.lower()])} for sent in
                  doc.sents]

    return humor_data


def save_to_csv(data, output_path):
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    # Update the script path based on your file location
    script_path = "C:/Users/grace/Desktop/Analysis/season1_friends.txt"

    # Define the output CSV file path
    output_csv_path = "C:/Users/grace/Desktop/Analysis/humor_data_output.csv"

    # Detect humor entities in the script
    humor_data = detect_humor_entities(script_path)

    # Save the detected humor data to a CSV file
    save_to_csv(humor_data, output_csv_path)

    print("Humor data detected and saved to:", output_csv_path)




