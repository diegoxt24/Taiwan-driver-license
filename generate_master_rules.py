import json

def generate_perfect_master_rules():
    # -------------------------------------------------------------
    # 1. MOTORCYCLE MASTER RULES (100% Motorcycle Specific)
    # -------------------------------------------------------------
    with open('questions.json', 'r', encoding='utf-8') as f:
        moto_qs = json.load(f)

    moto_rules_def = [
        {
            "id": "M_R01",
            "title": "1. Motorcycle Cargo Rear Extension Limit (Max 50 cm)",
            "keywords": ["rear axle", "50 cm", "extend", "rear wheel"],
            "summary": "Motorcycle cargo MUST NOT extend beyond the center of the rear wheel axle by more than 50 cm (0.5 meters). Violations carry traffic fines.",
            "key_fact": "Moto Rear Extension: Max 50 cm past rear axle",
            "diagram": "cargo_rear"
        },
        {
            "id": "M_R02",
            "title": "2. Motorcycle Side Cargo Width (Max 10 cm Past Handlebars)",
            "keywords": ["width", "handlebar", "10 cm"],
            "summary": "Motorcycle cargo width MUST NOT extend beyond the outer edge of the handlebars by more than 10 cm on either side.",
            "key_fact": "Moto Side Width: Max 10 cm past handlebar edge",
            "diagram": "cargo_rear"
        },
        {
            "id": "M_R03",
            "title": "3. Motorcycle Cargo Height & Weight Limits (80 kg / 50 kg)",
            "keywords": ["height", "shoulders", "80 kg", "50 kg", "70 kg"],
            "summary": "Cargo height must not exceed rider's shoulders (or total vehicle height of 2.0m). Max cargo weight: Heavy Motorcycle = 80 kg | Light Motorcycle = 50 kg.",
            "key_fact": "Heavy Moto Max Cargo: 80 kg | Light Moto: 50 kg",
            "diagram": "cargo_rear"
        },
        {
            "id": "M_R04",
            "title": "4. Motorcycle Two-Stage Left Turn (Hook Turn 兩段式左轉)",
            "keywords": ["hook turn", "two-stage", "兩段式"],
            "summary": "Motorcycles turning left at intersections with 'Two-Stage Left Turn' signs or on multi-lane roads with inner fast lane motorcycle prohibitions MUST perform a Two-Stage Hook Turn.",
            "key_fact": "Hook Turn Mandatory where Signed or Inner Lane Prohibited",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R05",
            "title": "5. Motorcycle Passenger Seat & Riding Position Rules",
            "keywords": ["side-saddle", "fixed rear seat", "1 passenger"],
            "summary": "Only 1 passenger is allowed on ordinary heavy/light motorcycles with a fixed rear seat. Side-saddle riding is strictly illegal. Small light motorcycles cannot carry any passengers.",
            "key_fact": "Max 1 Passenger, Fixed Seat Only (No Side-Saddle)",
            "diagram": "child_seat"
        },
        {
            "id": "M_R06",
            "title": "6. Motorcycle Minimum Tire Tread Depth (1.0 mm)",
            "keywords": ["1.0 mm", "tread depth", "motorcycle tire"],
            "summary": "Motorcycle tire tread depth across main grooves must be at least 1.0 mm. Replace tire immediately when tread wears down to the alignment bar.",
            "key_fact": "Motorcycle Min Tread Depth: 1.0 mm",
            "diagram": "tire_tread"
        },
        {
            "id": "M_R07",
            "title": "7. Helmet BSMI Certification & Chinstrap Rules",
            "keywords": ["helmet", "bsmi", "chinstrap"],
            "summary": "Riders and passengers MUST wear CNS/BSMI certified helmets. The helmet must fit properly and the chinstrap MUST be securely fastened under the jaw. Replace helmet after any severe impact.",
            "key_fact": "Helmets: BSMI Mark & Tight Chinstrap",
            "diagram": "tire_tread"
        },
        {
            "id": "M_R08",
            "title": "8. Motorcycle Drunk Driving 1st Offense Fine (NT$15,000–90,000)",
            "keywords": ["15,000", "90,000", "first offense", "drunk driving"],
            "summary": "First drunk driving offense fine for motorcycles is NT$15,000 to NT$90,000. Includes mandatory 1–2 year driver license suspension & vehicle impoundment.",
            "key_fact": "Moto Drunk Fine: NT$15,000–90,000",
            "diagram": "alcohol_limit"
        },
        {
            "id": "M_R09",
            "title": "9. Legal Breath Alcohol Concentration (BAC) Limit (0.15 mg/L)",
            "keywords": ["0.15 mg/l", "0.15", "0.03%"],
            "summary": "The legal BAC limit in Taiwan is 0.15 mg/L in breath (or 0.03% in blood). Testing at or above 0.15 mg/L constitutes illegal impaired driving.",
            "key_fact": "Legal BAC Threshold: 0.15 mg/L",
            "diagram": "alcohol_limit"
        },
        {
            "id": "M_R10",
            "title": "10. Refusing Sobriety Test Penalties (NT$180,000)",
            "keywords": ["refusing a breathalyzer", "refuse", "180,000"],
            "summary": "Refusing a police breathalyzer/sobriety test results in an immediate NT$180,000 fine, immediate driver license revocation, vehicle impoundment, and mandatory safety courses.",
            "key_fact": "Refusal: NT$180,000 Fine + License Revocation",
            "diagram": "alcohol_limit"
        },
        {
            "id": "M_R11",
            "title": "11. Motorcycle Handheld Phone Fine (NT$1,000)",
            "keywords": ["handheld mobile phone", "cellphone", "1,000 fine"],
            "summary": "Using a handheld mobile phone while riding a motorcycle incurs a mandatory administrative fine of NT$1,000.",
            "key_fact": "Motorcycle Phone Fine: NT$1,000",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R12",
            "title": "12. Standard Road Speed Limits (50 km/h Unmarked)",
            "keywords": ["unmarked", "50 km/h", "speed limit"],
            "summary": "On roads without posted speed limit signs or lane markings, the maximum legal speed limit is 50 km/h.",
            "key_fact": "Unmarked Roads: Max 50 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R13",
            "title": "13. Slow Lane & Narrow Road Speed Limits (40 km/h)",
            "keywords": ["slow lane", "40 km/h", "narrow road"],
            "summary": "On designated slow lanes or narrow roads without lane dividing lines, the maximum legal speed limit is 40 km/h.",
            "key_fact": "Slow Lane / Narrow Road: Max 40 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R14",
            "title": "14. Railroad Level Crossing Approach Speed (15 km/h)",
            "keywords": ["railroad", "level crossing", "15 km/h"],
            "summary": "When approaching a railroad level crossing, riders MUST reduce speed to 15 km/h or less and prepare to stop at least 3 to 6 meters before tracks when signals flash.",
            "key_fact": "Railroad Approach: Max 15 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R15",
            "title": "15. Speed vs. Braking Distance Physics (Double Speed = 4x Distance)",
            "keywords": ["braking distance", "doubles", "4 times"],
            "summary": "Braking distance is proportional to the square of speed. If your speed doubles (e.g. from 40 to 80 km/h), your required stopping distance becomes 4 times greater!",
            "key_fact": "Double Speed = 4x Braking Distance",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R16",
            "title": "16. Failing to Yield to Emergency Sirens (License Revocation)",
            "keywords": ["ambulance", "fire engine", "siren"],
            "summary": "Failing to immediately pull over and yield to an emergency vehicle sounding sirens results in a heavy fine AND immediate driver license revocation!",
            "key_fact": "Not Yielding to Siren = License Revocation",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R17",
            "title": "17. Horn Tap Usage Rules (Max 0.5s per tap, Max 3 Taps)",
            "keywords": ["0.5 seconds", "3 consecutive taps"],
            "summary": "Horn usage rule: Each tap must not exceed 0.5 seconds, with no more than 3 consecutive taps permitted.",
            "key_fact": "Horn: Max 0.5 sec per tap, max 3 taps",
            "diagram": "tire_tread"
        },
        {
            "id": "M_R18",
            "title": "18. Headlight Low-Beam / High-Beam Usage at Night",
            "keywords": ["high-beam", "low-beam", "oncoming traffic"],
            "summary": "When meeting oncoming vehicles at night or following behind another vehicle within 100 meters, you MUST switch from high-beams to low-beams. Do NOT use high-beams to retaliate.",
            "key_fact": "Oncoming Traffic: Must Use Low-Beams",
            "diagram": "tire_tread"
        },
        {
            "id": "M_R19",
            "title": "19. Unsignalized Intersection Priority (Straight Vehicle #1)",
            "keywords": ["straight-going", "unsignalized", "right-of-way"],
            "summary": "At unsignalized intersections of equal road width, straight-going vehicles have absolute right-of-way over turning vehicles.",
            "key_fact": "Priority #1: Straight-Going Vehicle",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R20",
            "title": "20. Left Turn vs. Right Turn Priority",
            "keywords": ["left-turning", "right-turning", "yield right-of-way"],
            "summary": "When two vehicles from opposite directions are turning into the same lane, the left-turning vehicle MUST yield right-of-way to the right-turning vehicle.",
            "key_fact": "Left Turn Yields to Right Turn",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R21",
            "title": "21. Narrow Road vs. Wide Main Road Rules",
            "keywords": ["narrow road", "wide road", "main road"],
            "summary": "Vehicles coming from a narrow road or side lane MUST stop and yield right-of-way to vehicles on the wider main road.",
            "key_fact": "Narrow Road Yields to Main Road",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R22",
            "title": "22. Pedestrian Crosswalk Absolute Right of Way",
            "keywords": ["crosswalk", "pedestrian", "zebra"],
            "summary": "Drivers and riders MUST stop and yield to pedestrians crossing on a crosswalk (zebra crossing). Violating pedestrian right-of-way incurs heavy fines and mandatory safety courses.",
            "key_fact": "Absolute Priority: Pedestrians on Crosswalk",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R23",
            "title": "23. Turn Signal Distance Requirement (30 meters)",
            "keywords": ["30 meters", "turn signal"],
            "summary": "You MUST activate your turn signals at least 30 meters before making any turn or lane change on ordinary roads.",
            "key_fact": "Turn Signal: At least 30 meters before turn",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R24",
            "title": "24. Prohibited U-Turn Locations & Markings",
            "keywords": ["double solid yellow", "u-turn"],
            "summary": "U-turns are strictly prohibited on roads marked with double solid yellow lines, solid white lines, steep slopes, sharp curves, or railroad crossings.",
            "key_fact": "U-Turn Prohibited on Double Yellow Lines",
            "diagram": "right_of_way"
        },
        {
            "id": "M_R25",
            "title": "25. CPR Compression-to-Ventilation Ratio (30:2)",
            "keywords": ["30 compressions", "2 breaths", "cpr"],
            "summary": "Standard CPR protocol for cardiac arrest is 30 chest compressions followed by 2 rescue breaths (30:2 ratio).",
            "key_fact": "CPR Ratio: 30 Compressions : 2 Breaths",
            "diagram": "child_seat"
        },
        {
            "id": "M_R26",
            "title": "26. CPR Compression Depth & Rate (5-6 cm & 100-120/min)",
            "keywords": ["5–6 cm", "100–120"],
            "summary": "Chest compressions must be delivered at a rate of 100 to 120 compressions per minute, reaching a depth of 5 to 6 cm on the center of the sternum.",
            "key_fact": "Depth: 5-6 cm | Rate: 100-120/min",
            "diagram": "child_seat"
        },
        {
            "id": "M_R27",
            "title": "27. Brain Oxygen Deprivation Window (4 to 6 minutes)",
            "keywords": ["4–6 minutes", "brain damage"],
            "summary": "Irreversible brain damage begins within 4 to 6 minutes of cardiac/respiratory arrest. CPR must begin immediately.",
            "key_fact": "Brain Damage Window: 4 to 6 Minutes",
            "diagram": "child_seat"
        },
        {
            "id": "M_R28",
            "title": "28. Spinal Injury Airway Clear (Jaw-Thrust Maneuver)",
            "keywords": ["jaw-thrust", "spinal"],
            "summary": "For an unconscious victim with suspected neck/spinal trauma, clear the airway using the Jaw-thrust maneuver without tilting the head back.",
            "key_fact": "Spinal Trauma: Use Jaw-Thrust (No Head Tilt)",
            "diagram": "child_seat"
        },
        {
            "id": "M_R29",
            "title": "29. Heimlich Maneuver Fist Position (Between Navel & Sternum)",
            "keywords": ["heimlich", "navel"],
            "summary": "When performing the Heimlich maneuver on a choking victim, place your fist between the navel and the bottom of the sternum, thrusting inward and upward.",
            "key_fact": "Heimlich Position: Between Navel & Sternum",
            "diagram": "child_seat"
        },
        {
            "id": "M_R30",
            "title": "30. Railroad Crossing Breakdown Emergency Button Protocol",
            "keywords": ["emergency button", "level crossing"],
            "summary": "If a vehicle breaks down on a railroad level crossing: 1. Immediately press the Emergency Button (緊急按鈕). 2. Push vehicle clear if possible. 3. Evacuate passengers to safety.",
            "key_fact": "Breakdown on Tracks = Press Emergency Button Immediately",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R31",
            "title": "31. Running Red Light Fines & Demerit Points",
            "keywords": ["running a red light", "3 demerit"],
            "summary": "Running a red light incurs fines (NT$1,800–5,400) PLUS 3 demerit points on your driving record.",
            "key_fact": "Red Light: Fine + 3 Demerit Points",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R32",
            "title": "32. Demerit Point Suspension Threshold (12 Points in 1 Year)",
            "keywords": ["12 demerit points", "2-month"],
            "summary": "Accumulating 12 demerit points within 1 year results in a mandatory 2-month driver license suspension.",
            "key_fact": "12 Demerits in 1 Year = 2-Month Suspension",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R33",
            "title": "33. Temporary Parking Rule (Max 3 Minutes, Rider Ready)",
            "keywords": ["temporary parking", "3 minutes"],
            "summary": "Temporary parking is permitted for a maximum of 3 minutes, and the rider MUST remain ready to move the vehicle immediately.",
            "key_fact": "Temporary Parking: Max 3 Mins & Driver in Seat",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R34",
            "title": "34. Prohibited Stopping Distance (10 meters from Intersections)",
            "keywords": ["10 meters", "bus stop"],
            "summary": "Stopping or parking is strictly prohibited within 10 meters of intersections, bus stops, fire hydrants, or fire stations.",
            "key_fact": "No Stopping Within 10m of Intersections/Bus Stops",
            "diagram": "speed_limit"
        },
        {
            "id": "M_R35",
            "title": "35. Traffic Light Indications (Solid Red / Flashing Red / Flashing Yellow)",
            "keywords": ["solid red circular", "flashing red", "flashing yellow"],
            "summary": "Solid Red = Complete stop behind stop line. Flashing Red = Stop completely and yield right-of-way. Flashing Yellow = Exercise caution and slow down.",
            "key_fact": "Flashing Red = Stop & Yield | Flashing Yellow = Caution",
            "diagram": "speed_limit"
        }
    ]

    moto_cards = []
    for r in moto_rules_def:
        matched_qs = [q for q in moto_qs if any(kw in (q['question'] + " " + q.get('explanation', '')).lower() for kw in r['keywords'])]
        canonical = matched_qs[0] if matched_qs else moto_qs[0]
        moto_cards.append({
            "id": r["id"], "title": r["title"], "summary": r["summary"], "key_fact": r["key_fact"], "diagram": r["diagram"],
            "canonical_question": canonical["question"], "canonical_options": canonical["options"],
            "canonical_correct": canonical["correct_answer"], "canonical_correct_index": canonical["correct_index"],
            "matched_question_count": len(matched_qs), "matched_question_ids": [q["id"] for q in matched_qs]
        })

    with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
        json.dump(moto_cards, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(moto_cards)} PERFECT Motorcycle Master Rule Cards.")

    # -------------------------------------------------------------
    # 2. CAR MASTER RULES (100% Car Specific & Perfectly Matched)
    # -------------------------------------------------------------
    with open('car_questions.json', 'r', encoding='utf-8') as f:
        car_qs = json.load(f)

    car_rules_def = [
        {
            "id": "C_R01",
            "title": "1. Passenger Car Cargo Limits (30 cm Bumper Extension)",
            "keywords": ["front and rear cargo extension", "30 cm"],
            "summary": "Cargo carried on small passenger cars must not extend past front or rear bumpers by more than 30 cm, nor exceed vehicle total length of 12m or body width (max 2.5m).",
            "key_fact": "Car Cargo Bumper Extension: Max 30 cm",
            "diagram": "cargo_rear"
        },
        {
            "id": "C_R02",
            "title": "2. Child Safety Seat Law (Under 4 yrs / 18 kg)",
            "keywords": ["children under 4 years old", "18 kg"],
            "summary": "Children under 4 years old or weighing under 18 kg MUST be seated in an approved rear-facing child safety seat installed in the REAR seat of the vehicle.",
            "key_fact": "Under 4 yrs / 18 kg: Mandatory Rear Child Safety Seat",
            "diagram": "child_seat"
        },
        {
            "id": "C_R03",
            "title": "3. Front Passenger Seat Age Restriction (12 years old)",
            "keywords": ["under 12 years of age", "front passenger seat"],
            "summary": "Children under 12 years of age are strictly prohibited from sitting in the front passenger seat of any automobile.",
            "key_fact": "Under 12 yrs: Prohibited from Front Seat",
            "diagram": "child_seat"
        },
        {
            "id": "C_R04",
            "title": "4. Opening Car Door Accident Fine (NT$2,400–4,800)",
            "keywords": ["opening a car door", "door accident", "2,400"],
            "summary": "Opening a car door without checking rear traffic and causing an accident incurs a fine of NT$2,400 to NT$4,800.",
            "key_fact": "Careless Door Opening Fine: NT$2,400–4,800",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R05",
            "title": "5. Passenger Car Minimum Tire Tread Depth (1.6 mm)",
            "keywords": ["minimum legal tire tread depth", "1.6 mm"],
            "summary": "Passenger car tire tread depth must be at least 1.6 mm. Failing tread depth during periodic inspection results in mandatory 1-month re-inspection or license plate suspension.",
            "key_fact": "Passenger Car Min Tread Depth: 1.6 mm",
            "diagram": "tire_tread"
        },
        {
            "id": "C_R06",
            "title": "6. Freeway Safe Following Distance Rule (Speed ÷ 2)",
            "keywords": ["freeway with a speed limit of 100", "following distance"],
            "summary": "Under dry weather conditions on freeways, small passenger cars must maintain a safe following distance equal to Speed ÷ 2 in meters (e.g. 100 km/h = 50m distance).",
            "key_fact": "Safe Distance = Speed ÷ 2 (50m @ 100km/h)",
            "diagram": "freeway_distance"
        },
        {
            "id": "C_R07",
            "title": "7. Freeway Wet Weather / Heavy Rain Distance Rule",
            "keywords": ["heavy rain, fog, or wet road", "double their standard"],
            "summary": "During heavy rain, fog, or wet road conditions on freeways, drivers MUST double their standard safe following distance.",
            "key_fact": "Wet Road: Double Following Distance",
            "diagram": "freeway_distance"
        },
        {
            "id": "C_R08",
            "title": "8. Freeway Breakdown Warning Triangle Distance (100 meters)",
            "keywords": ["breaks down on a national freeway", "100 meters"],
            "summary": "In the event of a vehicle breakdown on a freeway or expressway, place the red warning triangle 100 meters behind the vehicle on the shoulder/lane.",
            "key_fact": "Freeway Breakdown Triangle: 100m Behind",
            "diagram": "freeway_distance"
        },
        {
            "id": "C_R09",
            "title": "9. Freeway Inner Lane Minimum Speed Rule",
            "keywords": ["innermost overtaking lane", "maximum posted speed"],
            "summary": "The innermost lane on freeways is designated as the overtaking lane. Vehicles traveling in the inner lane MUST maintain the maximum posted speed limit for that segment (e.g. 90-110 km/h).",
            "key_fact": "Inner Lane: Must Maintain Max Speed Limit",
            "diagram": "freeway_distance"
        },
        {
            "id": "C_R10",
            "title": "10. Freeway Hard Shoulder Driving Prohibition",
            "keywords": ["hard shoulder of a national freeway", "prohibited"],
            "summary": "Driving on the hard shoulder of a freeway is strictly prohibited unless emergency signs explicitly open the shoulder during rush hours or during breakdown emergencies.",
            "key_fact": "Hard Shoulder Driving Prohibited",
            "diagram": "freeway_distance"
        },
        {
            "id": "C_R11",
            "title": "11. Car Drunk Driving 1st Offense Fine (NT$30,000–120,000)",
            "keywords": ["first-offense drunk driving violation", "30,000"],
            "summary": "First drunk driving offense fine for passenger cars is NT$30,000 to NT$120,000. Includes mandatory 1–2 year driver license suspension & vehicle impoundment.",
            "key_fact": "Car Drunk Fine: NT$30,000–120,000",
            "diagram": "alcohol_limit"
        },
        {
            "id": "C_R12",
            "title": "12. Legal Breath Alcohol Concentration (BAC) Limit (0.15 mg/L)",
            "keywords": ["legal breath alcohol concentration", "0.15 mg/l"],
            "summary": "The legal BAC limit in Taiwan is 0.15 mg/L in breath (or 0.03% in blood). Testing at or above 0.15 mg/L constitutes illegal impaired driving.",
            "key_fact": "Legal BAC Threshold: 0.15 mg/L",
            "diagram": "alcohol_limit"
        },
        {
            "id": "C_R13",
            "title": "13. Refusing Sobriety Test Penalties (NT$180,000)",
            "keywords": ["refusing a breathalyzer test", "180,000"],
            "summary": "Refusing a police breathalyzer/sobriety test results in an immediate NT$180,000 fine, immediate driver license revocation, vehicle impoundment, and mandatory safety courses.",
            "key_fact": "Refusal: NT$180,000 Fine + License Revocation",
            "diagram": "alcohol_limit"
        },
        {
            "id": "C_R14",
            "title": "14. Car Handheld Phone Fine (NT$3,000)",
            "keywords": ["handheld mobile phone while driving a car", "3,000"],
            "summary": "Using a handheld mobile phone while driving a car incurs a mandatory administrative fine of NT$3,000.",
            "key_fact": "Car Phone Fine: NT$3,000",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R15",
            "title": "15. Seatbelt Enforcement Law (All Occupants Mandatory)",
            "keywords": ["passengers in a small passenger car", "seat belts"],
            "summary": "All occupants inside a passenger car (both front and rear seat passengers) MUST wear seatbelts at all times while the vehicle is in motion.",
            "key_fact": "Seatbelts: Mandatory for ALL Occupants",
            "diagram": "child_seat"
        },
        {
            "id": "C_R16",
            "title": "16. Standard Road Speed Limits (50 km/h Unmarked)",
            "keywords": ["ordinary urban roads without lane separation", "50 km/h"],
            "summary": "On roads without posted speed limit signs or lane markings, the maximum legal speed limit is 50 km/h.",
            "key_fact": "Unmarked Roads: Max 50 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R17",
            "title": "17. Slow Lane & Narrow Road Speed Limits (40 km/h)",
            "keywords": ["slow lane or narrow road", "40 km/h"],
            "summary": "On designated slow lanes or narrow roads without lane dividing lines, the maximum legal speed limit is 40 km/h.",
            "key_fact": "Slow Lane / Narrow Road: Max 40 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R18",
            "title": "18. Railroad Level Crossing Approach Speed (15 km/h)",
            "keywords": ["railroad level crossing", "15 km/h"],
            "summary": "When approaching a railroad level crossing, drivers MUST reduce speed to 15 km/h or less and prepare to stop at least 3 to 6 meters before tracks when signals flash.",
            "key_fact": "Railroad Approach: Max 15 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R19",
            "title": "19. Speed vs. Braking Distance Physics (Double Speed = 4x Distance)",
            "keywords": ["braking distance is proportional", "4 times"],
            "summary": "Braking distance is proportional to the square of speed. If your speed doubles (e.g. from 40 to 80 km/h), your required stopping distance becomes 4 times greater!",
            "key_fact": "Double Speed = 4x Braking Distance",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R20",
            "title": "20. Failing to Yield to Emergency Sirens (License Revocation)",
            "keywords": ["siren of an approaching ambulance", "revoked"],
            "summary": "Failing to immediately pull over and yield to an emergency vehicle sounding sirens results in a heavy fine AND immediate driver license revocation!",
            "key_fact": "Not Yielding to Siren = License Revocation",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R21",
            "title": "21. Unsignalized Intersection Priority (Straight Vehicle #1)",
            "keywords": ["unsignalized intersection of equal road width", "straight"],
            "summary": "At unsignalized intersections of equal road width, straight-going vehicles have absolute right-of-way over turning vehicles.",
            "key_fact": "Priority #1: Straight-Going Vehicle",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R22",
            "title": "22. Left Turn vs. Right Turn Priority",
            "keywords": ["left-turning vehicle yields", "right-turning"],
            "summary": "When two vehicles from opposite directions are turning into the same lane, the left-turning vehicle MUST yield right-of-way to the right-turning vehicle.",
            "key_fact": "Left Turn Yields to Right Turn",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R23",
            "title": "23. Narrow Road vs. Wide Main Road Rules",
            "keywords": ["narrow road or side lane", "main road"],
            "summary": "Vehicles coming from a narrow road or side lane MUST stop and yield right-of-way to vehicles on the wider main road.",
            "key_fact": "Narrow Road Yields to Main Road",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R24",
            "title": "24. Pedestrian Crosswalk Absolute Right of Way",
            "keywords": ["yield to pedestrians crossing", "crosswalk"],
            "summary": "Drivers MUST stop and yield to pedestrians crossing on a crosswalk (zebra crossing). Violating pedestrian right-of-way incurs heavy fines and mandatory safety courses.",
            "key_fact": "Absolute Priority: Pedestrians on Crosswalk",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R25",
            "title": "25. Turn Signal Distance Requirement (30 meters)",
            "keywords": ["activate turn signals at least 30", "30 meters"],
            "summary": "You MUST activate your turn signals at least 30 meters before making any turn or lane change on ordinary roads (100m on expressways).",
            "key_fact": "Turn Signal: At least 30 meters before turn",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R26",
            "title": "26. Prohibited U-Turn Locations & Markings",
            "keywords": ["double solid yellow lines", "u-turn"],
            "summary": "U-turns are strictly prohibited on roads marked with double solid yellow lines, solid white lines, steep slopes, sharp curves, or railroad crossings.",
            "key_fact": "U-Turn Prohibited on Double Yellow Lines",
            "diagram": "right_of_way"
        },
        {
            "id": "C_R27",
            "title": "27. CPR Compression-to-Ventilation Ratio (30:2)",
            "keywords": ["chest compression to rescue breath ratio", "30 compressions"],
            "summary": "Standard CPR protocol for cardiac arrest is 30 chest compressions followed by 2 rescue breaths (30:2 ratio).",
            "key_fact": "CPR Ratio: 30 Compressions : 2 Breaths",
            "diagram": "child_seat"
        },
        {
            "id": "C_R28",
            "title": "28. CPR Compression Depth & Rate (5-6 cm & 100-120/min)",
            "keywords": ["compression depth and rate", "5–6 cm"],
            "summary": "Chest compressions must be delivered at a rate of 100 to 120 compressions per minute, reaching a depth of 5 to 6 cm on the center of the sternum.",
            "key_fact": "Depth: 5-6 cm | Rate: 100-120/min",
            "diagram": "child_seat"
        },
        {
            "id": "C_R29",
            "title": "29. Brain Oxygen Deprivation Window (4 to 6 minutes)",
            "keywords": ["irreversible brain damage", "4–6 minutes"],
            "summary": "Irreversible brain damage begins within 4 to 6 minutes of cardiac/respiratory arrest. CPR must begin immediately.",
            "key_fact": "Brain Damage Window: 4 to 6 Minutes",
            "diagram": "child_seat"
        },
        {
            "id": "C_R30",
            "title": "30. Spinal Injury Airway Clear (Jaw-Thrust Maneuver)",
            "keywords": ["unconscious victim with suspected neck", "jaw-thrust"],
            "summary": "For an unconscious victim with suspected neck/spinal trauma, clear the airway using the Jaw-thrust maneuver without tilting the head back.",
            "key_fact": "Spinal Trauma: Use Jaw-Thrust (No Head Tilt)",
            "diagram": "child_seat"
        },
        {
            "id": "C_R31",
            "title": "31. Heimlich Maneuver Fist Position (Between Navel & Sternum)",
            "keywords": ["performing the heimlich maneuver", "navel"],
            "summary": "When performing the Heimlich maneuver on a choking victim, place your fist between the navel and the bottom of the sternum, thrusting inward and upward.",
            "key_fact": "Heimlich Position: Between Navel & Sternum",
            "diagram": "child_seat"
        },
        {
            "id": "C_R32",
            "title": "32. Railroad Crossing Breakdown Emergency Button Protocol",
            "keywords": ["breaks down on a railroad level crossing", "emergency button"],
            "summary": "If a vehicle breaks down on a railroad level crossing: 1. Immediately press the Emergency Button (緊急按鈕). 2. Push vehicle clear if possible. 3. Evacuate passengers to safety.",
            "key_fact": "Breakdown on Tracks = Press Emergency Button Immediately",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R33",
            "title": "33. Running Red Light Fines & Demerit Points",
            "keywords": ["red light in a car", "2,700"],
            "summary": "Running a red light in a car incurs fines (NT$2,700–5,400) PLUS 3 demerit points on your driving record.",
            "key_fact": "Car Red Light: Fine NT$2.7k–5.4k + 3 Demerit Points",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R34",
            "title": "34. Demerit Point Suspension Threshold (12 Points in 1 Year)",
            "keywords": ["12 demerit points within 1 year", "2-month"],
            "summary": "Accumulating 12 demerit points within 1 year results in a mandatory 2-month driver license suspension.",
            "key_fact": "12 Demerits in 1 Year = 2-Month Suspension",
            "diagram": "speed_limit"
        },
        {
            "id": "C_R35",
            "title": "35. Traffic Light Indications (Solid Red / Flashing Red / Flashing Yellow)",
            "keywords": ["solid red circular traffic signal", "flashing red"],
            "summary": "Solid Red = Complete stop behind stop line. Flashing Red = Stop completely and yield right-of-way. Flashing Yellow = Exercise caution and slow down.",
            "key_fact": "Flashing Red = Stop & Yield | Flashing Yellow = Caution",
            "diagram": "speed_limit"
        }
    ]

    car_cards = []
    for r in car_rules_def:
        matched_qs = [q for q in car_qs if any(kw in (q['question'] + " " + q.get('explanation', '')).lower() for kw in r['keywords'])]
        canonical = matched_qs[0] if matched_qs else car_qs[0]
        car_cards.append({
            "id": r["id"], "title": r["title"], "summary": r["summary"], "key_fact": r["key_fact"], "diagram": r["diagram"],
            "canonical_question": canonical["question"], "canonical_options": canonical["options"],
            "canonical_correct": canonical["correct_answer"], "canonical_correct_index": canonical["correct_index"],
            "matched_question_count": len(matched_qs), "matched_question_ids": [q["id"] for q in matched_qs]
        })

    with open('car_master_rules.json', 'w', encoding='utf-8') as f:
        json.dump(car_cards, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(car_cards)} PERFECT Car Master Rule Cards.")

generate_perfect_master_rules()
