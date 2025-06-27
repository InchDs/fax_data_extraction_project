# Fax Data Extraction Project

This project automates the extraction and structuring of key information from fax documents (PDF or image) using Optical Character Recognition (OCR), Natural Language Processing (NLP), and exports the results to Excel.

## Project Structure

```
fax_data_extraction_project
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── ocr_processing.py
│   ├── nlp_extraction.py
│   ├── excel_writer.py
│   └── config.py
├── data
│   ├── input_faxes
│   └── output
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Tesseract OCR** and add it to your system PATH:  
   [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)
4. **Install Poppler** (for PDF support) and add its `bin` folder to your PATH:  
   [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)

## Usage

1. Place your fax images or PDFs in the `data/input_faxes` directory.
2. Run the main script:
   ```bash
   python src/main.py
   ```
3. The extracted and structured data will be saved as an Excel file in `data/output/fax_processed.xlsx`.

## Features

- **OCR Processing:** Converts fax images and PDFs to text using PyTesseract and pdf2image.
- **NLP Extraction:** Extracts metadata such as dates, subject lines, and named entities using regex and spaCy.
- **Excel Export:** Structures and exports the extracted data to an Excel file using pandas.

## Testing

Unit tests are provided for each component. To run the tests:
```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file