import fitz
import json
import re
import os

pdf_path = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Car questions\汽車筆試題庫_英文完整版_115年_含圖示_1090題.pdf'
doc = fitz.open(pdf_path)
img_dir = r'assets\car_signs'
os.makedirs(img_dir, exist_ok=True)

# 1. Parse text & question blocks across pages
all_text = ""
page_offsets = []

for pno in range(len(doc)):
    page = doc[pno]
    txt = page.get_text('text')
    page_offsets.append((pno, len(all_text)))
    all_text += f"\n--- PAGE {pno+1} ---\n" + txt

# Extract questions matching pattern: Question Number, Answer e.g. "(1)", Question Text/Options
# Regular expression to match question blocks:
# \n(\d{1,4})\s*\n\s*\(([123])\)\s*\n
pattern = re.compile(r'\n(\d{1,4})\s*\n\s*\(([123])\)\s*\n', re.MULTILINE)

matches = list(pattern.finditer(all_text))
print(f"Found {len(matches)} question pattern matches in Car 1090 PDF.")

parsed_car_qs = []
current_section = "Correct Concepts and Ethics"

for i in range(len(matches)):
    m = matches[i]
    q_num = int(m.group(1))
    ans_num = int(m.group(2))
    
    start_pos = m.end()
    end_pos = matches[i+1].start() if i+1 < len(matches) else len(all_text)
    
    q_block = all_text[start_pos:end_pos].strip()
    
    # Filter out page header/footer markers from q_block
    q_lines = [l.strip() for l in q_block.split('\n') if l.strip() and not l.startswith('Automobile Written Exam') and not l.startswith('—') and not l.startswith('SECTION')]
    
    full_q_text = " ".join(q_lines)
    
    # Extract options (1) ... (2) ... (3) ...
    opts = []
    opt_parts = re.split(r'\s*\(([123])\)\s*', full_q_text)
    stem = opt_parts[0].strip()
    if len(opt_parts) >= 7:
        opts = [f"({opt_parts[1]}) {opt_parts[2].strip()}", f"({opt_parts[3]}) {opt_parts[4].strip()}", f"({opt_parts[5]}) {opt_parts[6].strip()}"]
    elif len(opts) == 0:
        # True/False format or direct options
        if 'True' in full_q_text or 'False' in full_q_text:
            opts = ["(1) True.", "(2) False."]
        else:
            opts = [full_q_text]
            
    ans_idx = ans_num - 1
    c_ans = opts[ans_idx] if ans_idx < len(opts) else f"({ans_num})"
    
    # Determine category/section
    cat = "Car Regulations - Multiple Choice"
    if q_num <= 450:
        cat = "Car Regulations - Ethics & Misconduct"
    elif q_num <= 654:
        cat = "Car Regulations - Proactive Yielding"
    else:
        cat = "Car Regulations - Safe Driving & Signs"

    parsed_car_qs.append({
        "id": f"CAR_{q_num:04d}",
        "official_num": q_num,
        "category": cat,
        "topic": "Official THB Car License Examination Bank",
        "question": stem if stem else full_q_text,
        "options": opts,
        "correct_answer": c_ans,
        "correct_index": ans_idx,
        "explanation": f"Official Taiwan THB Automobile Driver License Rule #{q_num}. Mandatory safety standard for driver examination."
    })

print(f"Successfully parsed {len(parsed_car_qs)} Car questions.")
with open('car_1090_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_car_qs, f, indent=2, ensure_ascii=False)
