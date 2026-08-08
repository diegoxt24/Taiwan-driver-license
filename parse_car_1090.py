import fitz
import json
import re
import os

pdf_path = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Car questions\汽車筆試題庫_英文完整版_115年_含圖示_1090題.pdf'
doc = fitz.open(pdf_path)

os.makedirs(r'assets\car_signs', exist_ok=True)

questions = []
current_section = "Correct Concepts and Ethics"

# Iterate over all 86 pages
for pno in range(len(doc)):
    page = doc[pno]
    text = page.get_text('text')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # Detect Section headers
    for line in lines:
        if 'SECTION 1' in line:
            current_section = "Correct Concepts and Ethics"
        elif 'SECTION 2' in line:
            current_section = "Proactive Yielding Culture"
        elif 'SECTION 3' in line:
            current_section = "Safe Driving Ability"

    # We can group page text into question entries based on "No." or question number pattern
    # Let's inspect block items on the page
    blocks = page.get_text('blocks')
    # Filter out header/footer blocks
    valid_blocks = []
    for b in blocks:
        btxt = b[4].strip()
        if 'Automobile Written Exam' in btxt or 'SECTION' in btxt or btxt.startswith('—') or btxt == 'No.' or btxt == 'Ans' or btxt == 'Question':
            continue
        valid_blocks.append(b)

    # Sort blocks by vertical position y0
    valid_blocks.sort(key=lambda b: b[1])

print(f"Total pages in Car 1090 PDF: {len(doc)}")
