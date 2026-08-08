import fitz
import json
import re
import os

pdf_path = r'C:\Users\User\Documents\GitHub\Taiwan driver license\Documentos oficiales\Car questions\汽車筆試題庫_英文完整版_115年_含圖示_1090題.pdf'
doc = fitz.open(pdf_path)
img_dir = r'assets\car_signs'
os.makedirs(img_dir, exist_ok=True)

# Build full text with page markers
full_txt = ''
page_positions = []
for pno in range(len(doc)):
    page = doc[pno]
    txt = page.get_text('text')
    page_positions.append((pno, len(full_txt)))
    full_txt += f'\n--- PAGE {pno+1} ---\n' + txt

matches = list(re.finditer(r'\n(\d{1,4})\s*\n\s*\(([123])\)', full_txt))

questions = []

for idx, m in enumerate(matches):
    qnum = int(m.group(1))
    ans_idx = int(m.group(2)) - 1
    
    start_pos = m.end()
    end_pos = matches[idx+1].start() if idx+1 < len(matches) else len(full_txt)
    
    chunk = full_txt[start_pos:end_pos].strip()
    
    # Clean chunk from header/footer garbage
    lines = []
    for line in chunk.split('\n'):
        l = line.strip()
        if not l: continue
        if l.startswith('Automobile Written Exam') or l.startswith('—') or l.startswith('SECTION') or l == 'No.' or l == 'Ans' or l == 'Question' or l.startswith('Section 3'):
            continue
        lines.append(l)
    
    raw_content = ' '.join(lines)
    
    # Split stem and options (1) ... (2) ... (3) ...
    opt_split = re.split(r'\s*\(([123])\)\s*', raw_content)
    stem = opt_split[0].strip()
    options = []
    if len(opt_split) >= 7:
        options = [
            f'({opt_split[1]}) {opt_split[2].strip()}',
            f'({opt_split[3]}) {opt_split[4].strip()}',
            f'({opt_split[5]}) {opt_split[6].strip()}'
        ]
    elif 'True' in raw_content or 'False' in raw_content:
        options = ['(1) True.', '(2) False.']
        if not stem: stem = raw_content
    else:
        options = [raw_content]
    
    c_ans = options[ans_idx] if ans_idx < len(options) else f'({ans_idx+1})'
    
    # Determine page number for cropped image check
    match_start = m.start()
    pno = 0
    for p_idx, pos in enumerate(page_positions):
        if pos[1] <= match_start:
            pno = pos[0]
        else:
            break
            
    # SPATIAL MATCHING FOR CAR SIGNS:
    page_obj = doc[pno]
    text_blocks = page_obj.get_text('blocks')
    
    # Find question header bounding box y0 on page
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
            rects = page_obj.get_image_rects(xref)
            for r in rects:
                page_imgs.append((r, xref))
                
        # Find image whose vertical range matches this question header (y0 difference < 40)
        for img_rect, xref in page_imgs:
            if abs(img_rect.y0 - q_y0) < 40 or (img_rect.y0 >= q_y0 - 25 and img_rect.y0 <= q_y0 + 60):
                img_name = f'car_sign_{qnum:04d}.png'
                save_path = os.path.join(img_dir, img_name)
                pix = page_obj.get_pixmap(clip=img_rect, dpi=150)
                pix.save(save_path)
                sign_img_path = f'assets/car_signs/{img_name}'
                break

    # Categorization
    category = 'Car Regulations - Ethics & Misconduct'
    if qnum > 33 and qnum <= 53:
        category = 'Car Regulations - Drunk Driving & Fines'
    elif qnum > 53 and qnum <= 102:
        category = 'Road Signs & Signals - Warnings & Regulatory'
    elif qnum > 102 and qnum <= 350:
        category = 'Road Signs & Signals - Markings & Signs'
    elif qnum > 350 and qnum <= 654:
        category = 'Car Regulations - Proactive Yielding'
    elif qnum > 654:
        category = 'Car Regulations - Safe Driving Skills'

    # Rich Explanation Generation based on specific answer & topic
    expl = f"Official Taiwan THB Automobile Driver Examination Rule #{qnum}. "
    if 'shoulder' in c_ans.lower() or 'shoulder' in stem.lower():
        expl += "Cargo height on motorcycles must not exceed the rider's shoulder height."
    elif '50 cm' in c_ans or '0.5' in c_ans:
        expl += "Cargo extending beyond the rear wheel axle must not exceed 50 cm (0.5 meter)."
    elif '10 cm' in c_ans:
        expl += "Cargo width must not exceed 10 cm beyond the outer edges of the handlebars."
    elif '30:2' in c_ans:
        expl += "CPR standard compression-to-ventilation ratio for adults is 30 chest compressions to 2 rescue breaths."
    elif '1.6' in c_ans or '1.0' in c_ans:
        expl += "Minimum legal tire tread depth is 1.6mm for cars and 1.0mm for motorcycles."
    elif '180,000' in c_ans:
        expl += "Refusing a breath alcohol test incurs an immediate NT$180,000 administrative fine, license revocation, and vehicle impoundment."
    elif '30 meters' in c_ans:
        expl += "Turn signals must be activated at least 30 meters prior to turning or changing lanes."
    elif '3 meters' in c_ans:
        expl += "Vehicles must stop at least 3 meters (approx. 4 zebra stripes) before crosswalks to yield to pedestrians."
    else:
        expl += f"The correct legal rule is: {c_ans}. Always follow official Taiwan Road Traffic Management Regulations."

    questions.append({
        'id': f'CAR_{qnum:04d}',
        'official_num': qnum,
        'category': category,
        'topic': 'Official THB 115 Automobile Exam Question Bank',
        'question': stem if stem else raw_content,
        'options': options,
        'correct_answer': c_ans,
        'correct_index': ans_idx,
        'explanation': expl,
        'sign_image': sign_img_path
    })

print(f'Total Car Questions parsed with SPATIAL IMAGE MATCHING: {len(questions)}')

# Merge Hazard perception into car_questions.json
with open('car_hp_parsed.json', 'r', encoding='utf-8') as f:
    chp = json.load(f)

full_car_bank = questions + chp
with open('car_questions.json', 'w', encoding='utf-8') as f:
    json.dump(full_car_bank, f, indent=2, ensure_ascii=False)

print('Saved spatial accurate car_questions.json!')
