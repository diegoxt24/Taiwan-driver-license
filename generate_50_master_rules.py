import json

# Load question banks
with open('questions.json', 'r', encoding='utf-8') as f:
    moto_qs = json.load(f)

with open('car_questions.json', 'r', encoding='utf-8') as f:
    car_qs = json.load(f)

# Define 50 granular Master Rule Topics covering 100% of official topics
granular_topics = [
    # --- Group 1: Speed Limits & Vehicle Dynamics (Rules 1-5) ---
    {"id": "R01", "title": "1. Urban Road Standard Speed Limits (50 km/h)", "kw": ["50 km/h", "urban road", "unmarked lane", "speed limit"], "diagram": "speed_limit_50", "summary": "Unmarked urban roads have a default speed limit of 50 km/h unless signed otherwise."},
    {"id": "R02", "title": "2. Slow Lanes & Narrow Roads Speed Limits (40 km/h)", "kw": ["40 km/h", "slow lane", "narrow road", "undivided"], "diagram": "speed_limit_40", "summary": "Designated slow lanes or narrow undivided roads have a maximum speed limit of 40 km/h."},
    {"id": "R03", "title": "3. Railroad Crossing Approach Speed (15 km/h)", "kw": ["15 km/h", "railroad", "level crossing", "approach speed"], "diagram": "railroad_crossing", "summary": "Reduce speed to 15 km/h or lower when approaching any railroad level crossing."},
    {"id": "R04", "title": "4. Speed vs. Braking Distance Physics (Double Speed = 4x Distance)", "kw": ["braking", "stopping distance", "quadruple", "double speed", "4 times"], "diagram": "braking_physics", "summary": "Braking distance increases exponentially with speed: doubling your speed quadruples (4x) the braking distance."},
    {"id": "R05", "title": "5. Adverse Weather & Heavy Rain Speed Reduction", "kw": ["heavy rain", "fog", "slippery", "reduced speed", "visibility"], "diagram": "braking_physics", "summary": "Slow down immediately during heavy rain, fog, or slippery road conditions and increase following distance."},

    # --- Group 2: Drunk Driving, Drugs & Alcohol Laws (Rules 6-10) ---
    {"id": "R06", "title": "6. Legal BAC Thresholds (0.15 mg/L & 0.25 mg/L)", "kw": ["0.15", "0.25", "breath alcohol", "concentration", "bac"], "diagram": "alcohol_limit", "summary": "Administrative penalties apply at 0.15 mg/L BAC. Criminal prosecution applies at 0.25 mg/L BAC or higher."},
    {"id": "R07", "title": "7. Administrative Fines for Drunk Driving (NT$30,000 ~ NT$120,000)", "kw": ["drunk driving", "30,000", "120,000", "fine amount", "administrative fine"], "diagram": "alcohol_limit", "summary": "Drunk driving incurs fines ranging from NT$30,000 to NT$120,000 for cars, plus license suspension and vehicle impoundment."},
    {"id": "R08", "title": "8. Repeat Drunk Driving Violations within 10 Years", "kw": ["10 years", "repeat", "second time", "third time", "public disclosure"], "diagram": "alcohol_limit", "summary": "Repeat drunk driving within 10 years incurs escalating fines, license revocation, and public disclosure of name/photo."},
    {"id": "R09", "title": "9. Refusing Sobriety Breathalyzer Test Penalties (NT$180,000)", "kw": ["refus", "180,000", "breathalyzer", "sobriety test"], "diagram": "alcohol_limit", "summary": "Refusing a police breath alcohol test results in an immediate NT$180,000 fine, vehicle impoundment, and license revocation."},
    {"id": "R10", "title": "10. Passengers Joint Responsibility for Drunk Drivers", "kw": ["passenger", "same vehicle", "joint penalty", "knowingly"], "diagram": "alcohol_limit", "summary": "Passengers riding in a vehicle driven by an intoxicated driver are subject to fines of NT$6,000 to NT$15,000."},

    # --- Group 3: Cargo Loading & Dimension Limits (Rules 11-15) ---
    {"id": "R11", "title": "11. Motorcycle Cargo Length Limit (50 cm beyond rear axle)", "kw": ["50 cm", "rear axle", "motorcycle cargo", "rear wheel"], "diagram": "cargo_rear", "summary": "Motorcycle cargo must not extend forward past the rider seat or more than 50 cm beyond the rear wheel axle."},
    {"id": "R12", "title": "12. Motorcycle Cargo Width Limit (10 cm beyond handlebars)", "kw": ["10 cm", "handlebars", "motorcycle width", "load width"], "diagram": "cargo_rear", "summary": "Motorcycle cargo width must not extend more than 10 cm beyond the outer edges of the handlebars."},
    {"id": "R13", "title": "13. Motorcycle Cargo Weight Limits (Small 30kg / Light 60kg / Heavy 90kg)", "kw": ["30 kg", "60 kg", "90 kg", "weight limit", "load capacity"], "diagram": "cargo_rear", "summary": "Cargo weight limits: Small light motorcycle = 30 kg; Regular light = 60 kg; Heavy motorcycle = 90 kg."},
    {"id": "R14", "title": "14. Car Cargo Height Limit (Max 2.85m / 1.5x width)", "kw": ["2.85 meters", "1.5 times", "car cargo height", "overall height"], "diagram": "cargo_rear", "summary": "Small car cargo height must not exceed 1.5 times the vehicle overall width or a maximum height of 2.85 meters."},
    {"id": "R15", "title": "15. Cargo Protrusion & Falling Hazard Penalties", "kw": ["falling", "scattered", "protrud", "unsecured cargo", "falling onto road"], "diagram": "cargo_rear", "summary": "Cargo must be tightly covered and secured. Items falling onto the road carry severe fines and license demerit points."},

    # --- Group 4: Right-of-Way & Intersection Rules (Rules 16-22) ---
    {"id": "R16", "title": "16. Straight Vehicles Priority over Turning Vehicles", "kw": ["straight", "turning", "priority", "yield to straight"], "diagram": "right_of_way", "summary": "Vehicles proceeding straight have absolute right-of-way over vehicles turning into the same lane or intersection."},
    {"id": "R17", "title": "17. Left-Turning vs. Right-Turning Vehicle Priority", "kw": ["left turn", "right turn", "opposite direction", "same lane"], "diagram": "right_of_way", "summary": "When vehicles from opposite directions turn into the same lane, left-turning vehicles MUST yield to right-turning vehicles."},
    {"id": "R18", "title": "18. Unsignalized Intersection Equal Width Priority (Right Side Priority)", "kw": ["unsignalized", "equal width", "right side vehicle", "uncontrolled"], "diagram": "right_of_way", "summary": "At unsignalized intersections of equal road width, drivers MUST yield to vehicles approaching from their right side."},
    {"id": "R19", "title": "19. Branch Road vs. Main Road Priority", "kw": ["branch road", "main road", "side road", "wide road", "entering main"], "diagram": "right_of_way", "summary": "Vehicles entering from branch or side roads MUST stop and yield right-of-way to all traffic on the main road."},
    {"id": "R20", "title": "20. Pedestrian Zebra Crosswalk Priority (3 Meters Rule)", "kw": ["crosswalk", "pedestrian", "3 meters", "four zebra stripes", "yielding"], "diagram": "right_of_way", "summary": "Drivers MUST stop at least 3 meters (4 zebra stripes width) before crosswalks to yield to pedestrians."},
    {"id": "R21", "title": "21. Roundabout Traffic Priority", "kw": ["roundabout", "traffic circle", "inside roundabout", "entering roundabout"], "diagram": "right_of_way", "summary": "Vehicles entering a roundabout MUST yield right-of-way to vehicles already traveling inside the roundabout."},
    {"id": "R22", "title": "22. Yielding to Emergency Vehicles & Sirens", "kw": ["siren", "ambulance", "fire engine", "police car", "emergency vehicle"], "diagram": "siren_yield", "summary": "Drivers MUST immediately pull to the right and yield to emergency vehicles sounding sirens. Failure results in license revocation."},

    # --- Group 5: Road Markings, Signs & Signals (Rules 23-28) ---
    {"id": "R23", "title": "23. Solid Red Line (No Stopping 24 Hours)", "kw": ["solid red line", "no stopping", "24 hours", "red roadside line"], "diagram": "speed_limit_50", "summary": "Solid red roadside lines prohibit temporary stopping or parking 24 hours a day unless signed otherwise."},
    {"id": "R24", "title": "24. Solid Yellow Line (No Parking 7 AM - 8 PM)", "kw": ["solid yellow line", "no parking", "temporary stopping allowed", "7 a.m. to 8 p.m."], "diagram": "speed_limit_50", "summary": "Solid yellow roadside lines prohibit parking from 7 AM to 8 PM daily, but temporary stopping (<3 mins) is allowed."},
    {"id": "R25", "title": "25. Double Solid Yellow Lines (No Crossing / No Overtaking / No U-Turn)", "kw": ["double solid yellow", "no crossing", "center line", "no u-turn"], "diagram": "speed_limit_50", "summary": "Double solid yellow lines separate opposing traffic lanes. Crossing, straddling, or making U-turns over them is strictly illegal."},
    {"id": "R26", "title": "26. Inverted White Triangle Road Marking (Yield Line)", "kw": ["inverted triangle", "yield line", "white triangle", "give way marking"], "diagram": "right_of_way", "summary": "An inverted white triangle marked on the road surface indicates a Yield Line requiring drivers to slow down and yield."},
    {"id": "R27", "title": "27. Flashing Red Signal vs. Flashing Yellow Signal", "kw": ["flashing red", "flashing yellow", "stop line", "proceed with caution"], "diagram": "traffic_light", "summary": "Flashing Red = Complete stop before proceeding. Flashing Yellow = Slow down and proceed with heightened caution."},
    {"id": "R28", "title": "28. Police Officer Signals Superiority over Traffic Lights", "kw": ["police officer", "conflict", "signal light", "manual direction"], "diagram": "traffic_light", "summary": "Directions given by a police officer on site override all automated traffic light signals or road signs."},

    # --- Group 6: Driving Maneuvers & Turn Indicators (Rules 29-33) ---
    {"id": "R29", "title": "29. Turn Signal Advance Distance (30 Meters)", "kw": ["30 meters", "turn signal", "indicator", "before turning"], "diagram": "right_of_way", "summary": "Drivers MUST activate turn signals at least 30 meters before making turns or changing lanes on city streets."},
    {"id": "R30", "title": "30. Overtaking Regulations & Prohibited Locations", "kw": ["overtaking", "left side", "tunnel", "bridge", "curve", "railroad crossing"], "diagram": "right_of_way", "summary": "Overtake on the left side only. Overtaking is strictly prohibited in tunnels, on bridges, sharp curves, or railroad crossings."},
    {"id": "R31", "title": "31. U-Turn Restrictions & Prohibited Zones", "kw": ["u-turn", "slope", "steep grade", "narrow bridge", "tunnel"], "diagram": "right_of_way", "summary": "U-turns are prohibited on sharp curves, steep slopes, narrow bridges, tunnels, or where double solid yellow lines exist."},
    {"id": "R32", "title": "32. Reversing & Backing Up Restrictions", "kw": ["revers", "back up", "curve", "steep slope", "one-way road"], "diagram": "right_of_way", "summary": "Reversing is prohibited on steep slopes, sharp curves, narrow roads, or expressways unless avoiding obstacles."},
    {"id": "R33", "title": "33. Handheld Device Use Fine (Car NT$3,000 / Moto NT$1,000)", "kw": ["handheld", "mobile phone", "3,000", "1,000", "cellphone"], "diagram": "phone_fine", "summary": "Operating handheld mobile phones while driving incurs a fine of NT$3,000 for cars and NT$1,000 for motorcycles."},

    # --- Group 7: Highway & Freeway Regulations (Rules 34-37) ---
    {"id": "R34", "title": "34. Freeway Safe Following Distance Calculation", "kw": ["freeway following distance", "speed ÷ 2", "meters", "safe distance"], "diagram": "freeway_distance", "summary": "Freeway following distance for small cars: Speed (km/h) ÷ 2 = Minimum safe distance in meters (e.g. 100 km/h = 50 meters)."},
    {"id": "R35", "title": "35. Freeway Minimum Speed Limits & Lane Usage", "kw": ["innermost lane", "maximum speed", "minimum speed", "slow vehicle outer lane"], "diagram": "freeway_distance", "summary": "The innermost freeway lane is the overtaking lane; non-overtaking vehicles must travel at the maximum legal speed limit."},
    {"id": "R36", "title": "36. Hard Shoulder Driving Restrictions", "kw": ["hard shoulder", "roadside shoulder", "breakdown", "emergency stopping"], "diagram": "freeway_distance", "summary": "Driving on freeway hard shoulders is prohibited except during breakdowns, emergencies, or when signs indicate open shoulder."},
    {"id": "R37", "title": "37. Breakdown Warning Triangle Distance (100 Meters)", "kw": ["warning triangle", "100 meters", "breakdown", "behind vehicle"], "diagram": "freeway_distance", "summary": "Place warning triangles at least 100 meters behind a broken-down vehicle on freeways (30-100m on regular roads)."},

    # --- Group 8: Vehicle Equipment & Maintenance (Rules 38-42) ---
    {"id": "R38", "title": "38. Tire Tread Depth Minimum Standards (1.6mm Car / 1.0mm Moto)", "kw": ["1.6 mm", "1.0 mm", "tread depth", "wear indicator"], "diagram": "tire_tread", "summary": "Minimum tire tread depth is 1.6 mm for cars and 1.0 mm for motorcycles. Worn tires fail inspection and risk blowouts."},
    {"id": "R39", "title": "39. Mandatory Seatbelt Compliance & Child Seats", "kw": ["seatbelt", "front passenger", "rear passenger", "fasten"], "diagram": "seatbelt_law", "summary": "All occupants in cars MUST fasten seatbelts. Children under 4 must sit in rear seats in approved child safety seats."},
    {"id": "R40", "title": "40. Vehicle Door Opening 2-Stage Protocol", "kw": ["door opening", "two-stage", "check mirror", "shoulder check"], "diagram": "car_door", "summary": "Always use the 2-stage door opening method: look in mirrors, turn head to check blind spot, open door slightly, then alight."},
    {"id": "R41", "title": "41. Periodic Vehicle Inspection Schedule", "kw": ["periodic inspection", "10 years", "twice a year", "once a year"], "diagram": "demerit_points", "summary": "Private cars over 5 years old require annual inspection; cars over 10 years old require inspection twice per year."},
    {"id": "R42", "title": "42. Mandatory Liability Insurance Requirement", "kw": ["compulsory insurance", "liability insurance", "insurance card"], "diagram": "demerit_points", "summary": "All cars and motorcycles MUST carry active Compulsory Automobile Liability Insurance. Failure results in impoundment."},

    # --- Group 9: First Aid, Emergency Protocol & CPR (Rules 43-46) ---
    {"id": "R43", "title": "43. First Aid Priorities (Airway -> Bleeding -> Fracture)", "kw": ["airway", "bleeding", "fracture", "first aid priority", "order of treatment"], "diagram": "cpr_protocol", "summary": "First aid priority order: 1. Maintain open Airway (B). 2. Stop severe Bleeding (A). 3. Immobilize Fractures (C)."},
    {"id": "R44", "title": "44. CPR Chest Compression Ratio & Rate (30:2 / 100-120 bpm)", "kw": ["30:2", "100-120", "chest compression", "rescue breath", "cpr"], "diagram": "cpr_protocol", "summary": "Adult CPR standard: 30 chest compressions at 100-120 rate followed by 2 rescue breaths, compressing 5-6 cm deep."},
    {"id": "R45", "title": "45. Suspected Spinal Trauma Airway Method (Jaw-Thrust)", "kw": ["jaw-thrust", "spinal", "neck injury", "airway trauma"], "diagram": "cpr_protocol", "summary": "For victims with suspected neck/spinal trauma, use the Jaw-Thrust maneuver to open the airway without moving the neck."},
    {"id": "R46", "title": "46. Railroad Breakdown 3-Step SOS Procedure (Press -> Push -> Run)", "kw": ["sos button", "press push run", "emergency button", "railroad breakdown"], "diagram": "railroad_crossing", "summary": "Railroad breakdown SOS steps: 1. Press Emergency Red Button. 2. Push vehicle off tracks. 3. Run away from tracks."},

    # --- Group 10: Demerit Points, Fines & License Laws (Rules 47-50) ---
    {"id": "R47", "title": "47. Demerit Points Accumulation (12 Points in 1 Year = 2 Mo. Suspension)", "kw": ["demerit points", "12 points", "1 year", "2 months suspension"], "diagram": "demerit_points", "summary": "Accumulating 12 demerit points within 1 year results in a 2-month driver license suspension."},
    {"id": "R48", "title": "48. Hit-and-Run Penalties with Injury or Death", "kw": ["hit-and-run", "leaving scene", "injury or death", "license revoked"], "diagram": "demerit_points", "summary": "Fleeing the scene of an accident involving injury or death results in permanent driver license revocation and criminal charges."},
    {"id": "R49", "title": "49. Accident Scene Marking & Clearing Protocol", "kw": ["mark vehicle position", "no injuries", "move to roadside", "obstructing traffic"], "diagram": "demerit_points", "summary": "In minor accidents without injuries, drivers MUST photograph/mark vehicle positions and move vehicles to the roadside immediately."},
    {"id": "R50", "title": "50. Hazard Perception Defensive Driving Principles", "kw": ["defensive driving", "hazard perception", "anticipate", "blind spot", "rearview mirror"], "diagram": "right_of_way", "summary": "Defensive driving mandate: Constantly scan blind spots, monitor mirrors, slow at intersections, and anticipate hidden hazards."}
]

def generate_master_rules(qlist, module_prefix):
    cards = []
    for r in granular_topics:
        card_id = f"{module_prefix}_{r['id']}"
        
        # Search matching questions
        matched = [q for q in qlist if any(k in (q['question'] + ' ' + ' '.join(q['options']) + ' ' + q.get('explanation','')).lower() for k in r['kw'])]
        
        if not matched:
            # Fallback to category search
            matched = [q for q in qlist if any(k in q['category'].lower() for k in r['kw'])]
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

car_cards = generate_master_rules(car_qs, 'C')
moto_cards = generate_master_rules(moto_qs, 'M')

with open('car_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(car_cards, f, indent=2, ensure_ascii=False)

with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
    json.dump(moto_cards, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(car_cards)} Car Master Rules and {len(moto_cards)} Motorcycle Master Rules!")
