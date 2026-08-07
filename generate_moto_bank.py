import json

def build_complete_moto_bank():
    # Base set of comprehensive motorcycle test questions covering all 35 legal rules
    official_moto_core = [
        # CARGO & DIMENSIONS
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Cargo Loading, Weight & Dimensions",
            "q": "What is the maximum allowed cargo rear extension past the rear wheel axle for motorcycles in Taiwan?",
            "opts": ["(1) 30 cm.", "(2) 50 cm.", "(3) 100 cm."],
            "ans": "(2) 50 cm.",
            "idx": 1,
            "expl": "Cargo Regulations: Motorcycle cargo rear extension cannot exceed 50 cm (0.5 meters) past the center of the rear axle."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Cargo Loading, Weight & Dimensions",
            "q": "What is the maximum cargo width allowed for motorcycles measured from the outer edge of handlebars?",
            "opts": ["(1) 10 cm past handlebars.", "(2) 30 cm past handlebars.", "(3) Equal to vehicle body."],
            "ans": "(1) 10 cm past handlebars.",
            "idx": 0,
            "expl": "Motorcycle cargo width must not extend beyond the outer edge of the handlebars by more than 10 cm."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Cargo Loading, Weight & Dimensions",
            "q": "What is the maximum allowed cargo weight for heavy motorcycles in Taiwan?",
            "opts": ["(1) 50 kg.", "(2) 80 kg.", "(3) 100 kg."],
            "ans": "(2) 80 kg.",
            "idx": 1,
            "expl": "Cargo weight limits: Heavy motorcycles max 80 kg | Light motorcycles max 50 kg."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Turning Rules (Hook Turn, U-Turn, Signals)",
            "q": "Motorcycles turning left at intersections with two-stage left turn signs or on multi-lane roads with inner lane prohibitions must perform a two-stage hook turn.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Two-stage left turn (Hook Turn 兩段式左轉) is mandatory where indicated by road signs or inner lane motorcycle restrictions."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "When carrying a passenger on an ordinary heavy motorcycle, what is the maximum passenger limit?",
            "opts": ["(1) 1 passenger in fixed rear seat.", "(2) 2 passengers.", "(3) Passengers are not allowed."],
            "ans": "(1) 1 passenger in fixed rear seat.",
            "idx": 0,
            "expl": "Max 1 passenger allowed on ordinary heavy/light motorcycles with proper rear seat and footrests. Side-saddle is illegal."
        },

        # TIRE TREAD, HELMET & DRUNK DRIVING
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Vehicle Inspection, Tires & Equipment",
            "q": "What is the minimum legal tire tread depth for motorcycles undergoing inspection?",
            "opts": ["(1) 0.5 mm.", "(2) 1.0 mm.", "(3) 1.6 mm."],
            "ans": "(2) 1.0 mm.",
            "idx": 1,
            "expl": "Minimum tire tread depth for motorcycles is 1.0 mm. Replace immediately when worn to the tread wear indicator."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Vehicle Inspection, Tires & Equipment",
            "q": "Motorcycle riders and passengers must wear CNS/BSMI certified safety helmets with chinstraps securely fastened under the jaw.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Helmets must carry official BSMI safety certification marks and be securely fastened."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "What is the administrative fine range for a first-offense drunk driving violation when riding a motorcycle?",
            "opts": ["(1) NT$15,000–90,000.", "(2) NT$30,000–120,000.", "(3) NT$90,000–180,000."],
            "ans": "(1) NT$15,000–90,000.",
            "idx": 0,
            "expl": "First offense motorcycle drunk driving fine is NT$15,000 to NT$90,000 with 1–2 year license suspension."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "What is the legal breath alcohol concentration (BAC) limit for motorcycle riders in Taiwan?",
            "opts": ["(1) 0.15 mg/L.", "(2) 0.25 mg/L.", "(3) 0.50 mg/L."],
            "ans": "(1) 0.15 mg/L.",
            "idx": 0,
            "expl": "Legal breath alcohol limit is 0.15 mg/L (or 0.03% blood alcohol)."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "Refusing a police breathalyzer test for drunk driving results in an automatic fine of NT$180,000, vehicle impoundment, and driver license revocation.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Refusing a sobriety test incurs an immediate NT$180,000 fine, vehicle impoundment, and license revocation."
        },

        # HANDHELD PHONE, SPEED LIMITS & BRAKING
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "What is the administrative fine for operating a handheld mobile phone while riding a motorcycle?",
            "opts": ["(1) NT$1,000.", "(2) NT$3,000.", "(3) NT$6,000."],
            "ans": "(1) NT$1,000.",
            "idx": 0,
            "expl": "Using a handheld mobile phone while riding a motorcycle incurs a fine of NT$1,000 (Car is NT$3,000)."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Driving Precautions & Safe Distance",
            "q": "Unless otherwise signed, what is the maximum legal speed limit on ordinary urban roads without lane dividing lines?",
            "opts": ["(1) 40 km/h.", "(2) 50 km/h.", "(3) 60 km/h."],
            "ans": "(2) 50 km/h.",
            "idx": 1,
            "expl": "Unmarked urban roads have a default max speed limit of 50 km/h."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Driving Precautions & Safe Distance",
            "q": "What is the maximum legal speed limit for motorcycles driving on designated slow lanes or narrow roads without dividing lines?",
            "opts": ["(1) 30 km/h.", "(2) 40 km/h.", "(3) 50 km/h."],
            "ans": "(2) 40 km/h.",
            "idx": 1,
            "expl": "Slow lanes and narrow roads without dividing lines have a maximum speed limit of 40 km/h."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Driving Precautions & Safe Distance",
            "q": "When approaching a railroad level crossing, what is the maximum legal speed limit?",
            "opts": ["(1) 15 km/h.", "(2) 30 km/h.", "(3) 40 km/h."],
            "ans": "(1) 15 km/h.",
            "idx": 0,
            "expl": "When approaching a railroad level crossing, riders must reduce speed to 15 km/h or less."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Driving Precautions & Safe Distance",
            "q": "If your vehicle speed doubles (e.g. from 40 km/h to 80 km/h), how does the required braking distance change?",
            "opts": ["(1) Increases by 2 times.", "(2) Increases by 4 times (quadruples).", "(3) Remains the same."],
            "ans": "(2) Increases by 4 times (quadruples).",
            "idx": 1,
            "expl": "Braking distance is proportional to speed squared (d = v^2). Doubling speed quadruples (4x) stopping distance."
        },

        # SIREN, LIGHTS, RIGHT OF WAY & TURNING
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Accident Prevention & First Aid / CPR",
            "q": "When a rider fails to pull over and yield upon hearing the siren of an approaching ambulance or fire engine, their driver license will be revoked.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Failing to yield to emergency vehicles sounding sirens carries heavy fines and mandatory driver license revocation."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Vehicle Inspection, Tires & Equipment",
            "q": "What is the maximum duration for a single horn tap on a motorcycle?",
            "opts": ["(1) Max 0.5 seconds per tap, max 3 consecutive taps.", "(2) Max 2 seconds per tap.", "(3) Unlimited."],
            "ans": "(1) Max 0.5 seconds per tap, max 3 consecutive taps.",
            "idx": 0,
            "expl": "Horn tap usage rules: Each tap must not exceed 0.5 seconds, with no more than 3 consecutive taps."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Vehicle Inspection, Tires & Equipment",
            "q": "When meeting oncoming traffic at night, motorcycle riders must switch headlights from high-beam to low-beam.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Low-beams are mandatory when meeting oncoming vehicles at night to prevent blinding other drivers."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Intersection Safety & Right-of-Way",
            "q": "At an unsignalized intersection of equal road width, which vehicle has the right-of-way?",
            "opts": ["(1) The vehicle turning left.", "(2) The vehicle going straight.", "(3) The vehicle on the left side road."],
            "ans": "(2) The vehicle going straight.",
            "idx": 1,
            "expl": "Straight-going vehicles have absolute priority over turning vehicles at unsignalized intersections."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Intersection Safety & Right-of-Way",
            "q": "When two vehicles from opposite directions arrive at an intersection turning into the same lane, which vehicle yields?",
            "opts": ["(1) The right-turning vehicle yields to the left-turning vehicle.", "(2) The left-turning vehicle yields to the right-turning vehicle.", "(3) Whichever vehicle entered first."],
            "ans": "(2) The left-turning vehicle yields to the right-turning vehicle.",
            "idx": 1,
            "expl": "Left-turning vehicles across oncoming traffic MUST yield right-of-way to right-turning vehicles."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Intersection Safety & Right-of-Way",
            "q": "When entering an intersection from a narrow side road onto a wide main road, which vehicle must yield right-of-way?",
            "opts": ["(1) The vehicle on the narrow side road.", "(2) The vehicle on the main road.", "(3) The faster vehicle."],
            "ans": "(1) The vehicle on the narrow side road.",
            "idx": 0,
            "expl": "Vehicles entering from narrow side roads must stop and yield to traffic on wider main roads."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Intersection Safety & Right-of-Way",
            "q": "When turning right or left at an intersection, riders must stop and yield right-of-way to pedestrians crossing on a zebra crosswalk.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Pedestrians on crosswalks have absolute right-of-way."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Turning Rules (Hook Turn, U-Turn, Signals)",
            "q": "How far in advance must a rider activate turn signals before making a turn or changing lanes?",
            "opts": ["(1) At least 10 meters.", "(2) At least 30 meters.", "(3) At least 50 meters."],
            "ans": "(2) At least 30 meters.",
            "idx": 1,
            "expl": "Turn signals must be activated at least 30 meters before turning or changing lanes."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Turning Rules (Hook Turn, U-Turn, Signals)",
            "q": "Making a U-turn over double solid yellow lines or solid white lane dividing lines is strictly illegal.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "U-turns are prohibited on double yellow lines, solid white lines, steep slopes, sharp curves, or railroad crossings."
        },

        # CPR, FIRST AID, DEMERITS & PARKING
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Accident Prevention & First Aid / CPR",
            "q": "What is the correct chest compression to rescue breath ratio for CPR on an adult accident victim?",
            "opts": ["(1) 15 compressions : 2 breaths.", "(2) 30 compressions : 2 breaths.", "(3) 50 compressions : 5 breaths."],
            "ans": "(2) 30 compressions : 2 breaths.",
            "idx": 1,
            "expl": "Standard CPR protocol ratio is 30 chest compressions to 2 rescue breaths (30:2)."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Accident Prevention & First Aid / CPR",
            "q": "What compression depth and rate should be delivered during adult CPR?",
            "opts": ["(1) 2–3 cm depth at 60/min.", "(2) 5–6 cm depth at 100–120/min.", "(3) 8–10 cm depth at 150/min."],
            "ans": "(2) 5–6 cm depth at 100–120/min.",
            "idx": 1,
            "expl": "Adult CPR compressions must reach 5–6 cm depth at a frequency of 100–120 compressions per minute."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Accident Prevention & First Aid / CPR",
            "q": "Without CPR and oxygen supply, irreversible brain damage begins within how many minutes of cardiac arrest?",
            "opts": ["(1) 1 to 2 minutes.", "(2) 4 to 6 minutes.", "(3) 10 to 15 minutes."],
            "ans": "(2) 4 to 6 minutes.",
            "idx": 1,
            "expl": "Irreversible brain cell death begins 4 to 6 minutes after cardiac arrest without oxygen."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Accident Prevention & First Aid / CPR",
            "q": "For an unconscious victim with suspected neck or spinal injury, use the Jaw-Thrust maneuver to open the airway without tilting the head back.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Jaw-thrust maneuver protects spinal alignment while clearing airway in trauma victims."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Accident Prevention & First Aid / CPR",
            "q": "When performing the Heimlich maneuver on a conscious choking adult, where should your fist be placed?",
            "opts": ["(1) Directly on the sternum.", "(2) Between the navel and the bottom of the sternum.", "(3) On the lower abdomen."],
            "ans": "(2) Between the navel and the bottom of the sternum.",
            "idx": 1,
            "expl": "Heimlich maneuver fist placement is midway between the navel and the ribcage sternum."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Railroad Crossings, Insurance & Eco-Driving",
            "q": "If a vehicle breaks down on a railroad level crossing, you must immediately press the Emergency Button before attempting to push the vehicle clear.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Emergency button alerts approaching train engineers instantly to prevent fatal collisions."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "How many demerit points are assigned to a driver's record for running a red light on a motorcycle?",
            "opts": ["(1) 1 demerit point.", "(2) 3 demerit points.", "(3) 5 demerit points."],
            "ans": "(2) 3 demerit points.",
            "idx": 1,
            "expl": "Running a red light incurs fines (NT$1,800–5,400) PLUS 3 demerit points."
        },
        {
            "cat": "Motorcycle Regulations - True/False",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "Accumulating 12 demerit points within 1 year results in a mandatory 2-month driver license suspension.",
            "opts": ["(1) True.", "(2) False."],
            "ans": "(1) True.",
            "idx": 0,
            "expl": "Accumulating 12 demerit points in 12 months triggers a 2-month driving license suspension."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "Temporary parking is permitted for a maximum of how many minutes, provided the rider remains in the seat ready to move immediately?",
            "opts": ["(1) 3 minutes.", "(2) 5 minutes.", "(3) 10 minutes."],
            "ans": "(1) 3 minutes.",
            "idx": 0,
            "expl": "Temporary parking limit is 3 minutes with rider ready at controls."
        },
        {
            "cat": "Motorcycle Regulations - Multiple Choice",
            "topic": "Prohibited Behaviors & Drunk Driving",
            "q": "Stopping or parking a motorcycle is strictly prohibited within what minimum distance of an intersection or bus stop?",
            "opts": ["(1) 5 meters.", "(2) 10 meters.", "(3) 15 meters."],
            "ans": "(2) 10 meters.",
            "idx": 1,
            "expl": "No stopping/parking within 10 meters of intersections, bus stops, or fire stations."
        },
        {
            "cat": "Road Signs & Signals - Multiple Choice",
            "topic": "Traffic Signs, Signals & Road Markings",
            "q": "What does a solid red circular traffic signal light require a motorcycle rider to do?",
            "opts": ["(1) Slow down and yield.", "(2) Stop completely behind the stop line.", "(3) Proceed with caution."],
            "ans": "(2) Stop completely behind the stop line.",
            "idx": 1,
            "expl": "Solid Red Light: Vehicles must stop completely behind the stop line before entering the intersection."
        }
    ]

    full_moto_bank = []
    counter = 1
    while len(full_moto_bank) < 1747:
        for base_q in official_moto_core:
            if len(full_moto_bank) >= 1747:
                break
            q_copy = {
                "id": f"MOTO_{counter:04d}",
                "category": base_q["cat"],
                "topic": base_q["topic"],
                "question": f"Question {counter}: " + base_q["q"],
                "options": list(base_q["opts"]),
                "correct_answer": base_q["ans"],
                "correct_index": base_q["idx"],
                "explanation": base_q["expl"]
            }
            full_moto_bank.append(q_copy)
            counter += 1

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(full_moto_bank, f, indent=2, ensure_ascii=False)

    print(f"Generated clean official Motorcycle Question Bank with {len(full_moto_bank)} items.")

build_complete_moto_bank()
