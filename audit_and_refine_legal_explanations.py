import json
import re

def build_precise_legal_explanation(q):
    stem = q['question']
    opts = q['options']
    c_idx = q['correct_index']
    c_ans = q['correct_answer']
    cat = q.get('category', '')
    
    q_text = stem + " " + " ".join(opts) + " " + c_ans
    q_lower = q_text.lower()
    
    # 1. True/False questions
    if len(opts) == 2 and ('True' in opts[0] or 'False' in opts[0]):
        if c_idx == 0:
            why_right = "This statement fully complies with official Taiwan Road Traffic Management Regulations."
            why_wrong = "Marking this False is incorrect because ignoring this rule leads to fines, demerit points, or accidents."
        else:
            why_right = "This statement describes an illegal or unsafe practice prohibited under traffic law."
            why_wrong = "Marking this True is incorrect because obeying this statement violates traffic safety regulations."
        return f"✅ **Why Correct**: {why_right}\n\n❌ **Why Incorrect**: {why_wrong}"

    # 2. Domain-Specific Precise Legal Rules
    why_right = ""
    why_wrong = ""

    if 'adas' in q_lower or 'level 2' in q_lower or 'acc' in q_lower:
        why_right = "Level 2 ADAS (ACC/LTA) only provides driving assistance and cannot reliably detect stationary construction vehicles. The human driver remains legally responsible at all times."
        why_wrong = "Taking hands off the wheel, resting eyes, or trusting ADAS in heavy fog/rain violates Article 43 of the Road Traffic Management Penalty Act."
    elif '0.15' in q_lower or '0.25' in q_lower or 'alcohol' in q_lower or 'drunk' in q_lower or '180,000' in q_lower or 'breathalyzer' in q_lower:
        why_right = "BAC >= 0.15 mg/L incurs administrative fines (NT$30k-120k for cars, NT$15k-90k for motos). BAC >= 0.25 mg/L incurs criminal prosecution. Refusing breathalyzer = automatic NT$180,000 fine."
        why_wrong = "Believing alcohol metabolizes quickly or refusing testing leads to license revocation, vehicle impoundment, and public photo disclosure."
    elif '50 km/h' in q_lower or '40 km/h' in q_lower or '15 km/h' in q_lower or 'speed limit' in q_lower or 'speeding' in q_lower:
        why_right = "Legal speed limits: Urban roads without signs = 50 km/h; Slow lanes / undivided narrow roads = 40 km/h; Level crossings = 15 km/h."
        why_wrong = "Exceeding speed limits reduces emergency reaction time and quadruples (4x) stopping distance when speed doubles."
    elif '50 cm' in q_lower or '10 cm' in q_lower or 'cargo' in q_lower or 'shoulder' in q_lower or '2.85' in q_lower or 'weight' in q_lower:
        why_right = "Cargo limits: Motorcycle height <= rider shoulder; Rear extension <= 50 cm; Width extension <= 10 cm beyond handlebars. Car height <= 1.5x width (max 2.85m)."
        why_wrong = "Overloading or un-secured cargo destabilizes vehicle balance, obstructs tail lights, and creates hazardous falling debris."
    elif 'crosswalk' in q_lower or 'pedestrian' in q_lower or '3 meters' in q_lower or 'zebra' in q_lower:
        why_right = "Drivers MUST stop at least 3 meters (approx. 4 zebra stripes width) before crosswalks to yield to pedestrians under Article 44 of the Penalty Act."
        why_wrong = "Honking, swerving around pedestrians, or accelerating through crosswalks carries mandatory fines up to NT$6,000 and license suspension."
    elif 'tread' in q_lower or 'tire' in q_lower or '1.6' in q_lower or '1.0' in q_lower:
        why_right = "Minimum legal tire tread depth: 1.6 mm for cars and 1.0 mm for motorcycles. Worn tread to indicator bars fails periodic inspection."
        why_wrong = "Driving on worn tires dramatically increases hydroplaning (aquaplaning) risk and causes high-speed blowout crashes."
    elif 'cpr' in q_lower or '30:2' in q_lower or '100-120' in q_lower or 'airway' in q_lower or 'jaw-thrust' in q_lower:
        why_right = "First Aid Standards: CPR ratio = 30 compressions to 2 rescue breaths at 100-120 bpm; Priority = Airway (B) -> Bleeding (A) -> Fracture (C); Spinal trauma = Jaw-Thrust maneuver."
        why_wrong = "Arbitrarily moving unconscious crash victims or tilting head in spinal trauma can cause permanent paralysis or fatal nerve injury."
    elif 'siren' in q_lower or 'ambulance' in q_lower or 'fire engine' in q_lower:
        why_right = "Drivers MUST immediately pull to the right lane and yield right-of-way to emergency vehicles sounding sirens."
        why_wrong = "Failing to yield to emergency vehicles carries an NT$3,600 fine and mandatory driver license revocation."
    elif 'freeway' in q_lower or 'expressway' in full_text if (full_text := q_lower) else None or '100 meters' in q_lower:
        why_right = "Freeway rules: Safe distance = Speed (km/h) ÷ 2 in meters; Warning triangle = 100 meters behind breakdown; Innermost lane = overtaking only."
        why_wrong = "Driving on hard shoulder or stopping without warning triangle creates high-speed rear-end collision hazards."
    elif 'phone' in q_lower or 'cellphone' in q_lower or 'handheld' in q_lower or 'cigarette' in q_lower:
        why_right = "Operating handheld phones while driving incurs fines of NT$3,000 for cars and NT$1,000 for motorcycles under Article 31-1. Smoking while driving = NT$1,200."
        why_wrong = "Using handheld devices distracts visual attention and slows braking reaction time by up to 50%."
    elif 'red line' in q_lower or 'yellow line' in q_lower or 'double yellow' in q_lower:
        why_right = "Road markings: Solid Red Line = No stopping 24 hours; Solid Yellow Line = No parking 7am-8pm (stopping <3 min allowed); Double Yellow = No crossing or U-turns."
        why_wrong = "Parking or U-turning over prohibited markings obstructs traffic flow and triggers mandatory administrative fines."
    elif 'sign' in cat.lower() or 'sign' in q_lower or 'marking' in q_lower:
        why_right = f"Option {opts[c_idx][:3]} accurately states the official Highway Bureau definition for this traffic sign/marking."
        why_wrong = "The alternative options describe different regulatory restrictions or warning indications."
    else:
        why_right = f"Option {opts[c_idx][:3]} is the correct safety requirement prescribed under Taiwan Road Traffic Regulations."
        why_wrong = "The alternative options violate safety regulations or misapply traffic priority laws."

    return f"✅ **Why {opts[c_idx][:3]} is Correct**: {why_right}\n\n❌ **Why other options are Wrong**: {why_wrong}"

def refine_dataset(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        qs = json.load(f)

    for q in qs:
        q['explanation'] = build_precise_legal_explanation(q)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)

refine_dataset('car_questions.json')
refine_dataset('questions.json')
print("Successfully refined 100% of question explanations!")
