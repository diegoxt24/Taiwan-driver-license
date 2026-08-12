import fitz
import json
import re
import os

car_pdf = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Car questions\汽車筆試題庫_英文完整版_115年_含圖示_1090題.pdf'
img_dir = r'assets\car_signs'
os.makedirs(img_dir, exist_ok=True)

doc_car = fitz.open(car_pdf)

def clean_text(text):
    text = text.replace("\\'", "'").replace('\\"', '"').replace("driver\\'s", "driver's")
    text = re.sub(r'—\s*\d+\s*—', '', text)
    text = re.sub(r'Automobile Written Exam Question Bank.* Edition', '', text)
    text = re.sub(r'Section \d+.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'SECTION \d+.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

full_txt = ''
page_positions = []
for pno in range(len(doc_car)):
    page = doc_car[pno]
    txt = page.get_text('text')
    page_positions.append((pno, len(full_txt)))
    full_txt += f'\n[PAGEMARKER_{pno+1}]\n' + txt

matches = list(re.finditer(r'\n(\d{1,4})\s*\n\s*\(([123])\)\s*\n', full_txt))

car_qs = []

for idx, m in enumerate(matches):
    qnum = int(m.group(1))
    ans_idx = int(m.group(2)) - 1
    
    start_pos = m.end()
    end_pos = matches[idx+1].start() if idx+1 < len(matches) else len(full_txt)
    chunk = full_txt[start_pos:end_pos].strip()
    
    lines = [l.strip() for l in chunk.split('\n') if l.strip() and not l.startswith('Automobile Written') and not l.startswith('—') and not l.startswith('No.') and not l.startswith('Ans') and 'PAGEMARKER' not in l and not l.startswith('Section') and not l.startswith('SECTION')]
    raw_content = ' '.join(lines)
    opt_parts = re.split(r'\s*\(([123])\)\s*', raw_content)
    stem = clean_text(opt_parts[0])
    options = []
    if len(opt_parts) >= 7:
        options = [
            f'({opt_parts[1]}) {clean_text(opt_parts[2])}',
            f'({opt_parts[3]}) {clean_text(opt_parts[4])}',
            f'({opt_parts[5]}) {clean_text(opt_parts[6])}'
        ]
    else:
        options = [clean_text(raw_content)]
        
    c_ans = options[ans_idx] if ans_idx < len(options) else f'({ans_idx+1})'
    
    match_start = m.start()
    pno = 0
    for p_idx, pos in enumerate(page_positions):
        if pos[1] <= match_start: pno = pos[0]
        else: break
        
    page_obj = doc_car[pno]
    text_blocks = page_obj.get_text('blocks')
    
    q_y0 = None
    q_y1 = None
    for b in text_blocks:
        btxt = b[4].strip()
        blines = [x.strip() for x in btxt.split('\n') if x.strip()]
        if len(blines) >= 1 and (blines[0] == str(qnum) or btxt.startswith(f'{qnum}\n') or btxt.startswith(f'{qnum} ')):
            q_y0 = b[1]
            q_y1 = b[3]
            break
            
    sign_img_path = None
    if q_y0 is not None:
        page_imgs = []
        for img_info in page_obj.get_images():
            xref = img_info[0]
            for r in page_obj.get_image_rects(xref):
                page_imgs.append((r, xref))
                
        best_xref = None
        best_rect = None
        min_dist = 9999
        for img_rect, xref in page_imgs:
            # Check vertical distance to question text
            dist = min(abs(img_rect.y0 - q_y0), abs(img_rect.y0 - q_y1), abs(img_rect.y1 - q_y0))
            if dist < min_dist and dist < 65:
                min_dist = dist
                best_xref = xref
                best_rect = img_rect
                
        if best_rect is not None:
            img_name = f'car_sign_{qnum:04d}.png'
            save_path = os.path.join(img_dir, img_name)
            pix = page_obj.get_pixmap(clip=best_rect, dpi=150)
            pix.save(save_path)
            sign_img_path = f'assets/car_signs/{img_name}'

    category = 'Car Regulations - General'
    if qnum > 400 and qnum <= 650:
        category = 'Road Signs & Signals - Warnings & Rules'
    elif qnum > 650:
        category = 'Car Regulations - Ethics & Misconduct'

    car_qs.append({
        'id': f'CAR_{qnum:04d}',
        'official_num': qnum,
        'category': category,
        'topic': 'Official THB 115 Automobile Exam Question Bank',
        'question': stem,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': '',
        'sign_image': sign_img_path
    })

with open('car_questions.json', 'w', encoding='utf-8') as f:
    json.dump(car_qs, f, indent=2, ensure_ascii=False)

print(f'Reparsed {len(car_qs)} Car Questions!')
