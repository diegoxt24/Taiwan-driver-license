import json

def verify_mode1_mode2_dedup_and_rendering():
    report = []
    
    # 1. Load Datasets
    with open('car_questions.json', 'r', encoding='utf-8') as f:
        car_qs = json.load(f)
        
    with open('questions.json', 'r', encoding='utf-8') as f:
        moto_qs = json.load(f)

    # 2. Check for Duplicates in Car Bank
    seen_car_stems = {}
    car_dups = []
    unique_car_qs = []
    for q in car_qs:
        stem_norm = q['question'].strip().lower()
        if len(stem_norm) > 15 and stem_norm in seen_car_stems:
            car_dups.append((q['id'], seen_car_stems[stem_norm]))
        else:
            seen_car_stems[stem_norm] = q['id']
            unique_car_qs.append(q)

    # 3. Check for Duplicates in Motorcycle Bank
    seen_moto_stems = {}
    moto_dups = []
    unique_moto_qs = []
    for q in moto_qs:
        stem_norm = q['question'].strip().lower()
        if len(stem_norm) > 15 and stem_norm in seen_moto_stems:
            moto_dups.append((q['id'], seen_moto_stems[stem_norm]))
        else:
            seen_moto_stems[stem_norm] = q['id']
            unique_moto_qs.append(q)

    report.append(f"Car Bank: {len(car_qs)} total -> {len(unique_car_qs)} unique questions ({len(car_dups)} duplicate stems removed).")
    report.append(f"Motorcycle Bank: {len(moto_qs)} total -> {len(unique_moto_qs)} unique questions ({len(moto_dups)} duplicate stems removed).")

    # Save deduplicated clean datasets
    with open('car_questions.json', 'w', encoding='utf-8') as f:
        json.dump(unique_car_qs, f, indent=2, ensure_ascii=False)

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(unique_moto_qs, f, indent=2, ensure_ascii=False)

    # 4. Verify Mode 1 and Mode 2 rendering logic for every single question
    rendering_issues = []
    for bank_name, qset in [("Car", unique_car_qs), ("Motorcycle", unique_moto_qs)]:
        for q in qset:
            opts = q.get('options', [])
            idx = q.get('correct_index', -1)
            c_ans = q.get('correct_answer', '')
            
            # Mode 1 check: correct_index must be valid and correct_answer must equal option[correct_index]
            if idx < 0 or idx >= len(opts):
                rendering_issues.append((q['id'], "Mode 1/2 Error: index out of bounds", idx, len(opts)))
            elif opts[idx] != c_ans:
                rendering_issues.append((q['id'], "Mode 1/2 Mismatch: option[idx] != correct_answer", opts[idx], c_ans))

            # Text HTML escaping check
            if '<script>' in q['question'] or 'undefined' in q['question']:
                rendering_issues.append((q['id'], "Text Error: invalid characters in question"))

    report.append(f"Mode 1 & Mode 2 Rendering Verification: {len(rendering_issues)} errors found.")

    print("\n=======================================================")
    print("   MODE 1 & MODE 2 DE-DUPLICATION & VERIFICATION AUDIT ")
    print("=======================================================")
    for r in report:
        print(r)
    print("=======================================================")

if __name__ == '__main__':
    verify_mode1_mode2_dedup_and_rendering()
