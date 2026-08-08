import json

with open('car_questions.json', 'r', encoding='utf-8') as f:
    cq = json.load(f)

with open('questions.json', 'r', encoding='utf-8') as f:
    mq = json.load(f)

# Build dynamic flexible topic master rule generator
def generate_official_master_rules(qlist, module_type):
    is_car = module_type == 'car'
    
    # 35 Core Master Rule Definitions aligned with THB PDF structure
    rule_defs = [
        {"id": "R01", "title": "1. Cargo Loading & Length/Width Limits", "keywords": ["cargo", "loading", "length", "width", "weight", "extend", "rear"], "diagram": "cargo_rear", "summary": "Cargo loading regulations: Vehicle cargo must be securely tied and stacked. Must not exceed prescribed vehicle length, width, or height limits."},
        {"id": "R02", "title": "2. Child Safety Seats & Passenger Safety", "keywords": ["child", "children", "safety seat", "passenger", "rear seat", "front seat"], "diagram": "child_seat", "summary": "Child passenger safety: Children under 4 years old or 18 kg must be seated in rear-facing child safety seats in the rear seat."},
        {"id": "R03", "title": "3. Door Opening & Boarding Safety", "keywords": ["door", "opening", "mirror", "rear traffic", "alighting"], "diagram": "car_door", "summary": "Opening vehicle doors: Drivers and passengers must check rear mirrors and shoulder blind spots before opening doors to avoid traffic accidents."},
        {"id": "R04", "title": "4. Tire Inspection & Minimum Tread Depth", "keywords": ["tire", "tread", "depth", "inspection", "groove", "indicator"], "diagram": "tire_tread", "summary": "Tire tread safety: Tire tread depth must meet minimum legal standards (1.6mm for cars / 1.0mm for motorcycles) to prevent aquaplaning."},
        {"id": "R05", "title": "5. Freeway & Expressway Safe Following Distance", "keywords": ["freeway", "expressway", "following distance", "safe distance", "meters"], "diagram": "freeway_distance", "summary": "Following distance rule: Maintain safe following distance on freeways and expressways. Double distance under rain, fog, or wet road conditions."},
        {"id": "R06", "title": "6. Freeway Hard Shoulder & Lane Regulations", "keywords": ["shoulder", "lane", "innermost", "overtaking", "lane change"], "diagram": "freeway_distance", "summary": "Freeway lane rules: Driving on the hard shoulder is prohibited unless explicitly opened by signs or during breakdown emergencies."},
        {"id": "R07", "title": "7. Drunk Driving Administrative Fines & Penalties", "keywords": ["drunk", "alcohol", "intoxicated", "fine", "penalty", "blood alcohol"], "diagram": "alcohol_limit", "summary": "Drunk driving penalties: Operating a vehicle under the influence incurs heavy administrative fines, vehicle impoundment, and license suspension."},
        {"id": "R08", "title": "8. Legal Breath Alcohol Concentration (BAC) Limits", "keywords": ["0.15", "0.25", "breath alcohol", "concentration", "bac", "limit"], "diagram": "alcohol_limit", "summary": "Legal BAC threshold: Legal breath alcohol limit is 0.15 mg/L. Testing at or above 0.25 mg/L results in criminal prosecution."},
        {"id": "R09", "title": "9. Refusing Sobriety Test Penalties (NT$180,000)", "keywords": ["refus", "breathalyzer", "sobriety", "180,000", "test"], "diagram": "alcohol_limit", "summary": "Refusing sobriety test: Refusing a police breathalyzer test results in an automatic NT$180,000 fine, license revocation, and vehicle impoundment."},
        {"id": "R10", "title": "10. Handheld Mobile Phone & Device Penalties", "keywords": ["phone", "cellphone", "handheld", "device", "call", "mobile"], "diagram": "phone_fine", "summary": "Handheld phone prohibition: Operating handheld phones, computers, or mobile devices while driving or riding is strictly prohibited."},
        {"id": "R11", "title": "11. Mandatory Seatbelt & Safety Gear Regulations", "keywords": ["seatbelt", "seat belt", "helmet", "chinstrap", "gear", "fasten"], "diagram": "seatbelt_law", "summary": "Seatbelt & Helmet rules: Driver and all passengers must wear seatbelts at all times. Motorcycle riders must wear BSMI certified helmets."},
        {"id": "R12", "title": "12. Standard Unmarked Urban Road Speed Limits (50 km/h)", "keywords": ["50 km/h", "unmarked", "urban road", "speed limit"], "diagram": "speed_limit_50", "summary": "Standard urban speed limit: Unless otherwise signed, maximum speed limit on ordinary urban roads without lane lines is 50 km/h."},
        {"id": "R13", "title": "13. Slow Lane & Narrow Road Speed Limits (40 km/h)", "keywords": ["40 km/h", "slow lane", "narrow road", "dividing line"], "diagram": "speed_limit_40", "summary": "Slow lane speed limit: Maximum speed limit on designated slow lanes or narrow roads without dividing lines is 40 km/h."},
        {"id": "R14", "title": "14. Railroad Level Crossing Approach Speed (15 km/h)", "keywords": ["railroad", "level crossing", "15 km/h", "tracks", "train"], "diagram": "railroad_crossing", "summary": "Railroad crossing approach: Reduce speed to 15 km/h or less when approaching level crossings. Stop at least 3-6 meters before tracks when signals flash."},
        {"id": "R15", "title": "15. Speed vs. Braking Distance Physics", "keywords": ["braking", "stopping distance", "double speed", "quadrupled", "physics"], "diagram": "braking_physics", "summary": "Braking distance physics: Stopping distance is proportional to speed squared. Doubling speed quadruples (4x) required stopping distance."},
        {"id": "R16", "title": "16. Failing to Yield to Emergency Vehicles & Sirens", "keywords": ["siren", "ambulance", "fire engine", "emergency", "yield"], "diagram": "siren_yield", "summary": "Emergency vehicle priority: Drivers MUST immediately yield right-of-way to ambulances and fire engines sounding sirens. Failure results in license revocation."},
        {"id": "R17", "title": "17. Horn & Headlight Night Usage Rules", "keywords": ["horn", "headlight", "low-beam", "high-beam", "night", "oncoming"], "diagram": "tire_tread", "summary": "Lighting & Horn rules: Switch high-beams to low-beams when meeting oncoming traffic at night. Horn taps max 0.5s with max 3 taps."},
        {"id": "R18", "title": "18. Unsignalized Intersection Priority Rules", "keywords": ["unsignalized", "intersection", "straight", "priority", "equal width"], "diagram": "right_of_way", "summary": "Intersection priority: At unsignalized intersections, straight-going vehicles have absolute priority over turning vehicles."},
        {"id": "R19", "title": "19. Left Turn vs. Right Turn Priority", "keywords": ["left turn", "right turn", "opposite direction", "turning"], "diagram": "right_of_way", "summary": "Turning priority: When two vehicles from opposite directions turn into the same lane, left-turning vehicles MUST yield to right-turning vehicles."},
        {"id": "R20", "title": "20. Narrow Road vs. Wide Main Road Rules", "keywords": ["narrow", "side road", "main road", "wide road", "branch"], "diagram": "right_of_way", "summary": "Main road priority: Vehicles entering from narrow side roads or branch roads MUST stop and yield right-of-way to vehicles on main roads."},
        {"id": "R21", "title": "21. Pedestrian Crosswalk Absolute Right of Way", "keywords": ["crosswalk", "pedestrian", "zebra", "yielding", "walk"], "diagram": "right_of_way", "summary": "Pedestrian priority: Pedestrians on zebra crosswalks have absolute right-of-way. Vehicles MUST stop at least 3 meters before crosswalks to yield."},
        {"id": "R22", "title": "22. Turn Signal Advance Distance (30 meters)", "keywords": ["turn signal", "30 meters", "changing lanes", "turning", "indicator"], "diagram": "right_of_way", "summary": "Turn signal distance: Activate turn signals at least 30 meters before turning or changing lanes on city roads (100m on expressways)."},
        {"id": "R23", "title": "23. Prohibited U-Turn Locations & Markings", "keywords": ["u-turn", "double solid yellow", "solid white", "prohibited"], "diagram": "right_of_way", "summary": "Prohibited U-turns: U-turns are strictly prohibited on double solid yellow lines, steep slopes, sharp curves, or railroad crossings."},
        {"id": "R24", "title": "24. CPR Chest Compression Ratio (30:2)", "keywords": ["cpr", "compression", "ventilation", "30:2", "ratio", "rescue breath"], "diagram": "cpr_protocol", "summary": "CPR protocol: Standard CPR ratio for adult cardiac arrest is 30 chest compressions followed by 2 rescue breaths (30:2 ratio)."},
        {"id": "R25", "title": "25. CPR Compression Depth & Rate Parameters", "keywords": ["depth", "rate", "100-120", "5-6 cm", "compressions"], "diagram": "cpr_protocol", "summary": "CPR parameters: Deliver chest compressions at 100 to 120 compressions/min reaching 5 to 6 cm depth on central sternum."},
        {"id": "R26", "title": "26. Brain Oxygen Deprivation Window (4 to 6 mins)", "keywords": ["brain", "oxygen", "deprivation", "4 to 6", "cardiac arrest"], "diagram": "cpr_protocol", "summary": "Brain survival window: Irreversible brain damage begins within 4 to 6 minutes of cardiac/respiratory arrest without oxygen."},
        {"id": "R27", "title": "27. Spinal Injury Airway Clear (Jaw-Thrust Maneuver)", "keywords": ["jaw-thrust", "spinal", "neck", "airway", "trauma"], "diagram": "cpr_protocol", "summary": "Spinal trauma first aid: Clear airway using Jaw-thrust maneuver without tilting head for victims with suspected neck or spinal injury."},
        {"id": "R28", "title": "28. Heimlich Maneuver Position for Choking Victims", "keywords": ["heimlich", "choking", "navel", "sternum", "fist"], "diagram": "cpr_protocol", "summary": "Heimlich maneuver position: Place fist between navel and bottom of sternum, thrusting inward and upward for choking victims."},
        {"id": "R29", "title": "29. Railroad Level Crossing Breakdown SOS Button", "keywords": ["railroad", "emergency button", "sos", "breakdown", "push"], "diagram": "railroad_crossing", "summary": "Railroad breakdown SOS: If vehicle breaks down on railroad tracks: 1. Press Emergency SOS button. 2. Push vehicle clear. 3. Evacuate."},
        {"id": "R30", "title": "30. Running Red Light Fines & Demerit Points", "keywords": ["red light", "running red", "demerit", "3 points", "signal"], "diagram": "traffic_light", "summary": "Running red light: Running a red light carries administrative fines PLUS 3 demerit points on driver record."},
        {"id": "R31", "title": "31. Demerit Point Accumulation & Suspension (12 Points)", "keywords": ["demerit points", "12 points", "1 year", "suspension", "accumulating"], "diagram": "demerit_points", "summary": "Demerit threshold: Accumulating 12 demerit points within 1 year results in mandatory 2-month driver license suspension."},
        {"id": "R32", "title": "32. Temporary Parking Limit (3 Minutes)", "keywords": ["temporary parking", "3 minutes", "stopping", "driver ready"], "diagram": "speed_limit_50", "summary": "Temporary parking rule: Temporary parking is permitted for max 3 minutes with driver ready at controls to move immediately."},
        {"id": "R33", "title": "33. Prohibited Stopping Distance (10 meters)", "keywords": ["10 meters", "bus stop", "fire hydrant", "intersection stopping"], "diagram": "speed_limit_50", "summary": "Prohibited stopping zone: Stopping or parking is prohibited within 10 meters of intersections, bus stops, or fire hydrants."},
        {"id": "R34", "title": "34. Traffic Light Indications (Red / Flashing Red / Yellow)", "keywords": ["traffic light", "flashing red", "flashing yellow", "solid red", "indications"], "diagram": "traffic_light", "summary": "Traffic light signals: Solid Red = Stop behind stop line. Flashing Red = Stop & yield right-of-way. Flashing Yellow = Caution."},
        {"id": "R35", "title": "35. Hazard Perception & Defensive Driving Awareness", "keywords": ["hazard", "perception", "defensive", "anticipate", "blind spot", "video"], "diagram": "right_of_way", "summary": "Defensive driving: Always maintain situational awareness, scan blind spots, and anticipate potential hazards from surrounding traffic."}
    ]
    
    cards = []
    for r in rule_defs:
        card_id = f"C_{r['id']}" if is_car else f"M_{r['id']}"
        matched = [q for q in qlist if any(kw in (q['question'] + ' ' + ' '.join(q['options']) + ' ' + q.get('explanation','')).lower() for kw in r['keywords'])]
        
        # If no direct keyword match, grab topically related category question
        if not matched:
            matched = [q for q in qlist if r['keywords'][0] in (q['category'] + ' ' + q['question']).lower()]
        if not matched:
            matched = [qlist[0]]
            
        canonical = matched[0]
        
        cards.append({
            "id": card_id,
            "title": r["title"],
            "summary": r["summary"],
            "key_fact": r["title"],
            "diagram": r["diagram"],
            "canonical_question": canonical["question"],
            "canonical_options": canonical["options"],
            "canonical_correct": canonical["correct_answer"],
            "canonical_correct_index": canonical["correct_index"],
            "matched_question_count": len(matched),
            "matched_question_ids": [q["id"] for q in matched]
        })
    return cards

car_master_cards = generate_official_master_rules(cq, 'car')
moto_master_cards = generate_official_master_rules(mq, 'moto')

with open('car_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(car_master_cards, f, indent=2, ensure_ascii=False)

with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(moto_master_cards, f, indent=2, ensure_ascii=False)

print(f"Generated {len(car_master_cards)} Car Master Rules and {len(moto_master_cards)} Moto Master Rules for official datasets.")
