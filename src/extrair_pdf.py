import os
import sys
from pypdf import PdfReader

def create_corpus_from_pdf(pdf_path):
    """Extrai texto de um arquivo PDF e retorna uma lista de palavras.

    Args:
        pdf_path (str): Caminho para o arquivo PDF.

    Returns:
        list[str]: Lista de palavras extraídas do PDF.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: The file path '{pdf_path}' does not exist.", file=sys.stderr)
        return []
# insert error correction in case of missing file or incorrect path.
    print(f"Extracting text from: {os.path.basename(pdf_path)}...")
    
    # 1. Open the PDF and read digital text per page
    pdf = PdfReader(pdf_path)
    full_text = []
    
    for page in pdf.pages:

        text = page.extract_text()
        if text:
            full_text.append(text.strip())     

    # Combine text streams and clear arbitrary Windows line endings
    combined_text = " ".join(full_text).replace("\n", "").strip()
    words = combined_text.split()
    return words
