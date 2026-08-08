import fitz
import json
import re
import os

moto_dir = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Motorcycle'
img_dir = r'assets\moto_signs'
os.makedirs(img_dir, exist_ok=True)

# Helper to build rich explanation
def make_explanation(qnum, category, question, c_ans):
    q_lower = (question + " " + c_ans).lower()
    expl = f"Official Taiwan THB Motorcycle License Exam Rule #{qnum}. "
    if 'shoulder' in q_lower:
        expl += "Cargo height on a motorcycle must NOT exceed the rider's shoulder height."
    elif '10 cm' in q_lower:
        expl += "Cargo width must NOT extend more than 10 cm beyond the outer edges of the motorcycle handlebars."
    elif '50 cm' in q_lower or '0.5' in q_lower:
        expl += "Cargo length extending beyond the rear wheel axle must NOT exceed 50 cm (0.5 meter)."
    elif '30:2' in q_lower:
        expl += "Standard adult CPR compression-to-ventilation ratio is 30 chest compressions to 2 rescue breaths."
    elif '1.0' in q_lower:
        expl += "Minimum legal motorcycle tire tread depth is 1.0 mm."
    elif '180,000' in q_lower:
        expl += "Refusing a police breath alcohol test results in an immediate NT$180,000 fine, vehicle impoundment, and license revocation."
    elif '30 meters' in q_lower:
        expl += "Riders must activate turn signals at least 30 meters prior to making a turn or lane change."
    elif '1,000' in q_lower and 'phone' in q_lower:
        expl += "Using a handheld mobile phone while riding a motorcycle carries a mandatory fine of NT$1,000."
    elif 'headlight' in q_lower:
        expl += "Motorcycles should keep headlights on during daytime and nighttime to enhance visibility and safety."
    else:
        expl += f"Correct legal answer: {c_ans}. Always adhere to official Highway Bureau safety rules."
    return expl

all_moto_qs = []

# 1. Moto Main (804 Questions)
doc_main = fitz.open(os.path.join(moto_dir, 'Motorcycle_License_Written_Test_Question_Bank_English0127.pdf'))
txt_main = ''
for p in doc_main: txt_main += '\n' + p.get_text('text')
matches_main = list(re.finditer(r'\n(\d{1,3})\s*\n\s*([123])\s*\n', txt_main))

for idx, m in enumerate(matches_main):
    qnum = int(m.group(1))
    ans_idx = int(m.group(2)) - 1
    start_pos = m.end()
    end_pos = matches_main[idx+1].start() if idx+1 < len(matches_main) else len(txt_main)
    chunk = txt_main[start_pos:end_pos].strip()
    lines = [l.strip() for l in chunk.split('\n') if l.strip() and not l.startswith('Motorcycle License') and not l.startswith('Written Test') and not l.startswith('Question Bank') and not l.startswith('Category') and not l.startswith('Correct Concepts') and not l.startswith('Proactive Yielding') and not l.startswith('Safe Driving') and not l.startswith('━') and not l.startswith('No.') and not l.startswith('Ans')]
    raw = ' '.join(lines)
    opt_parts = re.split(r'\s*\(([123])\)\s*', raw)
    stem = opt_parts[0].strip()
    options = []
    if len(opt_parts) >= 7:
        options = [
            f'({opt_parts[1]}) {opt_parts[2].strip()}',
            f'({opt_parts[3]}) {opt_parts[4].strip()}',
            f'({opt_parts[5]}) {opt_parts[6].strip()}'
        ]
    else: options = [raw]
    c_ans = options[ans_idx] if ans_idx < len(options) else f'({ans_idx+1})'
    
    all_moto_qs.append({
        'id': f'MOTO_MAIN_{qnum:04d}',
        'official_num': qnum,
        'category': 'Motorcycle Regulations - General',
        'topic': 'Official THB Motorcycle Written Exam Bank',
        'question': stem if stem else raw,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': make_explanation(qnum, 'General', stem if stem else raw, c_ans)
    })

# 2. Moto Reg MC (514 Questions)
doc_reg_mc = fitz.open(os.path.join(moto_dir, '機車法規選擇題-英文1140516.pdf'))
txt_reg_mc = ''
for p in doc_reg_mc: txt_reg_mc += '\n' + p.get_text('text')
matches_reg_mc = list(re.finditer(r'\n(\d{3})\s*\n\s*([123])\s*\n', txt_reg_mc))

for idx, m in enumerate(matches_reg_mc):
    qnum_str = m.group(1)
    ans_idx = int(m.group(2)) - 1
    start_pos = m.end()
    end_pos = matches_reg_mc[idx+1].start() if idx+1 < len(matches_reg_mc) else len(txt_reg_mc)
    chunk = txt_reg_mc[start_pos:end_pos].strip()
    lines = [l.strip() for l in chunk.split('\n') if l.strip() and not l.startswith('MOTORCYCLES regulations') and not l.startswith('Question') and not l.startswith('number')]
    raw = ' '.join(lines)
    opt_parts = re.split(r'\s*\(([123])\)\s*', raw)
    stem = opt_parts[0].strip()
    options = []
    if len(opt_parts) >= 7:
        options = [
            f'({opt_parts[1]}) {opt_parts[2].strip()}',
            f'({opt_parts[3]}) {opt_parts[4].strip()}',
            f'({opt_parts[5]}) {opt_parts[6].strip()}'
        ]
    else: options = [raw]
    c_ans = options[ans_idx] if ans_idx < len(options) else f'({ans_idx+1})'
    
    all_moto_qs.append({
        'id': f'MOTO_REG_MC_{qnum_str}',
        'official_num': int(qnum_str),
        'category': 'Motorcycle Regulations - Multiple Choice',
        'topic': 'Traffic Regulations & Fine Laws',
        'question': stem if stem else raw,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': make_explanation(int(qnum_str), 'Reg MC', stem if stem else raw, c_ans)
    })

# 3. Moto Reg TF (759 Questions)
doc_reg_tf = fitz.open(os.path.join(moto_dir, '機車法規是非題-英文1130110.pdf'))
txt_reg_tf = ''
for p in doc_reg_tf: txt_reg_tf += '\n' + p.get_text('text')
matches_reg_tf = list(re.finditer(r'\n(\d{3})\s*\n\s*([OXox])\s*\n', txt_reg_tf))

for idx, m in enumerate(matches_reg_tf):
    qnum_str = m.group(1)
    ans_char = m.group(2).upper()
    ans_idx = 0 if ans_char == 'O' else 1
    start_pos = m.end()
    end_pos = matches_reg_tf[idx+1].start() if idx+1 < len(matches_reg_tf) else len(txt_reg_tf)
    chunk = txt_reg_tf[start_pos:end_pos].strip()
    lines = [l.strip() for l in chunk.split('\n') if l.strip() and not l.startswith('MOTORCYCLES regulations') and not l.startswith('Question') and not l.startswith('number')]
    raw = ' '.join(lines)
    options = ['(1) True.', '(2) False.']
    c_ans = options[ans_idx]
    
    all_moto_qs.append({
        'id': f'MOTO_REG_TF_{qnum_str}',
        'official_num': int(qnum_str),
        'category': 'Motorcycle Regulations - True/False',
        'topic': 'Traffic Regulations & Fine Laws',
        'question': raw,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': f"Official Taiwan THB Motorcycle Regulations Rule #{qnum_str}. This statement is {'CORRECT (True)' if ans_idx==0 else 'INCORRECT (False)'}."
    })

# 4. Moto Sign MC (152 Questions) - Precision Spatial Image Extraction
doc_sign_mc = fitz.open(os.path.join(moto_dir, '機車標誌選擇題-英文-1131113.pdf'))
for pno in range(len(doc_sign_mc)):
    page = doc_sign_mc[pno]
    blocks = page.get_text('blocks')
    page_imgs = []
    for img_info in page.get_images():
        xref = img_info[0]
        for r in page.get_image_rects(xref):
            page_imgs.append((r, xref))
    page_imgs.sort(key=lambda x: x[0].y0)
    
    q_headers = []
    for b in blocks:
        txt = b[4].strip()
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        if len(lines) >= 2 and lines[0].isdigit() and lines[1] in ['1','2','3']:
            q_headers.append({'qnum': int(lines[0]), 'ans_idx': int(lines[1])-1, 'bbox': fitz.Rect(b[:4]), 'raw': txt})
    q_headers.sort(key=lambda x: x['bbox'].y0)
    
    for idx_q, qh in enumerate(q_headers):
        qnum = qh['qnum']
        ans_idx = qh['ans_idx']
        q_y0 = qh['bbox'].y0
        
        sign_img_path = None
        for img_rect, xref in page_imgs:
            if abs(img_rect.y0 - q_y0) < 45 or (img_rect.y0 >= q_y0 - 25 and img_rect.y0 <= q_y0 + 60):
                img_name = f'moto_sign_mc_{qnum:04d}.png'
                save_path = os.path.join(img_dir, img_name)
                pix = page.get_pixmap(clip=img_rect, dpi=150)
                pix.save(save_path)
                sign_img_path = f'assets/moto_signs/{img_name}'
                break
                
        # Parse options
        opt_parts = re.split(r'\s*\(([123])\)\s*', qh['raw'])
        stem = opt_parts[0].strip()
        options = []
        if len(opt_parts) >= 7:
            options = [
                f'({opt_parts[1]}) {opt_parts[2].strip()}',
                f'({opt_parts[3]}) {opt_parts[4].strip()}',
                f'({opt_parts[5]}) {opt_parts[6].strip()}'
            ]
        else: options = [qh['raw']]
        c_ans = options[ans_idx] if ans_idx < len(options) else f'({ans_idx+1})'

        all_moto_qs.append({
            'id': f'MOTO_SIGN_MC_{qnum:03d}',
            'official_num': qnum,
            'category': 'Road Signs & Signals - Multiple Choice',
            'topic': 'Traffic Signs, Markings & Signals',
            'question': stem if stem else qh['raw'],
            'options': options,
            'correct_answer': c_ans,
            'correct_index': ans_idx,
            'explanation': f"Official Taiwan THB Motorcycle Road Sign Rule #{qnum}. Correct sign identification: {c_ans}.",
            'sign_image': sign_img_path
        })

# 5. Moto Sign TF (176 Questions) - Precision Spatial Image Extraction
doc_sign_tf = fitz.open(os.path.join(moto_dir, '機車標誌是非題-英文-1131113.pdf'))
for pno in range(len(doc_sign_tf)):
    page = doc_sign_tf[pno]
    blocks = page.get_text('blocks')
    page_imgs = []
    for img_info in page.get_images():
        xref = img_info[0]
        for r in page.get_image_rects(xref):
            page_imgs.append((r, xref))
    page_imgs.sort(key=lambda x: x[0].y0)
    
    q_headers = []
    for b in blocks:
        txt = b[4].strip()
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        if len(lines) >= 2 and lines[0].isdigit() and lines[1].upper() in ['O','X']:
            q_headers.append({'qnum': int(lines[0]), 'ans_char': lines[1].upper(), 'bbox': fitz.Rect(b[:4]), 'raw': txt})
    q_headers.sort(key=lambda x: x['bbox'].y0)
    
    for idx_q, qh in enumerate(q_headers):
        qnum = qh['qnum']
        ans_idx = 0 if qh['ans_char'] == 'O' else 1
        q_y0 = qh['bbox'].y0
        
        sign_img_path = None
        for img_rect, xref in page_imgs:
            if abs(img_rect.y0 - q_y0) < 45 or (img_rect.y0 >= q_y0 - 25 and img_rect.y0 <= q_y0 + 60):
                img_name = f'moto_sign_tf_{qnum:04d}.png'
                save_path = os.path.join(img_dir, img_name)
                pix = page.get_pixmap(clip=img_rect, dpi=150)
                pix.save(save_path)
                sign_img_path = f'assets/moto_signs/{img_name}'
                break
                
        # Question text is in the right block on page
        # find block at same y0 level
        q_text = ""
        for b in blocks:
            if abs(b[1] - q_y0) < 30 and b[0] > 200:
                q_text = b[4].strip()
                break
                
        options = ['(1) True.', '(2) False.']
        c_ans = options[ans_idx]

        all_moto_qs.append({
            'id': f'MOTO_SIGN_TF_{qnum:03d}',
            'official_num': qnum,
            'category': 'Road Signs & Signals - True/False',
            'topic': 'Traffic Signs, Markings & Signals',
            'question': q_text if q_text else f"Sign #{qnum:03d} identification",
            'options': options,
            'correct_answer': c_ans,
            'correct_index': ans_idx,
            'explanation': f"Official Taiwan THB Motorcycle Road Sign True/False Rule #{qnum}. Statement for sign shown is {'CORRECT (True)' if ans_idx==0 else 'INCORRECT (False)'}.",
            'sign_image': sign_img_path
        })

# 6. Moto Hazard Perception (126 Questions)
with open('moto_hp_parsed.json', 'r', encoding='utf-8') as f:
    moto_hp_qs = json.load(f)

all_moto_qs.extend(moto_hp_qs)

with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_moto_qs, f, indent=2, ensure_ascii=False)

print(f'Successfully updated questions.json with spatial images and rich explanations ({len(all_moto_qs)} total)!')
