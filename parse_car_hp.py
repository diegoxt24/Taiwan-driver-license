import fitz
import json
import re
import os

os.makedirs(r'assets\car_signs', exist_ok=True)
os.makedirs(r'assets\moto_signs', exist_ok=True)

# ---------------------------------------------------------------------------
# 1. PARSE CAR HAZARD PERCEPTION (10 Questions)
# ---------------------------------------------------------------------------
car_hp_pdf = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Car questions\1150605-危險感知影片題(英文版).pdf'
doc_car_hp = fitz.open(car_hp_pdf)
page = doc_car_hp[0]

# Extract links
links = page.get_links()
video_link_map = {}
for l in links:
    rect = l['from']
    words = [w[4] for w in page.get_text('words') if rect.intersects(fitz.Rect(w[:4]))]
    vnum = ' '.join(words).strip()
    if vnum.isdigit() and l.get('uri'):
        video_link_map[vnum] = l.get('uri')

# Parse questions from text
raw_text = page.get_text('text')
lines = [line.strip() for line in raw_text.split('\n') if line.strip()]

car_hp_qs = []
i = 0
while i < len(lines):
    # Match question number "01", "02", ..., "10"
    if re.match(r'^\d{2}$', lines[i]):
        q_num_str = lines[i]
        ans_str = lines[i+1] if i+1 < len(lines) else ""
        i += 2
        q_text_lines = []
        video_num = ""
        while i < len(lines):
            if re.match(r'^\d{6}$', lines[i]):
                video_num = lines[i]
                i += 1
                break
            if re.match(r'^\d{2}$', lines[i]):
                break
            q_text_lines.append(lines[i])
            i += 1
        
        full_q_str = " ".join(q_text_lines)
        
        # Parse options from full_q_str
        # Format: "... Question stem ... (1) Opt1. (2) Opt2. (3) Opt3."
        parts = re.split(r'\s*\(([123])\)\s*', full_q_str)
        stem = parts[0].strip()
        opts = []
        if len(parts) >= 7:
            opts = [f"({parts[1]}) {parts[2].strip()}", f"({parts[3]}) {parts[4].strip()}", f"({parts[5]}) {parts[6].strip()}"]
        
        # Determine correct index from ans_str e.g. "(1)" or "(3)"
        ans_idx = 0
        if '(1)' in ans_str: ans_idx = 0
        elif '(2)' in ans_str: ans_idx = 1
        elif '(3)' in ans_str: ans_idx = 2
        
        c_ans = opts[ans_idx] if ans_idx < len(opts) else ""
        v_url = video_link_map.get(video_num, "https://reurl.cc/zQj3Ge")
        
        car_hp_qs.append({
            "id": f"CAR_HP_{q_num_str}",
            "category": "Car Hazard Perception",
            "topic": "Hazard Perception Video Scenarios",
            "question": stem,
            "options": opts,
            "correct_answer": c_ans,
            "correct_index": ans_idx,
            "explanation": f"Official Taiwan THB Hazard Perception Video #{video_num}. Defensive Driving Rule: Always anticipate potential hazards, slow down at intersections, and maintain safe following distance.",
            "video_link": v_url,
            "video_number": video_num
        })
    else:
        i += 1

print(f"Extracted {len(car_hp_qs)} Car Hazard Perception Video Questions.")
with open('car_hp_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(car_hp_qs, f, indent=2, ensure_ascii=False)
