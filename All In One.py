from docx import Document
import pytesseract
from PIL import Image
import io
import os

# Path to your updated DOCX file
docx_path = "FULL-WEB-DEVLOPMENT_UPDATED.docx"
output_dir = "extracted_images"
report_path = "image_text_report.txt"

# Make output folder
os.makedirs(output_dir, exist_ok=True)

# Load document
doc = Document(docx_path)
report = []

image_count = 0

# Extract images from DOCX
for rel in doc.part.rels.values():
    if "image" in rel.reltype:
        image_count += 1
        image_data = rel.target_part.blob
        image_path = os.path.join(output_dir, f"image_{image_count}.png")
        with open(image_path, "wb") as f:
            f.write(image_data)

        # OCR: detect visible text in image
        try:
            text = pytesseract.image_to_string(Image.open(image_path))
            text = text.strip()
        except Exception as e:
            text = f"[ERROR: {e}]"

        report.append(f"{image_path}:\n{text}\n{'-'*40}\n")

# Write results
with open(report_path, "w") as f:
    f.writelines(report)

print(f"\n✅ Extracted {image_count} images.")
print(f"📝 OCR results saved to: {report_path}")
