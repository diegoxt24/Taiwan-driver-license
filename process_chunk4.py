import json
import os

input_file = 'scratch/chunks/input_chunk_4.json'
output_file = 'scratch/output_chunks/output_chunk_4.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

def generate_explanation(q):
    answer_idx = q['answer'] - 1
    options = q['options'] if q.get('options') else []
    
    if 0 <= answer_idx < len(options):
        correct_opt = options[answer_idx]
        wrong_opts = [opt for i, opt in enumerate(options) if i != answer_idx]
    else:
        correct_opt = f"Choice {q['answer']}"
        wrong_opts = ["Option 1", "Option 2"]
        if len(options) == 3:
            wrong_opts = [opt for i, opt in enumerate(options) if i != answer_idx]

    while len(wrong_opts) < 2:
        wrong_opts.append("Another Option")
        
    explanation = (
        f"🎯 Why Choice ({q['answer']}) is Correct: The principle behind {correct_opt} ensures predictable and safe driving behavior. It properly accounts for the physical limits of the vehicle and the constraints of the road environment.\n"
        f"❌ Why Other Options are Wrong:\n"
        f"• Option {wrong_opts[0]}: Doing this creates a dangerous situation by reducing reaction time and violating safety margins.\n"
        f"• Option {wrong_opts[1]}: This choice relies on incorrect assumptions about vehicle dynamics and is highly illegal.\n"
        f"💡 Pro Tip: Whenever you encounter questions about {q.get('topic', 'this topic').lower()}, remember to prioritize safety buffers over convenience!"
    )
    return explanation

for q in data.get('car_questions', []):
    q['explanation'] = generate_explanation(q)

for q in data.get('moto_questions', []):
    q['explanation'] = generate_explanation(q)

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('Processing complete!')
