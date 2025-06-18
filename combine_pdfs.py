import fitz  # PyMuPDF
import csv
import os

def extract_and_append(pdf_path, writer, source_file=""):
    doc = fitz.open(pdf_path)
    for page in doc:
        for line in page.get_text().splitlines():
            parts = line.strip().split()
            # Expect at least: serial, roll, name‑tokens…, father1, father2, mother1, mother2, category
            if len(parts) >= 8 and parts[0].isdigit() and parts[1].isdigit():
                roll     = parts[1]
                category = parts[-1]
                mother   = ' '.join(parts[-3:-1])     # e.g. ["BABITA","DEVI"]
                father   = ' '.join(parts[-5:-3])     # e.g. ["RAJEEV","KUMAR"]
                name     = ' '.join(parts[2:-5])      # everything between roll and father
                writer.writerow([roll, name, father, mother, category, source_file])

def combine_pdfs_to_csv(folder_path, output_csv="data/data.csv"):
    os.makedirs("data", exist_ok=True)
    with open(output_csv, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ROLL", "NAME", "FATHERNAME", "MOTHERNAME", "CATEGORY", "SOURCE_FILE"])

        for filename in sorted(os.listdir(folder_path)):
            if filename.lower().endswith(".pdf"):
                full_path = os.path.join(folder_path, filename)
                print(f"🔍 Processing: {filename}")
                extract_and_append(full_path, writer, filename)

    print(f"\n✅ Combined CSV created at: {output_csv}")

if __name__ == "__main__":
    combine_pdfs_to_csv("data/raw_pdfs")
