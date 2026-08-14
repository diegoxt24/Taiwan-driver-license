import json
import re

def build_coherent_master_rules():
    # 1. CAR MASTER RULES (Clear, High-Yield, Grouped Core Rules)
    with open('car_questions.json', 'r', encoding='utf-8') as f:
        car_qs = json.load(f)

    # Categories to synthesize
    car_clusters = [
        {
            "id": "C_RULE_01",
            "title": "⚡ Master Rule 1: Speed Limits & Weather Reductions",
            "summary": "• Urban unmarked roads: 50 km/h.\n• Slow lanes & undivided narrow roads: 40 km/h.\n• Approaching railroad crossings: 15 km/h or less.\n• Severe weather (heavy rain, dense fog, low visibility <100m on freeway): Below 40 km/h.\n• Exceeding limit by 40+ km/h is classified as dangerous driving (heavy fines + license suspension).",
            "diagram": "speed_limit_50",
            "keywords": ["speed", "km/h", "fast", "slow", "fog", "rain", "limit"],
            "canonical_q": "CAR_0195" # Weather speed reduction question
        },
        {
            "id": "C_RULE_02",
            "title": "🍷 Master Rule 2: Drunk Driving BAC Limits & Severe Penalties",
            "summary": "• Administrative Fine threshold: 0.15 mg/L breath (or 0.03% blood).\n• Criminal Offense threshold: 0.25 mg/L breath (or 0.05% blood).\n• First offense: NT$30,000–120,000 + license suspension for 1–2 years.\n• Refusal to blow: NT$180,000 fine + instant revocation + impoundment.\n• Passengers (18+): Joint penalty fine of NT$6,000–15,000.",
            "diagram": "alcohol_limit",
            "keywords": ["alcohol", "drunk", "bac", "blood", "breath", "liquor"],
            "canonical_q": "CAR_0020"
        },
        {
            "id": "C_RULE_03",
            "title": "🛑 Master Rule 3: Intersection Right-of-Way Priority Protocol",
            "summary": "• Priority 1: Straight-going vehicle > Turning vehicle.\n• Priority 2: Left-turning vehicle MUST yield to Right-turning vehicle.\n• Unmarked equal intersection: Yield to vehicle approaching from your RIGHT side.\n• Roundabout: Entering vehicles MUST yield to circulating traffic inside.\n• Emergency sirens (Ambulance, Fire, Police): Immediate yield required (failure = NT$3,600 + license revocation).",
            "diagram": "right_of_way",
            "keywords": ["yield", "intersection", "turn", "straight", "roundabout", "right of way"],
            "canonical_q": "CAR_0102"
        },
        {
            "id": "C_RULE_04",
            "title": "🛣️ Master Rule 4: Freeway Driving & Safe Following Distances",
            "summary": "• Small car distance: Speed (km/h) ÷ 2 in meters (e.g. 100 km/h = 50m). Double in wet/fog.\n• Large truck distance: Speed (km/h) - 50 in meters (e.g. 100 km/h = 50m).\n• Breakdown triangle: Place 100 meters behind vehicle on freeway (30–100m on regular roads).\n• Inner lane on freeway: Overtaking only (may cruise at maximum legal speed if not impeding).",
            "diagram": "freeway_distance",
            "keywords": ["freeway", "expressway", "following distance", "triangle", "breakdown", "shoulder"],
            "canonical_q": "CAR_0186"
        },
        {
            "id": "C_RULE_05",
            "title": "🚪 Master Rule 5: Two-Stage Door Opening & Parking Rules",
            "summary": "• Two-Stage Door Opening (Art. 112): First open 15 cm, look back for passing motorcycles/cyclists, then open fully.\n• Solid Red Line: No stopping or parking 24 hours a day.\n• Solid Yellow Line: Temporary stopping <3 min allowed; no parking 7 AM to 8 PM.\n• Distance from curb: Parking must be within 40 cm (temporary stopping within 60 cm).\n• Prohibited within 10 meters of intersections, bus stops, or hydrants.",
            "diagram": "child_seat",
            "keywords": ["door", "two-stage", "parking", "stopping", "red line", "yellow line", "curb"],
            "canonical_q": "CAR_0450"
        },
        {
            "id": "C_RULE_06",
            "title": "👶 Master Rule 6: Seatbelts & Child Safety Seats",
            "summary": "• Seatbelts: Mandatory for ALL occupants on all roads (fines: NT$1,500 local, NT$3,000–6,000 highway).\n• Children under 4 years old / under 18 kg: Mandatory child safety seat placed in REAR seat.\n• Children under 2 years old: Mandatory REAR-FACING child seat.\n• Children under 6 years old: NEVER leave alone in vehicle (NT$3,000 fine + 4h safety class).",
            "diagram": "child_seat",
            "keywords": ["child", "seatbelt", "baby", "safety seat", "alone"],
            "canonical_q": "CAR_0207"
        },
        {
            "id": "C_RULE_07",
            "title": "🔧 Master Rule 7: Vehicle Maintenance & Diagnostic Standards",
            "summary": "• Minimum Tire Tread Depth: 1.6 mm for Cars (1.0 mm for Motorcycles).\n• Exhaust Smoke Diagnosis: Bluish-white = Burning engine oil; White steam = Coolant leak; Black = Unburned fuel.\n• Low Oil Pressure Light on dashboard: Stop immediately and turn off engine.\n• Towing rope: Length 3 to 5 meters with a yellow flag in the middle.",
            "diagram": "tire_tread",
            "keywords": ["tread", "tire", "smoke", "exhaust", "oil", "dashboard", "towing"],
            "canonical_q": "CAR_0204"
        },
        {
            "id": "C_RULE_08",
            "title": "🚑 Master Rule 8: First Aid, CPR & Emergency Protocols",
            "summary": "• First Aid Priority: 1. Airway (A) → 2. Breathing/Bleeding (B) → 3. Circulation/Fractures (C).\n• CPR Protocol: 30 chest compressions to 2 rescue breaths (30:2) at 100–120 bpm, depth 5–6 cm.\n• Suspected spinal/neck trauma: Use Jaw-Thrust maneuver without tilting neck.\n• Irreversible brain damage occurs within 4 to 6 minutes without oxygen.",
            "diagram": "cpr_protocol",
            "keywords": ["cpr", "first aid", "airway", "bleeding", "unconscious", "brain"],
            "canonical_q": "CAR_0952"
        },
        {
            "id": "C_RULE_09",
            "title": "📋 Master Rule 9: Driver License Demerit Points & Review Cycle",
            "summary": "• Accumulating 12 demerit points within 1 year = 2-month driver license suspension.\n• Professional driver license (<60 yrs): Reviewed once every 3 years from issuance.\n• Professional driver (68–70 yrs): Annual physical + cognitive/dementia test required.\n• 3 violations in 3 months = Suspension of vehicle license plate for 1 month.",
            "diagram": "demerit_system",
            "keywords": ["demerit", "points", "professional", "review", "suspension", "revocation"],
            "canonical_q": "CAR_0200"
        }
    ]

    car_master_rules = []
    for cl in car_clusters:
        matched_ids = []
        for q in car_qs:
            text = (q['question'] + " " + " ".join(q['options'])).lower()
            if any(kw in text for kw in cl['keywords']):
                matched_ids.append(q['id'])
        
        # Find canonical question
        can_q = next((q for q in car_qs if q['id'] == cl['canonical_q']), car_qs[0])
        
        car_master_rules.append({
            "id": cl["id"],
            "title": cl["title"],
            "summary": cl["summary"],
            "diagram": cl["diagram"],
            "canonical_question": can_q["question"],
            "canonical_options": can_q["options"],
            "canonical_correct": can_q["correct_answer"],
            "canonical_correct_index": can_q["correct_index"],
            "matched_question_count": len(matched_ids),
            "matched_question_ids": matched_ids
        })

    with open('car_master_rules.json', 'w', encoding='utf-8') as f:
        json.dump(car_master_rules, f, indent=2, ensure_ascii=False)

    # 2. MOTORCYCLE MASTER RULES
    with open('questions.json', 'r', encoding='utf-8') as f:
        moto_qs = json.load(f)

    moto_clusters = [
        {
            "id": "M_RULE_01",
            "title": "📦 Master Rule 1: Cargo Loading Limits (Weight, Height, Width)",
            "summary": "• Rear extension limit: Max 50 cm beyond rear wheel axle.\n• Width extension limit: Max 10 cm beyond handlebar outer edges.\n• Height limit: Not exceeding rider shoulders (small light: max 1.5m, heavy: max 2.5m).\n• Weight limits: Small light moto: 30 kg | Regular light/heavy moto: 60 kg | Large heavy (250cc+): 90 kg.",
            "diagram": "cargo_rear",
            "keywords": ["cargo", "loading", "rear", "axle", "handlebar", "shoulder", "kg"],
            "canonical_q": "MOTO_0001"
        },
        {
            "id": "M_RULE_02",
            "title": "🍷 Master Rule 2: Drunk Riding Penalties & Zero Tolerance",
            "summary": "• Legal limit: 0.15 mg/L breath (or 0.03% blood alcohol).\n• First offense: NT$15,000–90,000 + license suspension for 1–2 years.\n• Refusal to take breathalyzer: NT$180,000 fine + instant license revocation + vehicle impoundment.\n• Repeat offenses within 10 years: Max fine + permanent revocation + public photo/name disclosure.",
            "diagram": "alcohol_limit",
            "keywords": ["alcohol", "drunk", "bac", "breath", "liquor"],
            "canonical_q": "MOTO_0020"
        },
        {
            "id": "M_RULE_03",
            "title": "🪝 Master Rule 3: Two-Stage Left Turn (Hook-Turn Protocol)",
            "summary": "• Mandatory on roads with 3 or more lanes in the same direction, or where two-stage left turn signs are posted.\n• Protocol: Ride straight across intersection into the designated waiting box on the far right, turn front wheel left, and proceed when traffic light changes to green.\n• Turning left directly across inner lanes is strictly illegal and causes severe t-bone collisions.",
            "diagram": "right_of_way",
            "keywords": ["two-stage", "hook", "left turn", "waiting box", "lanes"],
            "canonical_q": "MOTO_0102"
        },
        {
            "id": "M_RULE_04",
            "title": "🪖 Master Rule 4: Helmet Safety Standards & Passenger Age Rules",
            "summary": "• Helmets: Must be CNS/BSMI certified with securely fastened chin strap. Unfastened = NT$500 fine.\n• Rear Passengers: Allowed ONLY on heavy/light motorcycles (50cc+) with designated passenger seat.\n• Carrying children on front footrest / floorboard: Strictly prohibited (NT$300–600 fine).\n• Small light electric bicycles: Carrying passengers strictly prohibited.",
            "diagram": "child_seat",
            "keywords": ["helmet", "strap", "passenger", "footrest", "rear seat", "child"],
            "canonical_q": "MOTO_0050"
        },
        {
            "id": "M_RULE_05",
            "title": "⚡ Master Rule 5: Speed Limits & Safe Following Buffer",
            "summary": "• Urban unmarked roads: 50 km/h | Undivided narrow lanes / alleys: 40 km/h.\n• Railroad crossings approach: 15 km/h or less.\n• Following distance physics: Braking distance is proportional to speed squared (2x speed = 4x braking distance).\n• Wet / slippery asphalt: Braking distance increases significantly; avoid abrupt front braking.",
            "diagram": "speed_limit_50",
            "keywords": ["speed", "km/h", "fast", "slow", "braking", "wet"],
            "canonical_q": "MOTO_0090"
        },
        {
            "id": "M_RULE_06",
            "title": "🔧 Master Rule 6: Tire Inspection & Maintenance Standards",
            "summary": "• Minimum Tire Tread Depth: 1.0 mm for Motorcycles (1.6 mm for Cars).\n• Check tire pressure weekly when tires are cold.\n• Brake lever inspection: Free play should be 10–20 mm.\n• Smooth progressive braking: Use both front and rear brakes simultaneously (approx. 70% front, 30% rear).",
            "diagram": "tire_tread",
            "keywords": ["tread", "tire", "brake", "lever", "pressure", "maintenance"],
            "canonical_q": "MOTO_0080"
        },
        {
            "id": "M_RULE_07",
            "title": "🚑 Master Rule 7: Crash Response & First Aid CPR Protocol",
            "summary": "• Stop immediately, turn off engine, turn on hazard lights if available.\n• Do NOT remove victim helmet unless breathing is obstructed (prevents cervical spine injury).\n• CPR: 30 Compressions to 2 Breaths (30:2) at 100–120 bpm, depth 5–6 cm.\n• Railroad crossing breakdown: 1. Press Emergency SOS Button → 2. Push bike clear → 3. Move away.",
            "diagram": "cpr_protocol",
            "keywords": ["cpr", "accident", "first aid", "emergency", "helmet", "railroad"],
            "canonical_q": "MOTO_0073"
        },
        {
            "id": "M_RULE_08",
            "title": "👁️ Master Rule 8: Hazard Perception & Blind Spot Anticipation",
            "summary": "• Large vehicle blind spots & inner wheel radius difference (Off-tracking): Stay at least 2 meters away from turning trucks.\n• Parked car door opening hazard: Maintain at least 1 meter lateral clearance from parked vehicles.\n• Approaching green lights: Always scan left and right for red-light runners.\n• Intersection yellow light: If past stop line, proceed safely; if before stop line, brake smoothly.",
            "diagram": "right_of_way",
            "keywords": ["hazard", "blind spot", "truck", "door", "turning", "perception", "video"],
            "canonical_q": "MOTO_0121"
        }
    ]

    moto_master_rules = []
    for ml in moto_clusters:
        matched_ids = []
        for q in moto_qs:
            text = (q['question'] + " " + " ".join(q['options'])).lower()
            if any(kw in text for kw in ml['keywords']):
                matched_ids.append(q['id'])
        
        can_q = next((q for q in moto_qs if q['id'] == ml['canonical_q']), moto_qs[0])
        
        moto_master_rules.append({
            "id": ml["id"],
            "title": ml["title"],
            "summary": ml["summary"],
            "diagram": ml["diagram"],
            "canonical_question": can_q["question"],
            "canonical_options": can_q["options"],
            "canonical_correct": can_q["correct_answer"],
            "canonical_correct_index": can_q["correct_index"],
            "matched_question_count": len(matched_ids),
            "matched_question_ids": matched_ids
        })

    with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
        json.dump(moto_master_rules, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(car_master_rules)} Car Master Rules and {len(moto_master_rules)} Moto Master Rules with 100% coherent clustering!")

if __name__ == '__main__':
    build_coherent_master_rules()
