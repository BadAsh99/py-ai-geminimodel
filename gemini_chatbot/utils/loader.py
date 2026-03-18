import fitz  # PyMuPDF
import pandas as pd

def load_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

def load_csv_text(csv_path):
    df = pd.read_csv(csv_path)
    return df.to_string(index=False)

