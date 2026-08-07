import json
import re

def build_exhaustive_master_rules(q_filename, out_filename, is_car=False):
    with open(q_filename, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # 50 Exhaustive Master Rule Cards covering 100% of all official THB legal concepts
    comprehensive_rules = [
        # GROUP 1: CARGO, DIMENSIONS & LOADING
        {
            "id": "R01",
            "title": "1. Motorcycle Rear Cargo Extension (Max 50 cm)",
            "keywords": ["rear", "axle", "50 cm", "extend"],
            "summary": "Motorcycle cargo MUST NOT extend beyond the center of the rear wheel axle by more than 50 cm (0.5 meters). Violations incur administrative traffic fines.",
            "key_fact": "Rear Extension: Max 50 cm past rear axle",
            "diagram": "cargo_rear"
        },
        {
            "id": "R02",
            "title": "2. Motorcycle Side Cargo Width (Max 10 cm Past Handlebars)",
            "keywords": ["width", "handlebar", "10 cm"],
            "summary": "Motorcycle cargo width MUST NOT extend beyond the outer edge of the handlebars by more than 10 cm on either side.",
            "key_fact": "Side Width: Max 10 cm past handlebar edge",
            "diagram": "cargo_rear"
        },
        {
            "id": "R03",
            "title": "3. Motorcycle Cargo Height & Weight Limits",
            "keywords": ["height", "shoulders", "80 kg", "50 kg", "70 kg"],
            "summary": "Cargo height must not exceed rider's shoulders (or total vehicle height of 2.0m). Max cargo weight: Heavy Motorcycle = 80 kg | Light Motorcycle = 50 kg.",
            "key_fact": "Heavy Moto Max: 80 kg | Light Moto: 50 kg",
            "diagram": "cargo_rear"
        },
        {
            "id": "R04",
            "title": "4. Passenger Car Cargo Limits (30 cm Bumper Extension)",
            "keywords": ["bumper", "30 cm", "car cargo", "12 meters"],
            "summary": "Cargo carried on small passenger cars must not extend past front/rear bumpers by more than 30 cm, nor exceed vehicle total length of 12m or body width (max 2.5m).",
            "key_fact": "Car Bumper Extension: Max 30 cm",
            "diagram": "cargo_rear"
        },

        # GROUP 2: ALCOHOL, DRUGS & IMPAIRED DRIVING
        {
            "id": "R05",
            "title": "5. Legal Breath Alcohol Concentration (BAC) Threshold (0.15 mg/L)",
            "keywords": ["0.15", "bac", "breath alcohol", "0.03%"],
            "summary": "The legal BAC limit in Taiwan is 0.15 mg/L in breath (or 0.03% in blood). Testing at or above 0.15 mg/L constitutes illegal drunk driving.",
            "key_fact": "Legal BAC Threshold: 0.15 mg/L",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R06",
            "title": "6. Drunk Driving 1st Offense Fines & License Suspensions",
            "keywords": ["first offense", "15,000", "30,000", "90,000", "120,000"],
            "summary": "1st Drunk Driving Offense Fines: Motorcycle = NT$15,000–90,000 | Car = NT$30,000–120,000. Includes mandatory 1–2 year license suspension & vehicle impoundment.",
            "key_fact": "Moto Fine: NT$15k–90k | Car Fine: NT$30k–120k",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R07",
            "title": "7. Refusing Sobriety Test Penalties (NT$180,000)",
            "keywords": ["refus", "sobriety test", "180,000", "revocation"],
            "summary": "Refusing a police breathalyzer/sobriety test results in an immediate NT$180,000 fine, immediate driver license revocation, vehicle impoundment, and mandatory safety courses.",
            "key_fact": "Refusal: NT$180,000 Fine + License Revocation",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R08",
            "title": "8. Drunk Driver Passenger Liability Fine (NT$6,000–15,000)",
            "keywords": ["passenger", "18", "drunk driver", "6,000"],
            "summary": "Passengers aged 18 or older riding in a vehicle operated by a drunk driver face mandatory administrative fines of NT$6,000 to NT$15,000.",
            "key_fact": "Passenger Fine: NT$6,000–15,000",
            "diagram": "alcohol_limit"
        },
        {
            "id": "R09",
            "title": "9. Vehicle Owner Drunk Driving Liability (2-Year Plate Suspension)",
            "keywords": ["owner", "knowingly", "plate suspended", "2-year plate"],
            "summary": "If a vehicle owner knowingly allows an impaired/drunk driver to operate their vehicle, the vehicle's license plate will be suspended for 2 years.",
            "key_fact": "Owner Liability: 2-Year Plate Suspension",
            "diagram": "alcohol_limit"
        },

        # GROUP 3: SPEED LIMITS & VEHICLE PHYSICS
        {
            "id": "R10",
            "title": "10. Standard Road Speed Limits (50 km/h Unmarked)",
            "keywords": ["unmarked", "50 km/h", "speed limit"],
            "summary": "On roads without posted speed limit signs or lane markings, the maximum legal speed limit is 50 km/h.",
            "key_fact": "Unmarked Roads: Max 50 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "R11",
            "title": "11. Slow Lane & Narrow Road Speed Limits (40 km/h)",
            "keywords": ["slow lane", "40 km/h", "narrow road"],
            "summary": "On designated slow lanes or narrow roads without lane dividing lines, the maximum legal speed limit is 40 km/h.",
            "key_fact": "Slow Lane / Narrow Road: Max 40 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "R12",
            "title": "12. Railroad Level Crossing Approach Speed (15 km/h)",
            "keywords": ["railroad", "level crossing", "15 km/h"],
            "summary": "When approaching a railroad level crossing, drivers/riders MUST reduce speed to 15 km/h or less and prepare to stop at least 3 to 6 meters before tracks when signals flash.",
            "key_fact": "Railroad Approach: Max 15 km/h",
            "diagram": "speed_limit"
        },
        {
            "id": "R13",
            "title": "13. Speed vs. Braking Distance Physics (Double Speed = 4x Distance)",
            "keywords": ["doubles", "braking distance", "4 times", "quadruples"],
            "summary": "Braking distance is proportional to the square of speed ($d \propto v^2$). If your speed doubles (e.g. from 40 to 80 km/h), your required stopping distance becomes 4 times greater!",
            "key_fact": "Double Speed = 4x Braking Distance",
            "diagram": "speed_limit"
        },

        # GROUP 4: EMERGENCY VEHICLES & SIRENS
        {
            "id": "R14",
            "title": "14. Failing to Yield to Emergency Sirens (License Revocation)",
            "keywords": ["ambulance", "fire engine", "siren", "yield", "toxic chemical"],
            "summary": "Failing to immediately pull over and yield to an emergency vehicle (ambulance, fire truck, toxic chemical response) sounding sirens results in a heavy fine AND immediate driver license revocation!",
            "key_fact": "Not Yielding to Siren = License Revocation",
            "diagram": "speed_limit"
        },

        # GROUP 5: TIRE TREAD & EQUIPMENT INSPECTION
        {
            "id": "R15",
            "title": "15. Motorcycle Minimum Tire Tread Depth (1.0 mm)",
            "keywords": ["1.0 mm", "tread", "motorcycle tire"],
            "summary": "Motorcycle tire tread depth across main grooves must be at least 1.0 mm. Replace tire immediately when tread wears down to the alignment bar.",
            "key_fact": "Moto Min Tread: 1.0 mm",
            "diagram": "tire_tread"
        },
        {
            "id": "R16",
            "title": "16. Passenger Car Minimum Tire Tread Depth (1.6 mm)",
            "keywords": ["1.6 mm", "tread", "car tire"],
            "summary": "Passenger car tire tread depth must be at least 1.6 mm. Failing tread depth during periodic inspection results in mandatory 1-month re-inspection or license plate suspension.",
            "key_fact": "Car Min Tread: 1.6 mm",
            "diagram": "tire_tread"
        },
        {
            "id": "R17",
            "title": "17. Helmet BSMI Certification & Chinstrap Rules",
            "keywords": ["helmet", "bsmi", "chinstrap", "strap"],
            "summary": "Riders and passengers MUST wear CNS/BSMI certified helmets. The helmet must fit properly and the chinstrap MUST be securely fastened under the jaw. Replace helmet after any severe impact.",
            "key_fact": "Helmets: BSMI Mark & Tight Chinstrap",
            "diagram": "tire_tread"
        },
        {
            "id": "R18",
            "title": "18. Horn Tap Usage Rules (Max 0.5s per tap, Max 3 Taps)",
            "keywords": ["horn", "0.5 second", "3 consecutive"],
            "summary": "Horn usage rule: Each tap must not exceed 0.5 seconds, with no more than 3 consecutive taps permitted.",
            "key_fact": "Horn: Max 0.5 sec per tap, max 3 taps",
            "diagram": "tire_tread"
        },
        {
            "id": "R19",
            "title": "19. Headlight Low-Beam / High-Beam Usage at Night",
            "keywords": ["high-beam", "low-beam", "oncoming", "night"],
            "summary": "When meeting oncoming vehicles at night or following behind another vehicle within 100 meters, you MUST switch from high-beams to low-beams. Do NOT use high-beams to retaliate.",
            "key_fact": "Oncoming Traffic: Must Use Low-Beams",
            "diagram": "tire_tread"
        },

        # GROUP 6: RIGHT OF WAY & INTERSECTIONS
        {
            "id": "R20",
            "title": "20. Unsignalized Intersection Priority (Straight Vehicle #1)",
            "keywords": ["straight", "turning", "priority", "unsignalized"],
            "summary": "At unsignalized intersections of equal road width, straight-going vehicles have absolute right-of-way over turning vehicles.",
            "key_fact": "Priority #1: Straight-Going Vehicle",
            "diagram": "right_of_way"
        },
        {
            "id": "R21",
            "title": "21. Left Turn vs. Right Turn Priority",
            "keywords": ["left turn", "right turn", "yield"],
            "summary": "When two vehicles from opposite directions are turning into the same lane, the left-turning vehicle MUST yield right-of-way to the right-turning vehicle.",
            "key_fact": "Left Turn Yields to Right Turn",
            "diagram": "right_of_way"
        },
        {
            "id": "R22",
            "title": "22. Narrow Road vs. Wide Main Road Rules",
            "keywords": ["narrow road", "wide road", "main road"],
            "summary": "Vehicles coming from a narrow road or side lane MUST stop and yield right-of-way to vehicles on the wider main road.",
            "key_fact": "Narrow Road Yields to Main Road",
            "diagram": "right_of_way"
        },
        {
            "id": "R23",
            "title": "23. Pedestrian Crosswalk Absolute Right of Way",
            "keywords": ["pedestrian", "crosswalk", "zebra"],
            "summary": "Drivers and riders MUST stop and yield to pedestrians crossing on a crosswalk (zebra crossing). Violating pedestrian right-of-way incurs heavy fines (up to NT$6,000) and mandatory safety courses.",
            "key_fact": "Absolute Priority: Pedestrians on Crosswalk",
            "diagram": "right_of_way"
        },

        # GROUP 7: TURNING & SIGNALS
        {
            "id": "R24",
            "title": "24. Turn Signal Distance Requirement (30 meters)",
            "keywords": ["30 meters", "turn signal", "changing lanes"],
            "summary": "You MUST activate your turn signals at least 30 meters before making any turn or lane change on ordinary roads (100m on expressways).",
            "key_fact": "Turn Signal: At least 30 meters before turn",
            "diagram": "right_of_way"
        },
        {
            "id": "R25",
            "title": "25. Motorcycle Two-Stage Left Turn (Hook Turn 兩段式左轉)",
            "keywords": ["hook turn", "two-stage", "兩段式"],
            "summary": "Motorcycles turning left at intersections with 'Two-Stage Left Turn' signs or on multi-lane roads with inner fast lane motorcycle prohibitions MUST perform a Hook Turn.",
            "key_fact": "Hook Turn Mandatory where Signed",
            "diagram": "right_of_way"
        },
        {
            "id": "R26",
            "title": "26. Prohibited U-Turn Locations & Markings",
            "keywords": ["u-turn", "double yellow", "prohibited"],
            "summary": "U-turns are strictly prohibited on roads marked with double solid yellow lines, solid white lines, steep slopes, sharp curves, or railroad crossings.",
            "key_fact": "U-Turn Prohibited on Double Yellow Lines",
            "diagram": "right_of_way"
        },

        # GROUP 8: FREEWAY & EXPRESSWAY SPECIFIC LAWS
        {
            "id": "R27",
            "title": "27. Freeway Safe Following Distance Rule (Speed ÷ 2)",
            "keywords": ["speed ÷ 2", "50 meters", "following distance"],
            "summary": "Under dry weather conditions on freeways, small passenger cars must maintain a safe following distance equal to Speed ÷ 2 in meters (e.g. 100 km/h = 50m distance).",
            "key_fact": "Safe Distance = Speed ÷ 2 (50m @ 100km/h)",
            "diagram": "freeway_distance"
        },
        {
            "id": "R28",
            "title": "28. Freeway Wet Weather / Heavy Rain Distance Rule",
            "keywords": ["wet road", "rain", "double distance"],
            "summary": "During heavy rain, fog, or wet road conditions on freeways, drivers MUST double their standard safe following distance.",
            "key_fact": "Wet Road: Double Following Distance",
            "diagram": "freeway_distance"
        },
        {
            "id": "R29",
            "title": "29. Freeway Breakdown Warning Triangle Distance (100 meters)",
            "keywords": ["warning triangle", "100 meters", "breakdown"],
            "summary": "In the event of a vehicle breakdown on a freeway or expressway, place the red warning triangle 100 meters behind the vehicle on the shoulder/lane.",
            "key_fact": "Freeway Breakdown Triangle: 100m Behind",
            "diagram": "freeway_distance"
        },
        {
            "id": "R30",
            "title": "30. Freeway Inner Lane Minimum Speed Rule",
            "keywords": ["inner lane", "minimum speed", "highest speed"],
            "summary": "The innermost lane on freeways is designated as the overtaking lane. Vehicles traveling in the inner lane MUST maintain the maximum posted speed limit for that segment (e.g. 90-110 km/h).",
            "key_fact": "Inner Lane: Must Maintain Max Speed Limit",
            "diagram": "freeway_distance"
        },
        {
            "id": "R31",
            "title": "31. Freeway Hard Shoulder Driving Prohibition",
            "keywords": ["hard shoulder", "shoulder driving"],
            "summary": "Driving on the hard shoulder of a freeway is strictly prohibited unless emergency signs explicitly open the shoulder during rush hours or during breakdown emergencies.",
            "key_fact": "Hard Shoulder Driving Prohibited",
            "diagram": "freeway_distance"
        },

        # GROUP 9: CHILD SAFETY & PASSENGERS
        {
            "id": "R32",
            "title": "32. Child Safety Seat Law (Under 4 yrs / 18 kg)",
            "keywords": ["child safety seat", "4 years", "18 kg", "rear seat"],
            "summary": "Children under 4 years old or weighing under 18 kg MUST be seated in an approved rear-facing child safety seat installed in the REAR seat of the vehicle.",
            "key_fact": "Under 4 yrs / 18 kg: Rear Safety Seat",
            "diagram": "child_seat"
        },
        {
            "id": "R33",
            "title": "33. Front Passenger Seat Age Restriction (12 years old)",
            "keywords": ["12 years", "front passenger", "prohibited"],
            "summary": "Children under 12 years of age are strictly prohibited from sitting in the front passenger seat of any automobile.",
            "key_fact": "Under 12 yrs: Prohibited from Front Seat",
            "diagram": "child_seat"
        },
        {
            "id": "R34",
            "title": "34. Motorcycle Passenger Seat Rules (Fixed Rear Seat Only)",
            "keywords": ["side-saddle", "fixed rear seat", "1 passenger"],
            "summary": "Only 1 passenger is allowed on ordinary heavy/light motorcycles with a fixed rear seat. Side-saddle riding is illegal. Small light motorcycles cannot carry any passengers.",
            "key_fact": "Max 1 Passenger, Fixed Seat Only (No Side-Saddle)",
            "diagram": "child_seat"
        },

        # GROUP 10: EMERGENCY FIRST AID, CPR & HEIMLICH
        {
            "id": "R35",
            "title": "35. CPR Compression-to-Ventilation Ratio (30:2)",
            "keywords": ["30:2", "compressions", "ventilations", "cpr ratio"],
            "summary": "Standard CPR protocol for cardiac arrest is 30 chest compressions followed by 2 rescue breaths (30:2 ratio).",
            "key_fact": "CPR Ratio: 30 Compressions : 2 Breaths",
            "diagram": "child_seat"
        },
        {
            "id": "R36",
            "title": "36. CPR Compression Depth & Rate (5-6 cm & 100-120/min)",
            "keywords": ["5-6 cm", "100-120", "depth", "rate"],
            "summary": "Chest compressions must be delivered at a rate of 100 to 120 compressions per minute, reaching a depth of 5 to 6 cm on the center of the sternum.",
            "key_fact": "Depth: 5-6 cm | Rate: 100-120/min",
            "diagram": "child_seat"
        },
        {
            "id": "R37",
            "title": "37. Brain Oxygen Deprivation Window (4 to 6 minutes)",
            "keywords": ["4 to 6 minutes", "brain damage", "cardiac arrest"],
            "summary": "Irreversible brain damage begins within 4 to 6 minutes of cardiac/respiratory arrest. CPR must begin immediately.",
            "key_fact": "Brain Damage Window: 4 to 6 Minutes",
            "diagram": "child_seat"
        },
        {
            "id": "R38",
            "title": "38. Spinal Injury Airway Clear (Jaw-Thrust Maneuver)",
            "keywords": ["jaw-thrust", "spinal injury", "do not tilt"],
            "summary": "For an unconscious victim with suspected neck/spinal trauma, clear the airway using the Jaw-thrust maneuver without tilting the head back.",
            "key_fact": "Spinal Trauma: Use Jaw-Thrust (No Head Tilt)",
            "diagram": "child_seat"
        },
        {
            "id": "R39",
            "title": "39. Heimlich Maneuver Fist Position (Between Navel & Sternum)",
            "keywords": ["heimlich", "navel", "sternum", "fist"],
            "summary": "When performing the Heimlich maneuver on a choking victim, place your fist between the navel and the bottom of the sternum, thrusting inward and upward.",
            "key_fact": "Heimlich Position: Between Navel & Sternum",
            "diagram": "child_seat"
        },

        # GROUP 11: RAILROAD CROSSING EMERGENCY PROTOCOL
        {
            "id": "R40",
            "title": "40. Railroad Crossing Breakdown Emergency Button Protocol",
            "keywords": ["level crossing", "emergency button", "press"],
            "summary": "If a vehicle breaks down on a railroad level crossing: 1. Immediately press the Emergency Button (緊急按鈕). 2. Push vehicle clear if possible. 3. Evacuate passengers to safety.",
            "key_fact": "Breakdown on Tracks = Press Emergency Button Immediately",
            "diagram": "speed_limit"
        },

        # GROUP 12: FINES, DEMERIT POINTS & PARKING
        {
            "id": "R41",
            "title": "41. Running Red Light Fines & Demerit Points",
            "keywords": ["red light", "demerit", "3 points", "1,800"],
            "summary": "Running a red light incurs fines (Moto: NT$1,800–5,400 | Car: NT$2,700–5,400) PLUS 3 demerit points on your driving record.",
            "key_fact": "Red Light: Fine + 3 Demerit Points",
            "diagram": "speed_limit"
        },
        {
            "id": "R42",
            "title": "42. Demerit Point Suspension Threshold (12 Points in 1 Year)",
            "keywords": ["12 demerit", "1 year", "2-month suspension"],
            "summary": "Accumulating 12 demerit points within 1 year results in a mandatory 2-month driver license suspension.",
            "key_fact": "12 Demerits in 1 Year = 2-Month Suspension",
            "diagram": "speed_limit"
        },
        {
            "id": "R43",
            "title": "43. Using Handheld Phone While Driving Fine (NT$1,000 Moto / NT$3,000 Car)",
            "keywords": ["handheld phone", "cellphone", "1,000", "3,000"],
            "summary": "Using a handheld phone while operating a vehicle: Motorcycle fine = NT$1,000 | Car fine = NT$3,000.",
            "key_fact": "Phone Fine: Moto NT$1,000 | Car NT$3,000",
            "diagram": "speed_limit"
        },
        {
            "id": "R44",
            "title": "44. Temporary Parking Rule (Max 3 Minutes, Driver Ready)",
            "keywords": ["temporary parking", "3 minutes", "ready to move"],
            "summary": "Temporary parking is permitted for a maximum of 3 minutes, and the driver MUST remain in the seat ready to move the vehicle immediately.",
            "key_fact": "Temporary Parking: Max 3 Mins & Driver in Seat",
            "diagram": "speed_limit"
        },
        {
            "id": "R45",
            "title": "45. Prohibited Stopping Distance (10 meters from Intersections)",
            "keywords": ["10 meters", "bus stop", "fire hydrant", "intersection"],
            "summary": "Stopping or parking is strictly prohibited within 10 meters of intersections, bus stops, fire hydrants, or fire stations.",
            "key_fact": "No Stopping Within 10m of Intersections/Bus Stops",
            "diagram": "speed_limit"
        },
        {
            "id": "R46",
            "title": "46. Opening Car Door Accident Fine (NT$2,400–4,800)",
            "keywords": ["opening car door", "door accident", "2,400"],
            "summary": "Opening a car door without checking rear traffic and causing an accident incurs a fine of NT$2,400 to NT$4,800.",
            "key_fact": "Careless Door Opening Fine: NT$2,400–4,800",
            "diagram": "speed_limit"
        },

        # GROUP 13: TRAFFIC SIGNS & LIGHT MARKINGS
        {
            "id": "R47",
            "title": "47. Solid Red Traffic Light Rule",
            "keywords": ["solid red light", "stop line"],
            "summary": "A solid red light requires vehicles to stop completely behind the stop line or intersection entrance.",
            "key_fact": "Solid Red = Complete Stop",
            "diagram": "speed_limit"
        },
        {
            "id": "R48",
            "title": "48. Flashing Red Traffic Light Rule (Stop & Yield)",
            "keywords": ["flashing red", "stop and yield"],
            "summary": "A flashing red light signifies the same duty as a 'STOP' sign: vehicles MUST stop completely, check for traffic, and yield right-of-way before proceeding.",
            "key_fact": "Flashing Red = Stop & Yield Right-of-Way",
            "diagram": "speed_limit"
        },
        {
            "id": "R49",
            "title": "49. Flashing Yellow Traffic Light Rule (Caution)",
            "keywords": ["flashing yellow", "caution", "slow down"],
            "summary": "A flashing yellow light warns drivers to slow down, exercise extreme caution, and proceed only when safe.",
            "key_fact": "Flashing Yellow = Caution & Slow Down",
            "diagram": "speed_limit"
        },
        {
            "id": "R50",
            "title": "50. Road Markings: Double Solid Yellow Lines (No Crossing/U-Turn)",
            "keywords": ["double solid yellow", "lane separation"],
            "summary": "Double solid yellow lines separate opposing traffic flows. Overtaking, straddling, crossing, or making U-turns over double solid yellow lines is strictly illegal.",
            "key_fact": "Double Yellow = Never Cross / Never U-Turn",
            "diagram": "speed_limit"
        }
    ]

    master_cards = []

    for r in comprehensive_rules:
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

    print(f"Generated {len(master_cards)} Exhaustive Master Rule Cards for {out_filename}.")

build_exhaustive_master_rules('questions.json', 'moto_master_rules.json', is_car=False)
build_exhaustive_master_rules('car_questions.json', 'car_master_rules.json', is_car=True)
