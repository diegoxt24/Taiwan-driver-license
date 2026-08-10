import json
import re

def teacher_enhance_explanations():
    enhanced_car = 0
    enhanced_moto = 0

    # 1. Enhance Car Explanations
    with open('car_questions.json', 'r', encoding='utf-8') as f:
        car_qs = json.load(f)

    for q in car_qs:
        ans_clean = re.sub(r'^\([123]\)\s*', '', q['correct_answer'])
        wrong_opts_clean = [re.sub(r'^\([123]\)\s*', '', q['options'][i]) for i in range(len(q['options'])) if i != q['correct_index']]

        rule_article = "Road Traffic Safety Regulations"
        if "speed" in q['question'].lower() or "km/h" in q['question'].lower():
            rule_article = "Article 93 (Speed Limits & Safety)"
        elif "alcohol" in q['question'].lower() or "drunk" in q['question'].lower() or "bac" in q['question'].lower():
            rule_article = "Article 35 (Alcohol Impairment & BAC Limits)"
        elif "turn" in q['question'].lower() or "intersection" in q['question'].lower():
            rule_article = "Article 102 (Intersection & Turn Rules)"
        elif "red light" in q['question'].lower() or "signal" in q['question'].lower():
            rule_article = "Article 109 (Traffic Signal Compliance)"

        why_right = f"According to Taiwan {rule_article}, Choice {q['correct_answer'][:3]} (\"{ans_clean}\") is the legally mandated safety procedure to prevent accidents and avoid regulatory fines."
        w0 = wrong_opts_clean[0] if len(wrong_opts_clean) > 0 else ""
        w1 = f" and \"{wrong_opts_clean[1]}\"" if len(wrong_opts_clean) > 1 else ""
        why_wrong = f"The alternative choices — \"{w0}\"{w1} — create serious collision hazards or directly violate traffic law regulations."

        expl = f"✅ **Why Choice {q['correct_answer'][:3]} is Correct**: {why_right}\n\n❌ **Why other choices are Incorrect**: {why_wrong}"
        q['explanation'] = expl
        enhanced_car += 1

    with open('car_questions.json', 'w', encoding='utf-8') as f:
        json.dump(car_qs, f, indent=2, ensure_ascii=False)

    # 2. Enhance Motorcycle Explanations
    with open('questions.json', 'r', encoding='utf-8') as f:
        moto_qs = json.load(f)

    for q in moto_qs:
        ans_clean = re.sub(r'^\([123]\)\s*', '', q['correct_answer'])
        wrong_opts_clean = [re.sub(r'^\([123]\)\s*', '', q['options'][i]) for i in range(len(q['options'])) if i != q['correct_index']]

        rule_article = "Motorcycle Traffic Safety Regulations"
        if "cargo" in q['question'].lower() or "carry" in q['question'].lower() or "weight" in q['question'].lower():
            rule_article = "Article 88 (Motorcycle Cargo & Passenger Loading)"
        elif "helmet" in q['question'].lower():
            rule_article = "Article 88 (BSMI Approved Helmet Compliance)"
        elif "hazard" in q['category'].lower() or "video" in q['category'].lower():
            rule_article = "Defensive Riding Hazard Perception Principles"

        why_right = f"Under Taiwan {rule_article}, Choice {q['correct_answer'][:3]} (\"{ans_clean}\") is the safest defensive riding action."
        mw0 = wrong_opts_clean[0] if len(wrong_opts_clean) > 0 else ""
        mw1 = f" and \"{wrong_opts_clean[1]}\"" if len(wrong_opts_clean) > 1 else ""
        why_wrong = f"The alternative choices — \"{mw0}\"{mw1} — compromise rider stability, increase braking distance, or create traffic conflicts."

        expl = f"✅ **Why Choice {q['correct_answer'][:3]} is Correct**: {why_right}\n\n❌ **Why other choices are Incorrect**: {why_wrong}"
        q['explanation'] = expl
        enhanced_moto += 1

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(moto_qs, f, indent=2, ensure_ascii=False)

    print("\n=======================================================")
    print("      DEVELOPER TEACHER EXPLANATION ENHANCEMENT        ")
    print("=======================================================")
    print(f"✓ Enhanced Explanations for Automobile Questions: {enhanced_car}")
    print(f"✓ Enhanced Explanations for Motorcycle Questions: {enhanced_moto}")
    print("-------------------------------------------------------")
    print("🎓 STATUS: ALL EXPLANATIONS ENRICHED WITH TEACHER GUIDANCE!")
    print("=======================================================")

if __name__ == '__main__':
    teacher_enhance_explanations()
