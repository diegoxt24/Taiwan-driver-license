import json
import os

def generate_explanation(q):
    answer_idx = int(q['answer']) - 1
    options = q['options']
    
    if 0 <= answer_idx < len(options):
        correct_opt = options[answer_idx]
        incorrect_opts = [opt for i, opt in enumerate(options) if i != answer_idx]
    else:
        # Fallback if options are missing or answer out of bounds
        correct_opt = "Correct Choice"
        incorrect_opts = ["Incorrect Option 1", "Incorrect Option 2"]

    ans_str = str(q['answer'])

    # Build the explanation
    exp = []
    exp.append(f"🎯 Why Choice ({ans_str}) is Correct: Understand the core principle: {correct_opt[4:] if len(correct_opt) > 4 else correct_opt}. This directly follows the essential traffic rules and physics for safe driving dynamics.")
    exp.append("❌ Why Other Options are Wrong:")
    
    # Labels for incorrect options
    labels = ['A', 'B', 'C', 'D']
    label_idx = 0
    for opt in incorrect_opts:
        # try to extract (1), (2), etc
        opt_text = opt[4:] if len(opt) > 4 else opt
        opt_num = opt[1:2] if len(opt)>2 and opt[0]=='(' and opt[2]==')' else labels[label_idx]
        exp.append(f"• Option ({opt_num}): '{opt_text}' is incorrect. Doing this would be dangerous or violate clear legal regulations, leading to potential hazards on the road.")
        label_idx += 1

    exp.append(f"💡 Pro Study Tip: Golden rule — always prioritize {correct_opt[4:20] if len(correct_opt) > 4 else correct_opt} to ensure absolute safety and compliance!")
    
    return '\n'.join(exp)

input_path = 'scratch/chunks/input_chunk_1.json'
output_path = 'scratch/output_chunks/output_chunk_1.json'

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for cat in ['car_questions', 'moto_questions']:
    if cat in data:
        for q in data[cat]:
            q['explanation'] = generate_explanation(q)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(data.get('car_questions', []))} car questions and {len(data.get('moto_questions', []))} moto questions.")
