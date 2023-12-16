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
    sentences = text.split('.')
    chunks = []

    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:  # Add 1 for the period
            current_chunk += sentence + '.'
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + '.'

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)

    translated_chunks = []
    for chunk in chunks:
        # Split the chunk into smaller segments
        segments = [chunk[i:i + 500] for i in range(0, len(chunk), 500)]  # Set your preferred segment size
        for segment in segments:
            translated_segment = translate(segment, 'en', 'auto')
            translated_chunks.append(translated_segment)

    return ''.join(translated_chunks)

def create_docx(output_path, translated_text):
    doc = Document()
    doc.add_paragraph(translated_text)
    modified_output_path = output_path.replace('.docx', '_modified_new_version.docx')
    doc.save(modified_output_path)

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

