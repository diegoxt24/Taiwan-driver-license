import json

def update_diagram_types():
    with open('car_master_rules.json', 'r', encoding='utf-8') as f:
        car_cards = json.load(f)

    with open('moto_master_rules.json', 'r', encoding='utf-8') as f:
        moto_cards = json.load(f)

    # Detailed SVG mapping for Car
    diagram_map_car = {
        "C_R01": "cargo_rear",          # Passenger Car Cargo Limits (30 cm)
        "C_R02": "child_seat",          # Child Safety Seat Law (Under 4 yrs / 18 kg)
        "C_R03": "child_seat",          # Front Passenger Seat Age Restriction (12 yrs)
        "C_R04": "car_door",            # Opening Car Door Accident Fine (NT$2,400–4,800)
        "C_R05": "tire_tread",          # Passenger Car Minimum Tire Tread Depth (1.6 mm)
        "C_R06": "freeway_distance",    # Freeway Safe Following Distance (Speed ÷ 2)
        "C_R07": "freeway_distance",    # Freeway Wet Weather Distance Rule
        "C_R08": "freeway_distance",    # Freeway Breakdown Warning Triangle (100m)
        "C_R09": "freeway_distance",    # Freeway Inner Lane Minimum Speed Rule
        "C_R10": "freeway_distance",    # Freeway Hard Shoulder Driving Prohibition
        "C_R11": "alcohol_limit",       # Car Drunk Driving Fine (NT$30,000–120,000)
        "C_R12": "alcohol_limit",       # Legal BAC Limit (0.15 mg/L)
        "C_R13": "alcohol_limit",       # Refusing Sobriety Test Penalties (NT$180,000)
        "C_R14": "phone_fine",          # Car Handheld Phone Fine (NT$3,000)
        "C_R15": "seatbelt_law",        # Seatbelt Enforcement Law (All Occupants)
        "C_R16": "speed_limit_50",      # Standard Road Speed Limits (50 km/h)
        "C_R17": "speed_limit_40",      # Slow Lane & Narrow Road Speed Limits (40 km/h)
        "C_R18": "railroad_crossing",   # Railroad Crossing Speed (15 km/h)
        "C_R19": "braking_physics",     # Speed vs. Braking Distance (2x Speed = 4x Distance)
        "C_R20": "siren_yield",         # Emergency Sirens (License Revocation)
        "C_R21": "right_of_way",        # Unsignalized Intersection Priority
        "C_R22": "right_of_way",        # Left Turn vs Right Turn Priority
        "C_R23": "right_of_way",        # Narrow Road vs Wide Main Road
        "C_R24": "right_of_way",        # Pedestrian Crosswalk Priority
        "C_R25": "right_of_way",        # Turn Signal Distance (30m)
        "C_R26": "right_of_way",        # Prohibited U-Turn Locations
        "C_R27": "cpr_protocol",        # CPR Ratio (30:2)
        "C_R28": "cpr_protocol",        # CPR Depth & Rate (5-6 cm & 100-120/min)
        "C_R29": "cpr_protocol",        # Brain Damage Window (4-6 mins)
        "C_R30": "cpr_protocol",        # Jaw-Thrust Maneuver
        "C_R31": "cpr_protocol",        # Heimlich Maneuver Position
        "C_R32": "railroad_crossing",   # Railroad Breakdown Emergency Button
        "C_R33": "traffic_light",       # Running Red Light Fines & Demerit Points
        "C_R34": "demerit_points",      # Demerit Point Suspension (12 Points in 1 Year)
        "C_R35": "traffic_light"        # Traffic Signal Indications (Red/Yellow/Green)
    }

    # Detailed SVG mapping for Moto
    diagram_map_moto = {
        "M_R01": "cargo_rear",          # Moto Cargo Rear Extension (50 cm)
        "M_R02": "cargo_rear",          # Moto Side Cargo Width (10 cm)
        "M_R03": "cargo_rear",          # Moto Cargo Weight (80 kg / 50 kg)
        "M_R04": "right_of_way",        # Two-Stage Hook Turn
        "M_R05": "child_seat",          # Passenger Rules (Fixed Rear Seat)
        "M_R06": "tire_tread",          # Min Tread Depth (1.0 mm)
        "M_R07": "tire_tread",          # Helmet BSMI Certification
        "M_R08": "alcohol_limit",       # Moto Drunk Fine (NT$15,000–90,000)
        "M_R09": "alcohol_limit",       # Legal BAC Limit (0.15 mg/L)
        "M_R10": "alcohol_limit",       # Refusal Penalty (NT$180,000)
        "M_R11": "phone_fine",          # Moto Handheld Phone Fine (NT$1,000)
        "M_R12": "speed_limit_50",      # Standard Road Speed Limits (50 km/h)
        "M_R13": "speed_limit_40",      # Slow Lane Speed Limits (40 km/h)
        "M_R14": "railroad_crossing",   # Railroad Crossing Speed (15 km/h)
        "M_R15": "braking_physics",     # Speed vs. Braking Physics (2x = 4x)
        "M_R16": "siren_yield",         # Emergency Siren Yield
        "M_R17": "tire_tread",          # Horn Tap Rules (0.5s / 3 taps)
        "M_R18": "tire_tread",          # Low-Beam Usage at Night
        "M_R19": "right_of_way",        # Unsignalized Intersection Priority
        "M_R20": "right_of_way",        # Left Turn vs Right Turn Priority
        "M_R21": "right_of_way",        # Narrow Road vs Wide Main Road
        "M_R22": "right_of_way",        # Pedestrian Crosswalk Priority
        "M_R23": "right_of_way",        # Turn Signal Distance (30m)
        "M_R24": "right_of_way",        # Prohibited U-Turn
        "M_R25": "cpr_protocol",        # CPR Ratio (30:2)
        "M_R26": "cpr_protocol",        # CPR Depth & Rate
        "M_R27": "cpr_protocol",        # Brain Damage Window
        "M_R28": "cpr_protocol",        # Jaw-Thrust Maneuver
        "M_R29": "cpr_protocol",        # Heimlich Maneuver
        "M_R30": "railroad_crossing",   # Railroad Breakdown Button
        "M_R31": "traffic_light",       # Running Red Light & Demerits
        "M_R32": "demerit_points",      # 12 Demerit Points Threshold
        "M_R33": "speed_limit_50",      # Temporary Parking (3 Mins)
        "M_R34": "speed_limit_50",      # Prohibited Stopping (10m)
        "M_R35": "traffic_light"        # Traffic Signal Indications
    }

    for c in car_cards:
        if c['id'] in diagram_map_car:
            c['diagram'] = diagram_map_car[c['id']]

    for m in moto_cards:
        if m['id'] in diagram_map_moto:
            m['diagram'] = diagram_map_moto[m['id']]

    with open('car_master_rules.json', 'w', encoding='utf-8') as f:
        json.dump(car_cards, f, indent=2, ensure_ascii=False)

    with open('moto_master_rules.json', 'w', encoding='utf-8') as f:
        json.dump(moto_cards, f, indent=2, ensure_ascii=False)

    print("Successfully mapped rich specific SVG diagram keys for all 70 Master Rules.")

update_diagram_types()
