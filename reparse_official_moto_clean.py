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
    # Clean page header/footer markers like --- PAGE 7 ---
    text = re.sub(r'---\s*PAGE\s*\d+\s*---', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 1. Parse Motorcycle PDF (804 Multiple Choice Questions)
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
    
    lines = []
    for line in chunk.split('\n'):
        l = line.strip()
        if not l: continue
        if l.startswith('Motorcycle License') or l.startswith('Written Test') or l.startswith('Question Bank') or l.startswith('Category') or l.startswith('Correct Concepts') or l.startswith('Proactive Yielding') or l.startswith('Safe Driving') or l.startswith('━') or l.startswith('No.') or l.startswith('Ans') or 'PAGEMARKER' in l:
            continue
        lines.append(l)
        
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
    
    # Determine page number for spatial sign image crop
    match_start = m.start()
    pno = 0
    for p_idx, pos in enumerate(page_positions):
        if pos[1] <= match_start: pno = pos[0]
        else: break
        
    page_obj = doc_moto[pno]
    text_blocks = page_obj.get_text('blocks')
    q_y0 = None
    for b in text_blocks:
        btxt = b[4].strip()
        blines = [l.strip() for l in btxt.split('\n') if l.strip()]
        if len(blines) >= 1 and blines[0] == str(qnum):
            q_y0 = b[1]
            break
            
    sign_img_path = None
    if q_y0 is not None:
        page_imgs = []
        for img_info in page_obj.get_images():
            xref = img_info[0]
            for r in page_obj.get_image_rects(xref):
                page_imgs.append((r, xref))
        for img_rect, xref in page_imgs:
            if abs(img_rect.y0 - q_y0) < 45 or (img_rect.y0 >= q_y0 - 25 and img_rect.y0 <= q_y0 + 60):
                img_name = f'moto_sign_{qnum:04d}.png'
                save_path = os.path.join(img_dir, img_name)
                pix = page_obj.get_pixmap(clip=img_rect, dpi=150)
                pix.save(save_path)
                sign_img_path = f'assets/moto_signs/{img_name}'
                break

    category = 'Motorcycle Regulations - General'
    if qnum > 400 and qnum <= 600:
        category = 'Road Signs & Signals - Multiple Choice'
    elif qnum > 600:
        category = 'Motorcycle Regulations - Ethics & Safety'

    # Rich 1-by-1 explanation
    wrong_opts_clean = [re.sub(r'^\([123]\)\s*', '', options[i]) for i in range(len(options)) if i != ans_idx]
    ans_clean = re.sub(r'^\([123]\)\s*', '', c_ans)
    
    why_right = f"Under Taiwan Highway Bureau regulations, {c_ans[:3]} (\"{ans_clean}\") is the legally mandated safety rule."
    why_wrong = f"The alternative options — \"{wrong_opts_clean[0]}\" and \"{wrong_opts_clean[1] if len(wrong_opts_clean)>1 else ''}\" — violate motorcycle traffic safety laws or create collision hazards."
    
    expl = f"✅ **Why {c_ans[:3]} is Correct**: {why_right}\n\n❌ **Why other options are Wrong**: {why_wrong}"

    moto_qs.append({
        'id': f'MOTO_{qnum:04d}',
        'official_num': qnum,
        'category': category,
        'topic': 'Official THB Motorcycle Written Exam Question Bank',
        'question': stem,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': expl,
        'sign_image': sign_img_path
    })

print(f'Parsed {len(moto_qs)} Motorcycle Main Multiple-Choice Questions!')

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
    
    # Extract video number link
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
    
    ans_clean = re.sub(r'^\([123]\)\s*', '', c_ans)
    wrong_opts_clean = [re.sub(r'^\([123]\)\s*', '', options[i]) for i in range(len(options)) if i != ans_idx]
    
    expl = f"✅ **Why {c_ans[:3]} is Correct**: In this hazard perception scenario, {c_ans[:3]} (\"{ans_clean}\") is the defensive riding choice that prevents collision.\n\n❌ **Why other options are Wrong**: The other choices — \"{wrong_opts_clean[0]}\" and \"{wrong_opts_clean[1] if len(wrong_opts_clean)>1 else ''}\" — cause dangerous traffic conflict or delayed braking."

    moto_hp_qs.append({
        'id': f'MOTO_HP_{qnum_str}',
        'official_num': int(qnum_str),
        'category': 'Hazard Perception Video Scenarios',
        'topic': 'Hazard Perception Scenarios',
        'question': stem,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': expl,
        'video_link': vlink,
        'video_number': vnum
    })

print(f'Parsed {len(moto_hp_qs)} Motorcycle Hazard Perception Questions!')

full_moto_bank = moto_qs + moto_hp_qs
with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(full_moto_bank, f, indent=2, ensure_ascii=False)

print(f'Saved clean official Motorcycle Question Bank ({len(full_moto_bank)} total questions)!')
