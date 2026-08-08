import json

def generate_educational_explanation(q):
    stem = q['question']
    opts = q['options']
    c_idx = q['correct_index']
    c_ans = q['correct_answer']
    
    # Identify wrong options
    wrong_opts = [opts[i] for i in range(len(opts)) if i != c_idx]
    
    # 1. True/False questions
    if len(opts) == 2 and ('True' in opts[0] or 'False' in opts[0]):
        if c_idx == 0:
            return f"✅ **Correct (True)**: This statement accurately reflects Taiwan Highway Bureau traffic laws.\n❌ **Incorrect (False)**: Disregarding this safety standard creates traffic hazards and violates road safety regulations."
        else:
            return f"✅ **Correct (False)**: This statement is ILLEGAL or unsafe under traffic regulations.\n❌ **Incorrect (True)**: Believing this statement is correct is dangerous; drivers/riders must obey standard traffic safety laws."

    # 2. Multiple Choice Questions
    why_correct = ""
    why_incorrect = ""
    
    # Topic specific logic
    q_lower = (stem + " " + c_ans).lower()
    
    if 'adas' in q_lower or 'level 2' in q_lower:
        why_correct = "Level 2 ADAS (ACC/LTA) has technical limitations in detecting stationary objects e.g. construction vehicles; human drivers must maintain full control."
        why_incorrect = "Relying on ADAS to scroll phones, rest eyes, or drive in heavy fog/rain is dangerous and violates mandatory driver alertness laws."
    elif 'drunk' in q_lower or 'alcohol' in q_lower or 'bac' in q_lower or '0.15' in q_lower or '0.25' in q_lower or '180,000' in q_lower:
        why_correct = f"Taiwan has zero-tolerance DUI laws. The legal BAC administrative limit is 0.15 mg/L and criminal limit is 0.25 mg/L."
        why_incorrect = "Assuming alcohol metabolizes quickly, refusing breathalyzer tests, or scrolling phones carries severe fines up to NT$180,000 and license revocation."
    elif 'speed' in q_lower or '50 km/h' in q_lower or '40 km/h' in q_lower or '15 km/h' in q_lower:
        why_correct = "Speed limits are legally calibrated for road geometry: Urban default = 50 km/h; Slow lane = 40 km/h; Level crossing = 15 km/h."
        why_incorrect = "Exceeding speed limits reduces reaction time and quadruples (4x) braking distance when doubling speed."
    elif 'cargo' in q_lower or 'shoulder' in q_lower or '50 cm' in q_lower or '10 cm' in q_lower or '30 kg' in q_lower:
        why_correct = "Cargo dimension limits prevent load imbalance and road obstruction: Height <= rider shoulder / 2.85m; Rear extension <= 50 cm; Width extension <= 10 cm."
        why_incorrect = "Overloading or un-secured protruding cargo impairs steering, blocks vehicle lights, and creates severe falling debris hazards."
    elif 'crosswalk' in q_lower or 'pedestrian' in q_lower or '3 meters' in q_lower:
        why_correct = "Pedestrians have absolute right-of-way on zebra crosswalks. Vehicles MUST stop at least 3 meters (4 zebra stripes width) before crosswalks."
        why_incorrect = "Honking at pedestrians or maintaining speed through zebra crosswalks is illegal and carries heavy fines plus license suspension."
    elif 'sign' in q_lower or 'marking' in q_lower or 'traffic' in q_lower:
        why_correct = f"Option {opts[c_idx][:3]} accurately identifies the official road sign/marking definition prescribed by Taiwan Highway Bureau."
        why_incorrect = f"The other options describe completely different road signs or traffic rules."
    else:
        why_correct = f"Option {opts[c_idx][:3]} is the correct legal standard prescribed by the Road Traffic Management Penalty Act."
        why_incorrect = f"The other options violate road safety regulations, increase collision risk, or misinterpret traffic priority laws."

    expl = f"✅ **Why {opts[c_idx][:3]} is Correct**: {why_correct}\n\n❌ **Why other options are Wrong**: {why_incorrect}"
    return expl

def process_bank(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        qs = json.load(f)

    for q in qs:
        q['explanation'] = generate_educational_explanation(q)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Updated explanations for {len(qs)} questions in {filepath}")

process_bank('car_questions.json')
process_bank('questions.json')
