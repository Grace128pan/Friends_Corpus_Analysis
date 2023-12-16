import PyPDF2
import spacy
import pandas as pd

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Open the PDF file
with open("Ireland.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Initialize variables to store the results
    data = []

    # Iterate through each page of the PDF
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()

        # Process the text using spaCy
        doc = nlp(text)

        # Extract relevant information about "crafts"
        for sentence in doc.sents:
            sentence_text = sentence.text

            if "crafts" in sentence_text.lower():
                # Extract the country and date information (customize as per your document)
                country = "Country Name"  # Replace with code to extract the country
                date = "Publication Date"  # Replace with code to extract the date

                data.append({
                    "Country": country,
                    "Date": date,
                    "Summary": sentence_text,
                    "Page": page_num + 1
                })

# Create a DataFrame to store the results
df = pd.DataFrame(data)

# Save the results to a CSV file
df.to_csv("crafts_summary.csv", index=False)

