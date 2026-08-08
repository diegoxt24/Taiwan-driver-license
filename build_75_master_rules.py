import json

with open('car_questions.json', 'r', encoding='utf-8') as f:
    car_qs = json.load(f)

with open('questions.json', 'r', encoding='utf-8') as f:
    moto_qs = json.load(f)

from generate_75_master_rules import rule_defs_75

def get_exact_canonical(qlist, keywords):
    for q in qlist:
        q_text = (q['question'] + " " + " ".join(q['options'])).lower()
        if all(k in q_text for k in keywords):
            return q
    for q in qlist:
        q_text = (q['question'] + " " + " ".join(q['options'])).lower()
        if any(k in q_text for k in keywords):
            return q
    return qlist[0]

def build_master_rules(qlist, prefix):
    cards = []
    matched_q_set = set()
    
    for r in rule_defs_75:
        card_id = f"{prefix}_{r['id']}"
        kw_list = r.get('kw', [])
        matched = [q for q in qlist if any(k in (q['question'] + ' ' + ' '.join(q['options']) + ' ' + q.get('explanation','')).lower() for k in kw_list)]
        
        if not matched:
            matched = [qlist[0]]
            
        for q in matched:
            matched_q_set.add(q['id'])
            
        canonical = get_exact_canonical(matched, kw_list)
        
        cards.append({
            "id": card_id,
            "title": r["title"],
            "summary": r["summary"],
            "key_fact": r["title"],
            "diagram": r["diagram"],
            "canonical_question": canonical["question"],
            "canonical_options": canonical["options"],
            "canonical_correct": canonical["correct_answer"],
            "canonical_correct_index": canonical["correct_index"],
            "matched_question_count": len(matched),
            "matched_question_ids": [q["id"] for q in matched]
        })

    unmatched = [q for q in qlist if q['id'] not in matched_q_set]
    if unmatched:
        cards.append({
            "id": f"{prefix}_R76",
            "title": "76. General Traffic Safety Regulations & Ethics",
            "summary": "General road safety regulations, ethical driving habits, and situational hazard awareness.",
            "key_fact": "General Traffic Safety Rules",
            "diagram": "right_of_way",
            "canonical_question": unmatched[0]["question"],
            "canonical_options": unmatched[0]["options"],
            "canonical_correct": unmatched[0]["correct_answer"],
            "canonical_correct_index": unmatched[0]["correct_index"],
            "matched_question_count": len(unmatched),
            "matched_question_ids": [q["id"] for q in unmatched]
        })
    return cards

car_cards = build_master_rules(car_qs, 'C')
moto_cards = build_master_rules(moto_qs, 'M')

with open('car_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(car_cards, f, indent=2, ensure_ascii=False)

with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(moto_cards, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(car_cards)} Car Master Rules and {len(moto_cards)} Motorcycle Master Rules!")
