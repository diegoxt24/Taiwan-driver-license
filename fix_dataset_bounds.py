import json
import re

def fix_dataset(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        qs = json.load(f)

    fixed_count = 0
    for q in qs:
        opts = q.get('options', [])
        idx = q.get('correct_index', 0)
        
        # If options list has only 1 string containing options inside
        if len(opts) == 1 and ('(1)' in opts[0] or '( 1 )' in opts[0]):
            raw_text = opts[0]
            opt_parts = re.split(r'\s*\(\s*([123])\s*\)\s*', raw_text)
            stem = opt_parts[0].strip()
            new_opts = []
            if len(opt_parts) >= 7:
                new_opts = [
                    f"({opt_parts[1]}) {opt_parts[2].strip()}",
                    f"({opt_parts[3]}) {opt_parts[4].strip()}",
                    f"({opt_parts[5]}) {opt_parts[6].strip()}"
                ]
            if new_opts:
                q['question'] = stem if stem else q['question']
                q['options'] = new_opts
                fixed_count += 1

        # Ensure correct_index is within bounds
        if q['correct_index'] >= len(q['options']):
            q['correct_index'] = len(q['options']) - 1
            fixed_count += 1
            
        q['correct_answer'] = q['options'][q['correct_index']]

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Fixed dataset {filepath}: {fixed_count} updates.")

fix_dataset('questions.json')
fix_dataset('car_questions.json')
