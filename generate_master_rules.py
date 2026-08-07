import json
from collections import defaultdict

def build_master_groups(q_filename, out_filename, is_car=False):
    with open(q_filename, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Master Rule definitions with high-yield educational cards
    rules_def = [
        {
            "id": "RULE_01",
            "title": "Cargo Loading & Dimension Limits",
            "icon": "fa-box",
            "keywords": ["cargo", "weight", "rear", "width", "height", "50 cm", "10 cm", "30 cm"],
            "diagram": "cargo_rear",
            "summary": "Motorcycle: Cargo rear extension MAX 50 cm past rear axle, width MAX 10 cm past handlebars, height MAX rider shoulders (total height < 2.0m). Max cargo weight: Heavy Moto 80kg, Light 50kg.\nCar: Cargo extension MAX 30 cm past front/rear bumpers, width MAX body width (max 2.5m), height MAX 2.5m.",
            "key_fact": "Rear Extension: Moto 50cm / Car 30cm"
        },
        {
            "id": "RULE_02",
            "title": "Alcohol, BAC Limits & Impaired Driving Fines",
            "icon": "fa-wine-glass",
            "keywords": ["alcohol", "bac", "drunk", "0.15", "sobriety", "drunk driving"],
            "diagram": "alcohol_limit",
            "summary": "Legal Breath Alcohol Concentration (BAC) limit is 0.15 mg/L (0.03% blood alcohol). First offense: Moto fine NT$15k–90k / Car fine NT$30k–120k + 1–2 year license suspension. Refusing sobriety test: Immediate NT$180k fine + license revocation + vehicle impounded.",
            "key_fact": "Legal BAC Limit: 0.15 mg/L"
        },
        {
            "id": "RULE_03",
            "title": "Speed Limits, Braking Distance & Lane Rules",
            "icon": "fa-gauge-high",
            "keywords": ["speed", "km/h", "40", "50", "15", "fast lane", "slow lane", "braking distance"],
            "diagram": "speed_limit",
            "summary": "Urban / Unmarked roads MAX 50 km/h. Slow lanes & narrow roads MAX 40 km/h. Railroad level crossing approach MAX 15 km/h. Double speed quadruples (4x) the required braking distance!",
            "key_fact": "Unmarked: 50 km/h | Slow Lane: 40 km/h | Railroad: 15 km/h"
        },
        {
            "id": "RULE_04",
            "title": "Tire Tread Depth, Inspection & Maintenance",
            "icon": "fa-compact-disc",
            "keywords": ["tread", "tire", "1.0", "1.6", "wear"],
            "diagram": "tire_tread",
            "summary": "Minimum legal tire tread depth: Motorcycle = 1.0 mm | Car = 1.6 mm. Replace tire immediately when tread aligns with wear indicators or tire reaches 6 years from manufacture date.",
            "key_fact": "Min Tread: Moto 1.0 mm | Car 1.6 mm"
        },
        {
            "id": "RULE_05",
            "title": "Intersection Safety & Right-of-Way Rules",
            "icon": "fa-code-merge",
            "keywords": ["right of way", "intersection", "straight", "unsignalized", "left turn"],
            "diagram": "right_of_way",
            "summary": "At unsignalized intersections: 1. Vehicles going straight have absolute right of way over turning vehicles. 2. Left-turning vehicles must yield to right-turning/straight vehicles. 3. Vehicle on narrow road yields to wide road.",
            "key_fact": "Priority #1: Straight-Going Vehicles"
        },
        {
            "id": "RULE_06",
            "title": "Turning Laws, Signals & Hook Turn",
            "icon": "fa-arrows-turn-to-dots",
            "keywords": ["turn", "hook", "signal", "30 meter", "u-turn"],
            "diagram": "right_of_way",
            "summary": "Signal intention at least 30 meters before turning or changing lanes (100m on freeway). Motorcycles turning left on roads with designated inner fast lane prohibition MUST perform a Two-Stage Hook Turn (兩段式左轉).",
            "key_fact": "Turn Signal Distance: At least 30 meters"
        },
        {
            "id": "RULE_07",
            "title": "Freeway & Expressway Specific Laws",
            "icon": "fa-road",
            "keywords": ["freeway", "expressway", "shoulder", "100", "following distance"],
            "diagram": "freeway_distance",
            "summary": "Car freeway following distance on dry road = Speed ÷ 2 in meters (100 km/h = 50m distance). Rain/wet road = Double distance. Driving on hard shoulder prohibited unless authorized. Breakdown warning triangle placed 100m behind vehicle.",
            "key_fact": "Following Distance = Speed ÷ 2"
        },
        {
            "id": "RULE_08",
            "title": "Emergency First Aid, CPR/AED & Accident Protocols",
            "icon": "fa-heart-pulse",
            "keywords": ["cpr", "aed", "compression", "first aid", "accident", "brain"],
            "diagram": "child_seat",
            "summary": "CPR Ratio: 30 compressions to 2 ventilations (30:2). Rate: 100–120 compressions/min, depth 5–6 cm. Brain damage starts in 4–6 minutes without oxygen. Suspected spinal injury = Jaw-thrust maneuver (Do NOT tilt head!).",
            "key_fact": "CPR Ratio: 30 Compressions : 2 Breaths"
        },
        {
            "id": "RULE_09",
            "title": "Traffic Signs, Signals & Road Markings",
            "icon": "fa-traffic-light",
            "keywords": ["sign", "signal", "marking", "light", "red", "yellow"],
            "diagram": "speed_limit",
            "summary": "Red Light: Complete stop before stop line. Yellow Light: Warning of red light; proceed only if already inside intersection. Red Flashing Light: Stop and yield. Yellow Flashing Light: Slow down and proceed with caution.",
            "key_fact": "Red Flashing = Stop & Yield"
        }
    ]

    master_cards = []

    for r in rules_def:
        matched_qs = []
        for q in questions:
            q_text = (q['question'] + " " + q.get('explanation', '')).lower()
            if any(kw in q_text for kw in r['keywords']):
                matched_qs.append(q)

        canonical = matched_qs[0] if matched_qs else questions[0]
        
        master_cards.append({
            "id": r["id"],
            "title": r["title"],
            "icon": r["icon"],
            "summary": r["summary"],
            "key_fact": r["key_fact"],
            "diagram": r["diagram"],
            "canonical_question": canonical["question"],
            "canonical_options": canonical["options"],
            "canonical_correct": canonical["correct_answer"],
            "canonical_correct_index": canonical["correct_index"],
            "matched_question_count": len(matched_qs),
            "matched_question_ids": [q["id"] for q in matched_qs]
        })

    with open(out_filename, 'w', encoding='utf-8') as f:
        json.dump(master_cards, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(master_cards)} Master Rule Groups for {out_filename}.")

build_master_groups('questions.json', 'moto_master_rules.json', is_car=False)
build_master_groups('car_questions.json', 'car_master_rules.json', is_car=True)
