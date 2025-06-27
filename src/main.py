# main.py

import os
from ocr_processing import fax_to_text
from nlp_extraction import extract_metadata
from excel_writer import save_to_excel
from config import INPUT_FAXES_PATH, OUTPUT_EXCEL_PATH

def main():
    fax_data = []
    for filename in os.listdir(INPUT_FAXES_PATH):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.pdf')):
            file_path = os.path.join(INPUT_FAXES_PATH, filename)
            text = fax_to_text(file_path)
            metadata = extract_metadata(text)
            # Aplatir les champs pour Excel
            fax_data.append({
                "filename": filename,
                "dates": ", ".join(metadata.get("dates", [])),
                "subject": metadata.get("subject", ""),
                "entities": ", ".join(
                    [f"{k}: {', '.join(v)}" for k, v in metadata.get("entities", {}).items()]
                ),
                "text": text
            })

    save_to_excel(fax_data, OUTPUT_EXCEL_PATH)

if __name__ == "__main__":
    main()