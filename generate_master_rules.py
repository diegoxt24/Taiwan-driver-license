import json

def expand_master_rules(q_filename, out_filename, is_car=False):
    with open(q_filename, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # 35 Fine-grained granular Master Rules covering every single sub-topic
    detailed_rules = [
        # CARGO & DIMENSIONS
        {
            "id": "R01",
            "title": "Motorcycle Cargo Rear Extension Limit (50 cm)",
            "keywords": ["rear", "axle", "50 cm", "extend"],
            "summary": "Motorcycle cargo MUST NOT extend beyond the center of the rear wheel axle by more than 50 cm (0.5 meters). Violations carry traffic fines.",
            "key_fact": "Rear Extension: Max 50 cm",
            "diagram": "cargo_rear"
        },
        {
            "id": "R02",
            "title": "Motorcycle Cargo Width & Handlebar Limits (10 cm)",
            "keywords": ["width", "handlebar", "10 cm"],
            "summary": "Motorcycle cargo width MUST NOT extend beyond the outer edge of the handlebars by more than 10 cm on either side.",
            "key_fact": "Side Width: Max 10 cm past handlebar",
            "diagram": "cargo_rear"
        },
        {
            "id": "R03",
            "title": "Motorcycle Cargo Height & Weight Limits",
            "keywords": ["height", "shoulders", "80 kg", "50 kg", "70 kg"],
            "summary": "Cargo height must not exceed rider's shoulders (or 2.0 meters total vehicle height). Weight limits: Heavy Motorcycle = 80 kg max | Light Motorcycle = 50 kg max.",
            "key_fact": "Heavy Moto Max: 80 kg | Light Moto: 50 kg",
            "diagram": "cargo_rear"
        },
        {
            "id": "R04",
            "title": "Passenger Car Cargo Bumper Limits (30 cm)",
            "keywords": ["bumper", "30 cm", "car cargo", "12 meters"],
            "summary": "Cargo carried on small passenger cars must not extend past the front or rear bumpers by more than 30 cm, nor exceed total vehicle length of 12 meters.",
            "key_fact": "Car Bumper Extension: Max 30 cm",
            "diagram": "cargo_rear"
        },

        # ALCOHOL & IMPAIRED DRIVING
        {
            "id": "R05",
            "title": "Legal Breath Alcohol Concentration (BAC) Limit (0.15 mg/L)",
            "keywords": ["0.15", "bac", "breath alcohol", "0.03%"],
            "summary": "The legal BAC limit is 0.15 mg/L in breath (or 0.03% in blood). Any level at or above 0.15 mg/L constitutes illegal impaired driving.",
            "key_fact": "Legal BAC Threshold: 0.15 mg/L",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R06",
            "title": "First Drunk Driving Offense Penalties",
            "keywords": ["first offense", "15,000", "30,000", "90,000", "120,000"],
            "summary": "First drunk driving offense fines: Motorcycle = NT$15,000–90,000 | Car = NT$30,000–120,000. Includes mandatory 1–2 year driver license suspension & vehicle impoundment.",
            "key_fact": "Moto NT$15k–90k | Car NT$30k–120k",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R07",
            "title": "Refusing Sobriety Test Penalties (NT$180,000)",
            "keywords": ["refus", "sobriety test", "180,000", "revocation"],
            "summary": "Refusing a police breathalyzer test incurs an immediate NT$180,000 fine, immediate driver license revocation, vehicle impoundment, and mandatory safety courses.",
            "key_fact": "Refusal Fine: NT$180,000 + License Revocation",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R08",
            "title": "Drunk Driver Passenger Liability Fine (NT$6,000–15,000)",
            "keywords": ["passenger", "18", "drunk driver", "6,000"],
            "summary": "Passengers aged 18 or older riding in a vehicle operated by a drunk driver face mandatory administrative fines of NT$6,000 to NT$15,000.",
            "key_fact": "Passenger Fine: NT$6,000–15,000",
            "diagram": "alcohol_limit"
        },

        # SPEED LIMITS & BRAKING DISTANCE
        {
            "id": "R09",
            "title": "Standard Road Speed Limits (50 km/h Unmarked)",
            "keywords": ["unmarked", "50 km/h", "speed limit"],
            "summary": "On roads without posted speed limit signs or lane markings, the maximum legal speed limit is 50 km/h.",
            "key_fact": "Unmarked Roads: Max 50 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "R10",
            "title": "Slow Lane & Narrow Road Speed Limits (40 km/h)",
            "keywords": ["slow lane", "40 km/h", "narrow road"],
            "summary": "On designated slow lanes or narrow roads without lane dividing lines, the maximum legal speed limit is 40 km/h.",
            "key_fact": "Slow Lane / Narrow Road: Max 40 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "R11",
            "title": "Railroad Level Crossing Speed Limit (15 km/h)",
            "keywords": ["railroad", "level crossing", "15 km/h"],
            "summary": "When approaching a railroad level crossing, drivers/riders MUST reduce speed to 15 km/h or less and prepare to stop at least 3 to 6 meters before the tracks when signals flash.",
            "key_fact": "Railroad Approach: Max 15 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "R12",
            "title": "Speed vs. Braking Distance Physics (Double Speed = 4x Distance)",
            "keywords": ["doubles", "braking distance", "4 times", "quadruples"],
            "summary": "Braking distance is proportional to the square of speed ($d \propto v^2$). If your speed doubles (e.g. from 40 to 80 km/h), your required stopping distance becomes 4 times greater!",
            "key_fact": "Double Speed = 4x Braking Distance",
            "diagram": "speed_limit"
        },

        # TIRE TREAD & EQUIPMENT
        {
            "id": "R13",
            "title": "Motorcycle Minimum Tire Tread Depth (1.0 mm)",
            "keywords": ["1.0 mm", "tread", "motorcycle tire"],
            "summary": "Motorcycle tire tread depth across main grooves must be at least 1.0 mm. Replace tire immediately when tread wears down to the alignment bar.",
            "key_fact": "Moto Min Tread: 1.0 mm",
            "diagram": "tire_tread"
        },
        {
            "id": "R14",
            "title": "Passenger Car Minimum Tire Tread Depth (1.6 mm)",
            "keywords": ["1.6 mm", "tread", "car tire"],
            "summary": "Passenger car tire tread depth must be at least 1.6 mm. Failing tread depth during periodic inspection results in mandatory 1-month re-inspection or license plate suspension.",
            "key_fact": "Car Min Tread: 1.6 mm",
            "diagram": "tire_tread"
        },
        {
            "id": "R15",
            "title": "Helmet Certification & Safety Strap Rules",
            "keywords": ["helmet", "bsmi", "chinstrap", "strap"],
            "summary": "Riders and passengers MUST wear CNS/BSMI certified helmets. The helmet must fit properly and the chinstrap MUST be securely fastened under the jaw. Replace helmet after any severe impact.",
            "key_fact": "Helmets: Must have BSMI mark & tight strap",
            "diagram": "tire_tread"
        },
        {
            "id": "R16",
            "title": "Vehicle Horn Tap Usage Rule",
            "keywords": ["horn", "0.5 second", "3 consecutive"],
            "summary": "Horn usage rule: Each tap must not exceed 0.5 seconds, with no more than 3 consecutive taps permitted.",
            "key_fact": "Horn: Max 0.5 sec per tap, max 3 taps",
            "diagram": "tire_tread"
        },

        # RIGHT OF WAY & INTERSECTIONS
        {
            "id": "R17",
            "title": "Unsignalized Intersection Priority (Straight-Going Vehicle #1)",
            "keywords": ["straight", "turning", "priority", "unsignalized"],
            "summary": "At unsignalized intersections of equal road width, straight-going vehicles have absolute right-of-way over turning vehicles.",
            "key_fact": "Priority #1: Straight-Going Vehicle",
            "diagram": "right_of_way"
        },
        {
            "id": "R18",
            "title": "Left Turn vs. Right Turn Priority",
            "keywords": ["left turn", "right turn", "yield"],
            "summary": "When two vehicles from opposite directions are turning into the same lane, the left-turning vehicle MUST yield right-of-way to the right-turning vehicle.",
            "key_fact": "Left Turn Yields to Right Turn",
            "diagram": "right_of_way"
        },
        {
            "id": "R19",
            "title": "Narrow Road vs. Wide Road Intersection Rules",
            "keywords": ["narrow road", "wide road", "main road"],
            "summary": "Vehicles coming from a narrow road or side lane MUST stop and yield right-of-way to vehicles on the wider main road.",
            "key_fact": "Narrow Road Yields to Main/Wide Road",
            "diagram": "right_of_way"
        },

        # TURNING & SIGNALS
        {
            "id": "R20",
            "title": "Turn Signal Distance Requirement (30 meters)",
            "keywords": ["30 meters", "turn signal", "changing lanes"],
            "summary": "You MUST activate your turn signals at least 30 meters before making any turn or lane change on ordinary roads (100m on expressways).",
            "key_fact": "Turn Signal: At least 30 meters before turn",
            "diagram": "right_of_way"
        },
        {
            "id": "R21",
            "title": "Motorcycle Two-Stage Left Turn (Hook Turn 兩段式左轉)",
            "keywords": ["hook turn", "two-stage", "兩段式"],
            "summary": "Motorcycles turning left at intersections with 'Two-Stage Left Turn' signs or on multi-lane roads with inner fast lane motorcycle prohibitions MUST perform a Hook Turn.",
            "key_fact": "Hook Turn Mandatory where Signed",
            "diagram": "right_of_way"
        },
        {
            "id": "R22",
            "title": "Prohibited U-Turn Locations",
            "keywords": ["u-turn", "double yellow", "prohibited"],
            "summary": "U-turns are strictly prohibited on roads marked with double solid yellow lines, solid white lines, steep slopes, sharp curves, or railroad crossings.",
            "key_fact": "U-Turn Prohibited on Double Yellow Lines",
            "diagram": "right_of_way"
        },

        # FREEWAY & EXPRESSWAY
        {
            "id": "R23",
            "title": "Freeway Safe Following Distance Rule (Speed ÷ 2)",
            "keywords": ["speed ÷ 2", "50 meters", "following distance"],
            "summary": "Under dry weather conditions on freeways, small passenger cars must maintain a safe following distance equal to Speed ÷ 2 in meters (e.g. 100 km/h = 50m distance).",
            "key_fact": "Safe Distance = Speed ÷ 2 (50m @ 100km/h)",
            "diagram": "freeway_distance"
        },
        {
            "id": "R24",
            "title": "Freeway Rain/Wet Weather Distance Rule",
            "keywords": ["wet road", "rain", "double distance"],
            "summary": "During heavy rain, fog, or wet road conditions on freeways, drivers MUST double their standard safe following distance.",
            "key_fact": "Wet Road: Double Following Distance",
            "diagram": "freeway_distance"
        },
        {
            "id": "R25",
            "title": "Freeway Breakdown Warning Triangle Distance (100 meters)",
            "keywords": ["warning triangle", "100 meters", "breakdown"],
            "summary": "In the event of a vehicle breakdown on a freeway or expressway, place the red warning triangle 100 meters behind the vehicle on the shoulder/lane.",
            "key_fact": "Freeway Breakdown Triangle: 100m Behind",
            "diagram": "freeway_distance"
        },
        {
            "id": "R26",
            "title": "Freeway Inner Lane Minimum Speed Rule",
            "keywords": ["inner lane", "minimum speed", "highest speed"],
            "summary": "The innermost lane on freeways is designated as the overtaking lane. Vehicles traveling in the inner lane MUST maintain the maximum posted speed limit for that segment (e.g. 90-110 km/h).",
            "key_fact": "Inner Lane: Must Maintain Max Speed Limit",
            "diagram": "freeway_distance"
        },

        # CHILD SAFETY & PASSENGERS
        {
            "id": "R27",
            "title": "Child Safety Seat Law (Under 4 yrs / 18 kg)",
            "keywords": ["child safety seat", "4 years", "18 kg", "rear seat"],
            "summary": "Children under 4 years old or weighing under 18 kg MUST be seated in an approved rear-facing child safety seat installed in the REAR seat of the vehicle.",
            "key_fact": "Under 4 yrs / 18 kg: Mandatory Rear Child Seat",
            "diagram": "child_seat"
        },
        {
            "id": "R28",
            "title": "Front Passenger Seat Age Restriction (12 years old)",
            "keywords": ["12 years", "front passenger", "prohibited"],
            "summary": "Children under 12 years of age are strictly prohibited from sitting in the front passenger seat of any automobile.",
            "key_fact": "Under 12 yrs: Prohibited from Front Seat",
            "diagram": "child_seat"
        },
        {
            "id": "R29",
            "title": "Motorcycle Passenger Seat Rules (Fixed Seat Only)",
            "keywords": ["side-saddle", "fixed rear seat", "1 passenger"],
            "summary": "Only 1 passenger is allowed on ordinary heavy/light motorcycles with a fixed rear seat. Side-saddle riding is illegal. Small light motorcycles cannot carry any passengers.",
            "key_fact": "Max 1 Passenger, Fixed Seat Only (No Side-Saddle)",
            "diagram": "child_seat"
        },

        # EMERGENCY FIRST AID & CPR/AED
        {
            "id": "R30",
            "title": "CPR Compression-to-Ventilation Ratio (30:2)",
            "keywords": ["30:2", "compressions", "ventilations", "cpr ratio"],
            "summary": "Standard CPR protocol for cardiac arrest is 30 chest compressions followed by 2 rescue breaths (30:2 ratio).",
            "key_fact": "CPR Ratio: 30 Compressions : 2 Breaths",
            "diagram": "child_seat"
        },
        {
            "id": "R31",
            "title": "CPR Compression Depth & Rate (5-6 cm & 100-120/min)",
            "keywords": ["5-6 cm", "100-120", "depth", "rate"],
            "summary": "Chest compressions must be delivered at a rate of 100 to 120 compressions per minute, reaching a depth of 5 to 6 cm on the center of the sternum.",
            "key_fact": "Depth: 5-6 cm | Rate: 100-120/min",
            "diagram": "child_seat"
        },
        {
            "id": "R32",
            "title": "Brain Oxygen Deprivation Window (4 to 6 minutes)",
            "keywords": ["4 to 6 minutes", "brain damage", "cardiac arrest"],
            "summary": "Irreversible brain damage begins within 4 to 6 minutes of cardiac/respiratory arrest. CPR must begin immediately.",
            "key_fact": "Brain Damage Window: 4 to 6 Minutes",
            "diagram": "child_seat"
        },
        {
            "id": "R33",
            "title": "Spinal Injury Airway Clear (Jaw-Thrust Maneuver)",
            "keywords": ["jaw-thrust", "spinal injury", "do not tilt"],
            "summary": "For an unconscious victim with suspected neck/spinal trauma, clear the airway using the Jaw-thrust maneuver without tilting the head back.",
            "key_fact": "Spinal Trauma: Use Jaw-Thrust (No Head Tilt)",
            "diagram": "child_seat"
        },

        # FINES & DEMERIT POINTS
        {
            "id": "R34",
            "title": "Running Red Light Fines & Demerit Points",
            "keywords": ["red light", "demerit", "3 points", "1,800"],
            "summary": "Running a red light incurs fines (Moto: NT$1,800–5,400 | Car: NT$2,700–5,400) PLUS 3 demerit points on your driving record.",
            "key_fact": "Red Light: Fine + 3 Demerit Points",
            "diagram": "speed_limit"
        },
        {
            "id": "R35",
            "title": "Demerit Point Suspension Threshold (12 Points in 1 Year)",
            "keywords": ["12 demerit", "1 year", "2-month suspension"],
            "summary": "Accumulating 12 demerit points within 1 year results in a mandatory 2-month driver license suspension.",
            "key_fact": "12 Demerits in 1 Year = 2-Month Suspension",
            "diagram": "speed_limit"
        }
    ]

    master_cards = []

    for r in detailed_rules:
        matched_qs = []
        for q in questions:
            q_text = (q['question'] + " " + q.get('explanation', '')).lower()
            if any(kw in q_text for kw in r['keywords']):
                matched_qs.append(q)

        canonical = matched_qs[0] if matched_qs else questions[0]

        master_cards.append({
            "id": r["id"],
            "title": r["title"],
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

    print(f"Generated {len(master_cards)} Granular Master Rule Groups for {out_filename}.")

expand_master_rules('questions.json', 'moto_master_rules.json', is_car=False)
expand_master_rules('car_questions.json', 'car_master_rules.json', is_car=True)
