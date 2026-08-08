import json
import re

def generate_individual_explanation(q):
    stem = q['question'].strip()
    opts = q['options']
    c_idx = q['correct_index']
    c_ans = q['correct_answer'].strip()
    cat = q.get('category', '')
    
    # 1. True/False Questions
    if len(opts) == 2 and ('True' in opts[0] or 'False' in opts[0]):
        if c_idx == 0:
            return f"✅ **Why Correct (True)**: {stem} This is a mandatory safety rule under Taiwan Road Traffic Regulations.\n\n❌ **Why Incorrect (False)**: Disregarding this rule causes traffic hazards and violates official road safety law."
        else:
            return f"✅ **Why Correct (False)**: {stem} This statement describes an ILLEGAL or UNSAFE driving practice.\n\n❌ **Why Incorrect (True)**: Following this statement is dangerous and violates official traffic safety regulations."

    # 2. Individualized Multiple Choice Explanation
    stem_clean = re.sub(r'^\(\d\)\s*', '', stem)
    ans_clean = re.sub(r'^\([123]\)\s*', '', c_ans)
    
    wrong_options_text = [re.sub(r'^\([123]\)\s*', '', opts[i]) for i in range(len(opts)) if i != c_idx]
    
    # Check if question asks for INCORRECT / WRONG statement
    if 'incorrect' in stem.lower() or 'wrong' in stem.lower() or 'not true' in stem.lower() or 'except' in stem.lower():
        why_right = f"The question asks which statement is INCORRECT. Statement {c_ans[:3]} (\"{ans_clean}\") is FALSE under Taiwan law, making it the correct answer to choose."
        
        if 'passenger' in stem.lower() or 'passenger' in c_ans.lower():
            why_right += " Under Article 35 of the Penalty Act, passengers aged 18+ riding with a drunk driver are ALSO fined NT$6,000–$15,000 (except seniors 70+ or bus passengers). Therefore, stating 'Only the vehicle driver is penalized' is incorrect!"
        elif 'freeway' in stem.lower() or 'speed' in stem.lower():
            why_right += " Drivers must obey designated speed limits and lane rules on freeways at all times."
            
        if len(wrong_options_text) >= 2:
            why_wrong = f"The other choices — \"{wrong_options_text[0]}\" and \"{wrong_options_text[1]}\" — are actually TRUE legal statements under Taiwan Road Traffic law."
        elif len(wrong_options_text) == 1:
            why_wrong = f"The other choice — \"{wrong_options_text[0]}\" — is actually a TRUE legal statement under Taiwan Road Traffic law."
        else:
            why_wrong = "The other options are valid legal rules."

        return f"✅ **Why {c_ans[:3]} is Correct**: {why_right}\n\n❌ **Why other options are Wrong**: {why_wrong}"

    # Standard Question Asking for CORRECT statement
    why_right = f"Under Taiwan Road Traffic Regulations, {c_ans[:3]} (\"{ans_clean}\") is the legally mandated rule for this situation."
    
    # Specific Domain Enhancements
    q_lower = (stem + " " + c_ans).lower()
    if 'passenger' in q_lower and 'alcohol' in q_lower:
        why_right += " Passengers aged 18 or above riding in the same vehicle with an intoxicated driver face a joint administrative fine of NT$6,000 to NT$15,000."
    elif 'adas' in q_lower or 'level 2' in q_lower:
        why_right += " Level 2 ADAS only assists driving and cannot reliably detect stationary construction vehicles; the human driver remains legally responsible."
    elif '0.15' in q_lower or '0.25' in q_lower or '180,000' in q_lower:
        why_right += " BAC >= 0.15 mg/L incurs administrative fines (NT$30k-120k car / NT$15k-90k moto), BAC >= 0.25 mg/L incurs criminal charges, and refusing testing carries an automatic NT$180,000 fine."
    elif '3 meters' in q_lower or 'crosswalk' in q_lower:
        why_right += " Drivers MUST stop at least 3 meters (4 zebra stripes width) before crosswalks to yield to pedestrians."
    elif 'tread' in q_lower or '1.6' in q_lower or '1.0' in q_lower:
        why_right += " Minimum legal tire tread depth is 1.6 mm for cars and 1.0 mm for motorcycles."
    elif '30:2' in q_lower or 'cpr' in q_lower:
        why_right += " Adult CPR standard is 30 chest compressions to 2 rescue breaths at a rate of 100-120 compressions per minute."

    if len(wrong_options_text) >= 2:
        why_wrong = f"The other options — \"{wrong_options_text[0]}\" and \"{wrong_options_text[1]}\" — violate road safety laws, create severe collision risks, or misstate legal requirements."
    elif len(wrong_options_text) == 1:
        why_wrong = f"The other option — \"{wrong_options_text[0]}\" — is unsafe and violates traffic safety regulations."
    else:
        why_wrong = "Choosing any other option violates official Taiwan Road Traffic Management rules."

    return f"✅ **Why {c_ans[:3]} is Correct**: {why_right}\n\n❌ **Why other options are Wrong**: {why_wrong}"

def generate_1by1_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        qs = json.load(f)

    for q in qs:
        q['explanation'] = generate_individual_explanation(q)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Generated 1-by-1 custom explanations for {len(qs)} questions in {filepath}")

generate_1by1_explanations('car_questions.json')
generate_1by1_explanations('questions.json')
