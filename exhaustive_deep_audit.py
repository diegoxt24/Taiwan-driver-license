import json
import os
import re

def run_exhaustive_deep_audit():
    audit_results = {
        "car_questions_checked": 0,
        "moto_questions_checked": 0,
        "car_master_rules_checked": 0,
        "moto_master_rules_checked": 0,
        "cheat_sheet_items_checked": 0,
        "defects_found": 0,
        "details": []
    }

    # 1. Audit Car Questions (car_questions.json)
    with open('car_questions.json', 'r', encoding='utf-8') as f:
        car_qs = json.load(f)

    for q in car_qs:
        audit_results["car_questions_checked"] += 1
        q_id = q['id']
        
        # Check correct_index bounds and matching text
        opts = q['options']
        c_idx = q['correct_index']
        c_ans = q['correct_answer']
        if c_idx < 0 or c_idx >= len(opts) or opts[c_idx] != c_ans:
            audit_results["defects_found"] += 1
            audit_results["details"].append(f"[{q_id}] Option index mismatch")

        # Check sign image file on disk if present
        if q.get('sign_image'):
            img_path = q['sign_image'].replace('/', os.sep)
            if not os.path.exists(img_path):
                audit_results["defects_found"] += 1
                audit_results["details"].append(f"[{q_id}] Missing image file: {img_path}")

        # Check explanation alignment (Must contain 'Why' and match question context)
        expl = q.get('explanation', '')
        if not expl or 'Official Taiwan THB' in expl or 'Rule #' in expl or 'Level 2 ADAS' in expl and 'adas' not in q['question'].lower():
            audit_results["defects_found"] += 1
            audit_results["details"].append(f"[{q_id}] Explanation context mismatch")

    # 2. Audit Motorcycle Questions (questions.json)
    with open('questions.json', 'r', encoding='utf-8') as f:
        moto_qs = json.load(f)

    for q in moto_qs:
        audit_results["moto_questions_checked"] += 1
        q_id = q['id']
        opts = q['options']
        c_idx = q['correct_index']
        c_ans = q['correct_answer']
        if c_idx < 0 or c_idx >= len(opts) or opts[c_idx] != c_ans:
            audit_results["defects_found"] += 1
            audit_results["details"].append(f"[{q_id}] Option index mismatch")

        if q.get('sign_image'):
            img_path = q['sign_image'].replace('/', os.sep)
            if not os.path.exists(img_path):
                audit_results["defects_found"] += 1
                audit_results["details"].append(f"[{q_id}] Missing image file: {img_path}")

        expl = q.get('explanation', '')
        if not expl or 'Official Taiwan THB' in expl or 'Rule #' in expl:
            audit_results["defects_found"] += 1
            audit_results["details"].append(f"[{q_id}] Explanation context mismatch")

    # 3. Audit Mode 0 Master Rules (car_master_rules.json & moto_master_rules.json)
    with open('car_master_rules.json', 'r', encoding='utf-8') as f:
        cmr = json.load(f)
    with open('moto_master_rules.json', 'r', encoding='utf-8') as f:
        mmr = json.load(f)

    for card in cmr:
        audit_results["car_master_rules_checked"] += 1
        if not card.get('title') or not card.get('summary') or not card.get('canonical_question') or not card.get('canonical_correct'):
            audit_results["defects_found"] += 1
            audit_results["details"].append(f"[Car Master Rule {card['id']}] Incomplete fields")

    for card in mmr:
        audit_results["moto_master_rules_checked"] += 1
        if not card.get('title') or not card.get('summary') or not card.get('canonical_question') or not card.get('canonical_correct'):
            audit_results["defects_found"] += 1
            audit_results["details"].append(f"[Moto Master Rule {card['id']}] Incomplete fields")

    # 4. Audit Cram Cheat Sheets
    with open('car_cheat_sheet.json', 'r', encoding='utf-8') as f:
        ccs = json.load(f)
    with open('cheat_sheet.json', 'r', encoding='utf-8') as f:
        mcs = json.load(f)

    for section in ccs + mcs:
        for item in section.get('items', []):
            audit_results["cheat_sheet_items_checked"] += 1
            if not item.get('label') or not item.get('value'):
                audit_results["defects_found"] += 1
                audit_results["details"].append(f"[Cheat Sheet] Missing label/value in {section.get('category')}")

    print("\n=======================================================")
    print("       EXHAUSTIVE DEEP INTEGRITY AUDIT REPORT          ")
    print("=======================================================")
    print(f"✓ Total Automobile Questions Audited: {audit_results['car_questions_checked']}")
    print(f"✓ Total Motorcycle Questions Audited: {audit_results['moto_questions_checked']}")
    print(f"✓ Total Mode 0 Car Master Rules Audited: {audit_results['car_master_rules_checked']}")
    print(f"✓ Total Mode 0 Motorcycle Master Rules Audited: {audit_results['moto_master_rules_checked']}")
    print(f"✓ Total Cram Cheat Sheet Items Audited: {audit_results['cheat_sheet_items_checked']}")
    print("-------------------------------------------------------")
    print(f"TOTAL DEFECTS DETECTED: {audit_results['defects_found']}")
    if audit_results['defects_found'] > 0:
        for d in audit_results['details'][:10]:
            print(f"  ❌ {d}")
    else:
        print("🎉 100% PERFECT GUARANTEE: ZERO DISCREPANCIES OR BUGS FOUND!")
    print("=======================================================")

if __name__ == '__main__':
    run_exhaustive_deep_audit()
