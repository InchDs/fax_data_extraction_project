# Configuration settings for the fax data extraction project

# Input and output paths
INPUT_FAXES_PATH = 'data/input_faxes/'
OUTPUT_EXCEL_PATH = 'data/output/extracted_data.xlsx'

# OCR settings
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as necessary

# NLP settings
NER_MODEL_PATH = 'path/to/your/ner/model'  # Update this path as necessary

# Constants
DATE_FORMAT = '%Y-%m-%d'  # Desired date format for extracted dates
SUBJECT_KEYWORDS = ['Subject', 'Re:', 'Fwd:', 'Objet:']  # Keywords to identify subject lines in text