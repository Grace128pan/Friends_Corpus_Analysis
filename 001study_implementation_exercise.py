import fitz  # PyMuPDF
import pandas as pd
import regex as re
import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define the path to the PDF file
pdf_path = "C:/Users/grace/Desktop/54547-EN.pdf"


# Function to extract text from a PDF page
def extract_text_from_page(pdf_document, page_number):
    page = pdf_document.load_page(page_number)
    return page.get_text("text")


# Load the PDF document
pdf_document = fitz.open(pdf_path)

# Search for "crafts" in the PDF and extract relevant information
crafts_sections = []
for page_number in range(len(pdf_document)):
    page_text = extract_text_from_page(pdf_document, page_number)

    # Use spaCy for NLP analysis
    doc = nlp(page_text)

    # Look for sentences containing "crafts"
    for sentence in doc.sents:
        if re.search(r'\bcrafts\b', sentence.text, flags=re.IGNORECASE):
            crafts_sections.append((page_number + 1, sentence.text))

# Create a dataframe to store the results
df = pd.DataFrame(crafts_sections, columns=["page", "summary"])
df["country"] = "Sweden"

# Save the results to a CSV file
df.to_csv("sweden_crafts_report.csv", index=False)

print("Data has been saved to sweden_crafts_report.csv")









