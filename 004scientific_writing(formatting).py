import fitz  # PyMuPDF
from docx import Document
from mtranslate import translate

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def translate_text(text):
    chunk_size = 1000  # Set your preferred chunk size
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    translated_chunks = []
    for chunk in chunks:
        translated_chunk = translate(chunk, 'en', 'auto')
        translated_chunks.append(translated_chunk)

    return ''.join(translated_chunks)

def create_docx(output_path, translated_text):
    doc = Document()
    doc.add_paragraph(translated_text)
    doc.save(output_path)

def main():
    pdf_path = "C:/Users/grace/Desktop/AQZhengZhuan.pdf"
    output_path = "C:/Users/grace/Desktop/Translated_Document.docx"

    # Extract text from the PDF
    chinese_text = extract_text_from_pdf(pdf_path)

    # Translate the text to English
    english_text = translate_text(chinese_text)

    # Create a Word document with the translated text
    create_docx(output_path, english_text)

if __name__ == "__main__":
    main()



