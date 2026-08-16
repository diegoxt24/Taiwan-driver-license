import json
path = r'C:\Users\User\Documents\GitHub\Taiwan driver license\scratch\chunks\input_chunk_2.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
for q in data['car_questions'][:5]:
    print(f"Num options: {len(q['options'])}")
