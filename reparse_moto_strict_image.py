import fitz
import json
import re
import os

moto_pdf = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Motorcycle\Motorcycle_License_Written_Test_Question_Bank_English0127.pdf'
moto_hp_pdf = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Motorcycle\(英語)機車危險感知影片選擇題.pdf'
img_dir = r'assets\moto_signs'
os.makedirs(img_dir, exist_ok=True)

doc_moto = fitz.open(moto_pdf)
doc_moto_hp = fitz.open(moto_hp_pdf)

def clean_text(text):
    text = text.replace("\\'", "'").replace('\\"', '"').replace("driver\\'s", "driver's")
    text = re.sub(r'—\s*\d+\s*—', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

full_txt = ''
page_positions = []
for pno in range(len(doc_moto)):
    page = doc_moto[pno]
    txt = page.get_text('text')
    page_positions.append((pno, len(full_txt)))
    full_txt += f'\n[PAGEMARKER_{pno+1}]\n' + txt

matches = list(re.finditer(r'\n(\d{1,3})\s*\n\s*([123])\s*\n', full_txt))

moto_qs = []

for idx, m in enumerate(matches):
    qnum = int(m.group(1))
    ans_idx = int(m.group(2)) - 1
    
    start_pos = m.end()
    end_pos = matches[idx+1].start() if idx+1 < len(matches) else len(full_txt)
    chunk = full_txt[start_pos:end_pos].strip()
    
    lines = [l.strip() for l in chunk.split('\n') if l.strip() and not l.startswith('Motorcycle License') and not l.startswith('Written Test') and not l.startswith('Question Bank') and not l.startswith('Category') and not l.startswith('Correct Concepts') and not l.startswith('Proactive Yielding') and not l.startswith('Safe Driving') and not l.startswith('━') and not l.startswith('No.') and not l.startswith('Ans') and 'PAGEMARKER' not in l]
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
    
    stem_lower = stem.lower()
    needs_image = any(kw in stem_lower for kw in [
        'in the picture', 'in the figure', 'shown in the picture', 'shown in the figure',
        'this sign', 'this marking', 'this signal', 'this icon', 'hand gesture', 'indicated by the arrow',
        'which of the following signs', 'which sign', 'which road marking'
    ])
    
    match_start = m.start()
    pno = 0
    for p_idx, pos in enumerate(page_positions):
        if pos[1] <= match_start: pno = pos[0]
        else: break
        
    page_obj = doc_moto[pno]
    text_blocks = page_obj.get_text('blocks')
    q_y0 = None
    q_y1 = None
    for b in text_blocks:
        btxt = b[4].strip()
        blines = [x.strip() for x in btxt.split('\n') if x.strip()]
        if len(blines) >= 1 and blines[0] == str(qnum):
            q_y0 = b[1]
            q_y1 = b[3]
            break
            
    sign_img_path = None
    if needs_image and q_y0 is not None:
        page_imgs = []
        for img_info in page_obj.get_images():
            xref = img_info[0]
            for r in page_obj.get_image_rects(xref):
                page_imgs.append((r, xref))
                
        best_xref = None
        best_rect = None
        min_dist = 9999
        for img_rect, xref in page_imgs:
            dist = min(abs(img_rect.y0 - q_y0), abs(img_rect.y0 - q_y1), abs(img_rect.y1 - q_y0))
            if dist < min_dist and dist < 120:
                min_dist = dist
                best_xref = xref
                best_rect = img_rect
                
        if best_rect is not None:
            img_name = f'moto_sign_{qnum:04d}.png'
            save_path = os.path.join(img_dir, img_name)
            pix = page_obj.get_pixmap(clip=best_rect, dpi=150)
            pix.save(save_path)
            sign_img_path = f'assets/moto_signs/{img_name}'

    category = 'Motorcycle Regulations - General'
    if qnum > 400 and qnum <= 600:
        category = 'Road Signs & Signals - Multiple Choice'
    elif qnum > 600:
        category = 'Motorcycle Regulations - Ethics & Safety'

    moto_qs.append({
        'id': f'MOTO_{qnum:04d}',
        'official_num': qnum,
        'category': category,
        'topic': 'Official THB Motorcycle Written Exam Question Bank',
        'question': stem,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': '',
        'sign_image': sign_img_path
    })

print(f'Reparsed {len(moto_qs)} Motorcycle Questions with STRICT explicit image assignment!')

# 2. Parse Motorcycle Hazard Perception PDF (120 Questions)
moto_hp_qs = []
hp_txt = ''
for pno in range(len(doc_moto_hp)):
    page = doc_moto_hp[pno]
    hp_txt += '\n' + page.get_text('text')

matches_hp = list(re.finditer(r'\n(\d{3})\s*\n\s*([123])\s*\n', hp_txt))

for idx, m in enumerate(matches_hp):
    qnum_str = m.group(1)
    ans_idx = int(m.group(2)) - 1
    start_pos = m.end()
    end_pos = matches_hp[idx+1].start() if idx+1 < len(matches_hp) else len(hp_txt)
    chunk = hp_txt[start_pos:end_pos].strip()
    
    v_match = re.search(r'(\d{4})\s*$', chunk)
    vnum = v_match.group(1) if v_match else ''
    
    lines = [l.strip() for l in chunk.split('\n') if l.strip() and not l.startswith('Motorcycle Hazard') and not l.startswith('Instructions') and not l.startswith('Question') and not l.startswith('Number') and not l.startswith('Answer') and l != vnum]
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
    vlink = f'https://space2.thb.gov.tw/d/s/18RCOJhYA7zb0ddUn5cirG3IEQPtV5q3/w0XjZBCrh6cqzzFZIhd5a-DpOcCtAxnM-ibGA2PqiOw0'

    moto_hp_qs.append({
        'id': f'MOTO_HP_{qnum_str}',
        'official_num': int(qnum_str),
        'category': 'Hazard Perception Video Scenarios',
        'topic': 'Hazard Perception Scenarios',
        'question': stem,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': '',
        'video_link': vlink,
        'video_number': vnum
    })

full_moto_bank = moto_qs + moto_hp_qs
with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(full_moto_bank, f, indent=2, ensure_ascii=False)

print(f'Saved {len(full_moto_bank)} total Motorcycle questions with strict explicit image assignment!')
