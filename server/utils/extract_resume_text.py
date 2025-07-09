import sys
import fitz
import re

def clean(text):
    # Keep common symbols, accents, punctuation
    text = re.sub(r'[^\x09\x0A\x0D\x20-\x7E•*-]', '', text)

    headings = [
        "Technical Skills", "Projects", "Experience",
        "Education", "Achievements", "Certifications"
    ]
    for h in headings:
        text = re.sub(rf'(?i)(?<!\n)({h})', r'\n\n\1', text)
    text = re.sub(r'\.\s+', '.\n', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    print("🔥 CLEAN FUNCTION CALLED", file=sys.stderr)
    return clean(text)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    cleaned = extract_text_from_pdf(pdf_path)
    print(cleaned)
    with open("extracted_resume.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)
