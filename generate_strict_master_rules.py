import json

with open('car_questions.json', 'r', encoding='utf-8') as f:
    car_qs = json.load(f)

with open('questions.json', 'r', encoding='utf-8') as f:
    moto_qs = json.load(f)

def get_exact_canonical(qlist, keywords):
    for q in qlist:
        q_text = (q['question'] + " " + " ".join(q['options'])).lower()
        if all(k in q_text for k in keywords):
            return q
    # fallback to first keyword match
    for q in qlist:
        q_text = (q['question'] + " " + " ".join(q['options'])).lower()
        if any(k in q_text for k in keywords):
            return q
    return qlist[0]

rule_defs_60 = [
    {"id": "R01", "title": "1. Urban Road Speed Limit (50 km/h)", "strict_kw": ["50 km/h", "speed"], "diagram": "speed_limit_50", "summary": "Default speed limit on urban roads without speed limit signs is 50 km/h."},
    {"id": "R02", "title": "2. Slow Lane & Narrow Road Speed Limit (40 km/h)", "strict_kw": ["40 km/h", "speed"], "diagram": "speed_limit_40", "summary": "Designated slow lanes and narrow roads without dividing lines have a max speed limit of 40 km/h."},
    {"id": "R03", "title": "3. Railroad Crossing Approach Speed (15 km/h)", "strict_kw": ["15 km/h"], "diagram": "railroad_crossing", "summary": "Approach railroad level crossings at 15 km/h or less and stop before crossing if red lights flash."},
    {"id": "R04", "title": "4. Downhill & Long Slope Engine Braking", "strict_kw": ["downhill", "slope"], "diagram": "braking_physics", "summary": "Use low gear engine braking on downhill slopes; avoid excessive foot braking to prevent brake fade."},
    {"id": "R05", "title": "5. Speed vs. Braking Physics (Double Speed = 4x Distance)", "strict_kw": ["braking", "distance"], "diagram": "braking_physics", "summary": "Braking distance is proportional to speed squared. Doubling speed quadruples required braking distance."},

    {"id": "R06", "title": "6. Breath Alcohol Administrative Limit (0.15 mg/L)", "strict_kw": ["0.15"], "diagram": "alcohol_limit", "summary": "Driving with breath alcohol concentration at or above 0.15 mg/L triggers mandatory administrative fines."},
    {"id": "R07", "title": "7. Criminal Drunk Driving Threshold (0.25 mg/L)", "strict_kw": ["0.25"], "diagram": "alcohol_limit", "summary": "BAC at or exceeding 0.25 mg/L constitutes a criminal offense under the Penal Code."},
    {"id": "R08", "title": "8. Drunk Driving Administrative Fines (NT$30,000 ~ NT$120,000)", "strict_kw": ["30,000", "120,000"], "diagram": "alcohol_limit", "summary": "Drunk driving for car drivers incurs fines from NT$30,000 to NT$120,000 plus license suspension."},
    {"id": "R09", "title": "9. Repeat Drunk Driving within 10 Years", "strict_kw": ["10 years", "second time"], "diagram": "alcohol_limit", "summary": "Repeat drunk driving within 10 years results in maximum fines, license revocation, and public disclosure."},
    {"id": "R10", "title": "10. Refusing Sobriety Breathalyzer Test (NT$180,000)", "strict_kw": ["180,000"], "diagram": "alcohol_limit", "summary": "Refusing a police breathalyzer test incurs an automatic NT$180,000 fine, impoundment, and license revocation."},

    {"id": "R11", "title": "11. Passengers Joint Fine for Drunk Driving", "strict_kw": ["passenger", "alcohol"], "diagram": "alcohol_limit", "summary": "Passengers riding in a vehicle operated by an intoxicated driver are fined NT$6,000 to NT$15,000."},
    {"id": "R12", "title": "12. Ignition Interlock Device (Alcohol Lock) Requirement", "strict_kw": ["ignition interlock"], "diagram": "alcohol_limit", "summary": "Drivers re-applying after license revocation for drunk driving MUST install an approved ignition interlock device."},
    {"id": "R13", "title": "13. Motorcycle Cargo Rear Extension (Max 50 cm)", "strict_kw": ["50 cm"], "diagram": "cargo_rear", "summary": "Motorcycle cargo must not extend forward past rider seat or more than 50 cm beyond rear wheel axle."},
    {"id": "R14", "title": "14. Motorcycle Cargo Width Extension (Max 10 cm)", "strict_kw": ["10 cm", "handlebars"], "diagram": "cargo_rear", "summary": "Cargo width on motorcycles must not extend more than 10 cm beyond outer edges of handlebars."},
    {"id": "R15", "title": "15. Motorcycle Cargo Weight Limits (30kg / 60kg / 90kg)", "strict_kw": ["30 kg"], "diagram": "cargo_rear", "summary": "Motorcycle load weight limits: Small light = 30 kg; Regular light = 60 kg; Heavy = 90 kg."},

    {"id": "R16", "title": "16. Small Vehicle Cargo Height (Max 2.85m / 1.5x width)", "strict_kw": ["2.85"], "diagram": "cargo_rear", "summary": "Car cargo height must not exceed 1.5 times vehicle width or a maximum height of 2.85 meters."},
    {"id": "R17", "title": "17. Cargo Protrusion & Falling Spills Penalty", "kw": ["falling", "scattered", "protrud"], "diagram": "cargo_rear", "summary": "Cargo must be tightly covered and secured. Items spilling onto roads incur severe fines and demerit points."},
    {"id": "R18", "title": "18. Straight Vehicles Priority over Turning Vehicles", "strict_kw": ["straight", "turn"], "diagram": "right_of_way", "summary": "Vehicles going straight have absolute priority over vehicles turning into the same lane or intersection."},
    {"id": "R19", "title": "19. Left-Turn vs. Right-Turn Priority", "strict_kw": ["left turn", "right turn"], "diagram": "right_of_way", "summary": "When vehicles from opposite directions turn into the same lane, left-turning vehicles yield to right-turning vehicles."},
    {"id": "R20", "title": "20. Unsignalized Equal Width Intersection Priority", "strict_kw": ["equal width"], "diagram": "right_of_way", "summary": "At unsignalized intersections of equal width, drivers yield to vehicles approaching from their right side."},

    {"id": "R21", "title": "21. Branch Road vs. Main Road Priority", "strict_kw": ["branch road"], "diagram": "right_of_way", "summary": "Vehicles entering from side/branch roads must stop and yield right-of-way to main road traffic."},
    {"id": "R22", "title": "22. Pedestrian Crosswalk Priority (3 Meters / 4 Stripes)", "strict_kw": ["pedestrian", "crossing"], "diagram": "right_of_way", "summary": "Drivers MUST stop at least 3 meters (4 zebra stripes) before crosswalks to yield to pedestrians."},
    {"id": "R23", "title": "23. Roundabout Traffic Priority", "strict_kw": ["roundabout"], "diagram": "right_of_way", "summary": "Vehicles entering roundabouts MUST yield right-of-way to vehicles already inside the roundabout."},
    {"id": "R24", "title": "24. Yielding to Emergency Vehicles & Sirens", "strict_kw": ["siren"], "diagram": "siren_yield", "summary": "Drivers MUST pull right and yield immediately to emergency sirens. Failure results in license revocation."},
    {"id": "R25", "title": "25. Solid Red Line (No Stopping 24 Hours)", "strict_kw": ["solid red line"], "diagram": "speed_limit_50", "summary": "Solid red roadside lines prohibit temporary stopping or parking 24 hours a day."},

    {"id": "R26", "title": "26. Solid Yellow Line (No Parking 7 AM - 8 PM)", "strict_kw": ["solid yellow line"], "diagram": "speed_limit_50", "summary": "Solid yellow lines prohibit parking from 7 AM to 8 PM; temporary stopping (<3 mins) is permitted."},
    {"id": "R27", "title": "27. Double Solid Yellow Lines (No Crossing / No U-Turn)", "strict_kw": ["double solid yellow"], "diagram": "speed_limit_50", "summary": "Double solid yellow lines separate opposite directions. Crossing or U-turning over them is strictly illegal."},
    {"id": "R28", "title": "28. Inverted White Triangle Road Marking (Yield Line)", "strict_kw": ["inverted triangle"], "diagram": "right_of_way", "summary": "An inverted white triangle marked on the road surface indicates a Yield Line requiring drivers to slow and yield."},
    {"id": "R29", "title": "29. Flashing Red vs. Flashing Yellow Signal", "strict_kw": ["flashing red"], "diagram": "traffic_light", "summary": "Flashing Red = Complete stop before proceeding. Flashing Yellow = Slow down and proceed with caution."},
    {"id": "R30", "title": "30. Police Officer Direction Superiority", "strict_kw": ["police officer"], "diagram": "traffic_light", "summary": "Manual directions given by a police officer on site override all automated signals or road signs."},

    {"id": "R31", "title": "31. Turn Signal Advance Distance (30 Meters)", "strict_kw": ["30 meters"], "diagram": "right_of_way", "summary": "Activate turn signals at least 30 meters before turning or changing lanes on city streets."},
    {"id": "R32", "title": "32. Overtaking Regulations & Prohibited Locations", "strict_kw": ["overtaking"], "diagram": "right_of_way", "summary": "Overtake on the left side only. Overtaking is prohibited in tunnels, bridges, curves, or level crossings."},
    {"id": "R33", "title": "33. Prohibited U-Turn Locations", "strict_kw": ["u-turn"], "diagram": "right_of_way", "summary": "U-turns are prohibited on sharp curves, steep slopes, narrow bridges, tunnels, or over double yellow lines."},
    {"id": "R34", "title": "34. Reversing & Backing Up Restrictions", "strict_kw": ["reversing"], "diagram": "right_of_way", "summary": "Reversing is prohibited on steep slopes, sharp curves, narrow roads, or expressways."},
    {"id": "R35", "title": "35. Handheld Mobile Device Penalties (Car NT$3,000 / Moto NT$1,000)", "strict_kw": ["handheld"], "diagram": "phone_fine", "summary": "Operating handheld mobile phones while driving incurs fines of NT$3,000 for cars and NT$1,000 for motorcycles."},

    {"id": "R36", "title": "36. Cigarette Smoking While Driving Fine (NT$1,200)", "strict_kw": ["cigarette"], "diagram": "phone_fine", "summary": "Holding, smoking, or lighting a cigarette while driving that affects others incurs a fine of NT$1,200."},
    {"id": "R37", "title": "37. Freeway Small Car Following Distance (Speed ÷ 2 in meters)", "strict_kw": ["following distance"], "diagram": "freeway_distance", "summary": "Freeway following distance for small cars: Speed (km/h) ÷ 2 = Minimum safe distance in meters."},
    {"id": "R38", "title": "38. Freeway Innermost Lane Usage (Overtaking Only)", "strict_kw": ["innermost lane"], "diagram": "freeway_distance", "summary": "The innermost freeway lane is the overtaking lane; non-overtaking vehicles must travel at max legal speed."},
    {"id": "R39", "title": "39. Hard Shoulder Driving Restrictions", "strict_kw": ["shoulder"], "diagram": "freeway_distance", "summary": "Driving on freeway hard shoulders is prohibited except during breakdowns, emergencies, or opened shoulder signs."},
    {"id": "R40", "title": "40. Warning Triangle Distance (100 Meters on Freeway)", "strict_kw": ["warning triangle"], "diagram": "freeway_distance", "summary": "Place warning triangles at least 100 meters behind broken-down vehicles on freeways (30-100m on regular roads)."},

    {"id": "R41", "title": "41. Tire Tread Depth Standards (1.6mm Car / 1.0mm Moto)", "strict_kw": ["tread"], "diagram": "tire_tread", "summary": "Minimum tire tread depth is 1.6 mm for cars and 1.0 mm for motorcycles. Worn tires risk aquaplaning."},
    {"id": "R42", "title": "42. Mandatory Seatbelt & Child Safety Seat Laws", "strict_kw": ["seatbelt"], "diagram": "seatbelt_law", "summary": "All occupants MUST wear seatbelts. Children under 4 years old must sit in rear-facing child safety seats."},
    {"id": "R43", "title": "43. Door Opening 2-Stage Protocol", "strict_kw": ["door"], "diagram": "car_door", "summary": "Always use 2-stage door opening: check mirrors, check blind spots, open door slightly, then step out safely."},
    {"id": "R44", "title": "44. Periodic Vehicle Inspection Frequency", "strict_kw": ["inspection"], "diagram": "demerit_points", "summary": "Cars >5 years old require annual inspection; cars >10 years old require inspection twice per year."},
    {"id": "R45", "title": "45. Compulsory Automobile Liability Insurance", "strict_kw": ["compulsory insurance"], "diagram": "demerit_points", "summary": "All motor vehicles must carry active Compulsory Liability Insurance; driving without it incurs impoundment."},

    {"id": "R46", "title": "46. First Aid Treatment Order (Airway -> Bleeding -> Fracture)", "strict_kw": ["first aid"], "diagram": "cpr_protocol", "summary": "First aid priority order: 1. Open Airway (B). 2. Control Bleeding (A). 3. Immobilize Fractures (C)."},
    {"id": "R47", "title": "47. CPR Chest Compression Ratio & Rate (30:2 / 100-120 bpm)", "strict_kw": ["cpr"], "diagram": "cpr_protocol", "summary": "Adult CPR standard: 30 compressions followed by 2 rescue breaths at a rate of 100-120 compressions per minute."},
    {"id": "R48", "title": "48. Suspected Neck/Spinal Injury Airway (Jaw-Thrust)", "strict_kw": ["jaw-thrust"], "diagram": "cpr_protocol", "summary": "For suspected neck/spinal trauma, use the Jaw-Thrust maneuver to clear airway without tilting the head."},
    {"id": "R49", "title": "49. Railroad Breakdown 3-Step SOS (Press -> Push -> Run)", "strict_kw": ["sos"], "diagram": "railroad_crossing", "summary": "Railroad breakdown SOS steps: 1. Press Emergency Red Button. 2. Push vehicle clear. 3. Run clear."},
    {"id": "R50", "title": "50. Demerit Points Cap (12 Points in 1 Year = 2 Mo. Suspension)", "strict_kw": ["demerit"], "diagram": "demerit_points", "summary": "Accumulating 12 demerit points within 1 year results in a 2-month driver license suspension."}
]

def generate_strict_canonical_rules(qlist, prefix):
    cards = []
    matched_q_set = set()
    
    for r in rule_defs_60:
        card_id = f"{prefix}_{r['id']}"
        kw_list = r.get('strict_kw', r.get('kw', []))
        matched = [q for q in qlist if any(k in (q['question'] + ' ' + ' '.join(q['options']) + ' ' + q.get('explanation','')).lower() for k in kw_list)]
        
        if not matched:
            matched = [qlist[0]]
            
        for q in matched:
            matched_q_set.add(q['id'])
            
        canonical = get_exact_canonical(matched, kw_list)
        
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

    unmatched = [q for q in qlist if q['id'] not in matched_q_set]
    if unmatched:
        cards.append({
            "id": f"{prefix}_R51",
            "title": "51. General Traffic Safety Regulations & Ethics",
            "summary": "General road safety regulations, ethical driving habits, and situational hazard awareness.",
            "key_fact": "General Traffic Safety Rules",
            "diagram": "right_of_way",
            "canonical_question": unmatched[0]["question"],
            "canonical_options": unmatched[0]["options"],
            "canonical_correct": unmatched[0]["correct_answer"],
            "canonical_correct_index": unmatched[0]["correct_index"],
            "matched_question_count": len(unmatched),
            "matched_question_ids": [q["id"] for q in unmatched]
        })
    return cards

car_cards = generate_strict_canonical_rules(car_qs, 'C')
moto_cards = generate_strict_canonical_rules(moto_qs, 'M')

with open('car_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(car_cards, f, indent=2, ensure_ascii=False)

with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(moto_cards, f, indent=2, ensure_ascii=False)

print(f"Strict canonical alignment complete: {len(car_cards)} Car cards, {len(moto_cards)} Moto cards.")
