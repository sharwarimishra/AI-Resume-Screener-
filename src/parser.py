import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    """Opens a PDF and returns all the text found inside it."""
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text


def save_text_to_file(text, output_path):
    """Saves text to a .txt file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


def process_all_resumes(data_folder, output_folder):
    """Finds every PDF in data_folder, extracts its text, and saves it to output_folder."""
    for filename in os.listdir(data_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(data_folder, filename)
            print(f"Processing: {filename}")

            text = extract_text_from_pdf(pdf_path)

            output_filename = filename.replace(".pdf", ".txt")
            output_path = os.path.join(output_folder, output_filename)
            save_text_to_file(text, output_path)

    print("All resumes processed!")


if __name__ == "__main__":
    process_all_resumes("../data", "../output")