def fax_to_text(file_path):
    import cv2
    import pytesseract
    import os

    # Pour les PDF
    if file_path.lower().endswith('.pdf'):
        from pdf2image import convert_from_path
        images = convert_from_path(file_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text

    # Pour les images classiques
    image = cv2.imread(file_path)
    if image is None:
        print(f"Erreur : Impossible de lire le fichier image {file_path}")
        return ""
    text = pytesseract.image_to_string(image)
    return text