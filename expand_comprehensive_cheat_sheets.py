import json

def expand_comprehensive_cheat_sheets():
    # 1. CAR COMPREHENSIVE CHEAT SHEET (100% Exam Coverage)
    car_cheat = [
        {
            "category": "⚡ 1. Speed Limits, Following Distances & Physics",
            "items": [
                {"label": "Urban Unmarked Road Speed Limit", "value": "50 km/h"},
                {"label": "Slow Lane & Narrow Undivided Road Speed Limit", "value": "40 km/h"},
                {"label": "Railroad Level Crossing Approach Speed", "value": "15 km/h or less (Stop if red light flashes or bells ring)"},
                {"label": "Adverse Weather on Freeway (<100m visibility)", "value": "Reduce speed to under 40 km/h or pull into service area"},
                {"label": "Dangerous Driving Speed Violation Threshold", "value": "Exceeding speed limit by 40+ km/h (NT$6k–36k + license suspension)"},
                {"label": "Freeway Small Car Safe Following Distance", "value": "Speed (km/h) ÷ 2 in meters (e.g. 100 km/h = 50m; Double in rain/fog)"},
                {"label": "Freeway Large Vehicle Safe Following Distance", "value": "Speed (km/h) - 50 in meters (e.g. 100 km/h = 50m)"},
                {"label": "Speed vs. Braking Distance Physics", "value": "Braking distance ∝ Speed² (Doubling speed = 4x longer braking distance)"},
                {"label": "Reaction Time Distance Physics", "value": "Reaction distance increases directly proportionally to speed (linear)"},
                {"label": "Turn Signal Advance Distance", "value": "Must signal at least 30 meters prior to turning or changing lanes"},
                {"label": "Pedestrian Crosswalk Safe Buffer", "value": "Stop and yield at least 3 meters (approx. 4 zebra stripes) before crosswalk"},
                {"label": "Freeway Breakdown Warning Triangle Distance", "value": "Place triangle 100 meters behind vehicle (30–100m on regular roads)"},
                {"label": "Highway Emergency Triangle in Heavy Fog/Rain", "value": "Place triangle 100 to 200 meters behind vehicle"}
            ]
        },
        {
            "category": "🍷 2. Alcohol BAC Limits, DUI Offenses & Passenger Penalties",
            "items": [
                {"label": "Administrative Fine BAC Threshold", "value": "0.15 mg/L breath alcohol (or 0.03% blood alcohol)"},
                {"label": "Criminal Offense Prosecution BAC Threshold", "value": "0.25 mg/L breath alcohol (or 0.05% blood alcohol)"},
                {"label": "First-Time Car Drunk Driving Fine", "value": "NT$30,000 to NT$120,000 + License suspension for 1 to 2 years"},
                {"label": "Refusing Sobriety Breathalyzer Test Penalty", "value": "NT$180,000 fine + Instant license revocation + Vehicle impoundment"},
                {"label": "Second Refusal to Sobriety Test (within 10 yrs)", "value": "NT$360,000 fine + Instant revocation + Public disclosure"},
                {"label": "Repeat Drunk Driving Window (10 Years)", "value": "Maximum fine + License revocation + Public photo/name disclosure"},
                {"label": "Passenger Riding with Drunk Driver Penalty", "value": "NT$6,000 to NT$15,000 fine for passengers 18+ (except seniors 70+)"},
                {"label": "DUI Involving Severe Injury or Death", "value": "Permanent driver license revocation + Lifetime ban from retesting"},
                {"label": "Ignition Interlock (Alcohol Lock) Mandate", "value": "Mandatory installation upon re-applying for license after DUI revocation"}
            ]
        },
        {
            "category": "📱 3. Traffic Fines, Demerit Points & License Laws",
            "items": [
                {"label": "Demerit Points License Suspension Threshold", "value": "Accumulating 12 demerit points within 1 year = 2-month suspension"},
                {"label": "Running a Red Light Fine", "value": "NT$1,800 to NT$5,400 fine + 3 demerit points"},
                {"label": "Operating Handheld Mobile Device (Car Driver)", "value": "NT$3,000 fine (prohibited while vehicle is in motion)"},
                {"label": "Failing to Yield to Pedestrians on Crosswalk", "value": "NT$1,200 to NT$6,000 fine + 3 demerit points + 3h safety class"},
                {"label": "Failing to Yield to Emergency Sirens (Ambulance)", "value": "NT$3,600 fine + Mandatory driver license revocation"},
                {"label": "Leaving Child Under 6 Unattended in Car", "value": "NT$3,000 fine + 4 hours road traffic safety training class"},
                {"label": "Driving Without a Valid Driver's License", "value": "NT$6,000 to NT$24,000 fine + Immediate vehicle impoundment"},
                {"label": "Driving With Suspended or Revoked License", "value": "NT$6,000 to NT$24,000 fine + Immediate vehicle impoundment"},
                {"label": "Lending Driver's License to Another Person", "value": "Driver's license suspended for 3 months"},
                {"label": "Hit-and-Run Fleeing Scene (Injury or Death)", "value": "Driver license permanently revoked + Criminal prosecution"},
                {"label": "Three Violations in 3 Months (Vehicle Penalty)", "value": "Suspension of vehicle license plate for 1 month"},
                {"label": "Professional License Review Cycle (<60 yrs)", "value": "Reviewed once every 3 years from date of issuance"},
                {"label": "Elderly Drivers (75+ yrs) License Renewal", "value": "Must pass physical + cognitive dementia test every 3 years"}
            ]
        },
        {
            "category": "🛑 4. Right-of-Way, Intersections & Road Markings",
            "items": [
                {"label": "Intersection Right-of-Way Priority #1", "value": "Straight-going vehicle has absolute priority over turning vehicle"},
                {"label": "Intersection Right-of-Way Priority #2", "value": "Left-turning vehicle MUST yield to Right-turning vehicle"},
                {"label": "Uncontrolled / Equal Intersections", "value": "Vehicle on left must yield to vehicle approaching from RIGHT side"},
                {"label": "Roundabout Traffic Right-of-Way", "value": "Vehicles entering roundabout MUST yield to vehicles already circulating inside"},
                {"label": "T-Intersection Priority", "value": "Vehicle on stem of T-intersection must yield to cross traffic on main road"},
                {"label": "Solid Double Yellow Lines", "value": "Strictly prohibited to cross, overtake, or make U-turns 24 hours a day"},
                {"label": "Solid White Line (Lane Separation)", "value": "Prohibited from changing lanes across solid white line"},
                {"label": "Yellow Diagonal Crosshatch Area", "value": "Prohibited from stopping or parking inside grid at all times"},
                {"label": "Zig-zag Lines on Pavement (Zebra approach)", "value": "Indicates pedestrian crosswalk ahead; driver must slow down"}
            ]
        },
        {
            "category": "🚪 5. Parking, Stopping & Child Safety Regulations",
            "items": [
                {"label": "Two-Stage Door Opening Protocol (Art. 112)", "value": "1. Look back and open door ~15 cm → 2. Check clear → 3. Open and exit"},
                {"label": "Solid Red Curb Line Marking", "value": "Prohibited from stopping or parking 24 hours a day"},
                {"label": "Solid Yellow Curb Line Marking", "value": "Temporary stopping (<3 min) allowed; No parking from 7 AM to 8 PM"},
                {"label": "Parking Distance from Road Edge / Curb", "value": "Right wheels must be within 40 cm of curb (within 60 cm for temp stopping)"},
                {"label": "Prohibited Stopping Zone Distance", "value": "Prohibited within 10 meters of intersections, bus stops, fire hydrants"},
                {"label": "Child Under 2 Years Old Safety Seat", "value": "Mandatory REAR-FACING child safety seat placed in REAR seat"},
                {"label": "Child 2 to 4 Years Old (<18 kg) Safety Seat", "value": "Mandatory child safety seat installed in REAR seat"},
                {"label": "Child Under 12 Years Old Seating Law", "value": "Prohibited from riding in front passenger seat (must sit in rear)"}
            ]
        },
        {
            "category": "🔧 6. Vehicle Mechanics, Maintenance & Troubleshooting",
            "items": [
                {"label": "Minimum Tire Tread Depth (Automobile)", "value": "1.6 mm (failing depth results in failed inspection and hydroplaning)"},
                {"label": "Exhaust Smoke: Bluish-White Smoke", "value": "Indicates engine oil leaking into cylinders and burning"},
                {"label": "Exhaust Smoke: Thick White Smoke / Steam", "value": "Indicates coolant/water leaking into combustion chamber"},
                {"label": "Exhaust Smoke: Dense Black Smoke", "value": "Indicates incomplete fuel combustion (too rich air-fuel mixture)"},
                {"label": "Low Engine Oil Pressure Warning Light", "value": "Stop vehicle immediately in safe place and shut off engine"},
                {"label": "Brake Fade on Long Downhill Mountain Slope", "value": "Shift to lower gear to utilize engine braking (avoid riding brakes)"},
                {"label": "Tire Blowout while Driving Response", "value": "Grip steering wheel firmly, do NOT slam on brakes, decelerate smoothly"},
                {"label": "Vehicle Towing Rope Standard", "value": "Rope length between 3 and 5 meters with a yellow flag in middle"}
            ]
        },
        {
            "category": "🚑 7. First Aid, CPR & Emergency Crash Response",
            "items": [
                {"label": "First Aid Medical Emergency Priority", "value": "1. Open Airway (A) → 2. Control Bleeding (B) → 3. Circulation & Fractures (C)"},
                {"label": "Adult CPR Compression to Ventilation Ratio", "value": "30 Chest Compressions to 2 Rescue Breaths (30:2)"},
                {"label": "Adult CPR Chest Compression Rate & Depth", "value": "100 to 120 compressions per minute; 5 to 6 cm compression depth"},
                {"label": "Suspected Cervical Spine / Neck Trauma Airway", "value": "Jaw-Thrust maneuver only (do NOT tilt head or twist neck)"},
                {"label": "Irreversible Brain Damage Time Window", "value": "Irreversible brain damage occurs after 4 to 6 minutes without oxygen"},
                {"label": "Railroad Crossing Breakdown 3-Step SOS", "value": "1. Press Red Emergency SOS Button → 2. Push car clear → 3. Evacuate"}
            ]
        }
    ]

    with open('car_cheat_sheet.json', 'w', encoding='utf-8') as f:
        json.dump(car_cheat, f, indent=2, ensure_ascii=False)

    # 2. MOTORCYCLE COMPREHENSIVE CHEAT SHEET (100% Exam Coverage)
    moto_cheat = [
        {
            "category": "⚡ 1. Speed Limits, Braking Physics & Following Buffers",
            "items": [
                {"label": "Urban Unmarked Road Speed Limit", "value": "50 km/h"},
                {"label": "Slow Lane & Undivided Alley Speed Limit", "value": "40 km/h"},
                {"label": "Railroad Crossing Approach Speed Limit", "value": "15 km/h or less (Stop if red light flashes)"},
                {"label": "Braking Distance Physics", "value": "Braking distance ∝ Speed² (2x speed = 4x longer stopping distance)"},
                {"label": "Reaction Time Distance Physics", "value": "Reaction distance increases directly in linear proportion to speed"},
                {"label": "Turn Signal Advance Distance", "value": "Activate turn signal at least 30 meters before turning or lane change"},
                {"label": "Pedestrian Crosswalk Yielding Buffer", "value": "Yield at least 3 meters (approx. 4 zebra stripes) before crosswalk"},
                {"label": "Prohibited Stopping Zone Distance", "value": "Prohibited within 10 meters of intersections, bus stops, fire hydrants"}
            ]
        },
        {
            "category": "📦 2. Motorcycle Cargo Dimensions, Loading & Passengers",
            "items": [
                {"label": "Cargo Rear Extension Limit", "value": "Max 50 cm beyond rear wheel axle"},
                {"label": "Cargo Width Extension Limit", "value": "Max 10 cm beyond outer edges of handlebars"},
                {"label": "Cargo Height Limit (Small Light Motorcycle)", "value": "Not exceeding rider shoulders; max 1.5 meters from ground"},
                {"label": "Cargo Height Limit (Regular / Heavy Motorcycle)", "value": "Not exceeding rider shoulders; max 2.5 meters from ground"},
                {"label": "Small Light Motorcycle Cargo Weight Limit", "value": "Max 30 kg"},
                {"label": "Regular Light Motorcycle Cargo Weight Limit", "value": "Max 60 kg"},
                {"label": "Heavy Motorcycle Cargo Weight Limit", "value": "Max 90 kg"},
                {"label": "Passenger Carrying Regulations", "value": "Allowed ONLY on rear passenger seat of 50cc+ motorcycles"},
                {"label": "Carrying Children on Front Footrest / Floorboard", "value": "Strictly illegal (fines NT$300 to NT$600)"},
                {"label": "Small Electric Bicycles (Micro-Mobility)", "value": "Carrying any passenger is strictly prohibited"}
            ]
        },
        {
            "category": "🪖 3. Helmet Laws, Driver Licenses & Traffic Fines",
            "items": [
                {"label": "Helmet Certification & Fastening Law", "value": "Must wear BSMI/CNS approved helmet with chin strap securely fastened (NT$500 fine if unfastened)"},
                {"label": "Running a Red Light (Motorcycle)", "value": "NT$1,800 to NT$5,400 fine + 3 demerit points"},
                {"label": "Operating Handheld Mobile Phone While Riding", "value": "NT$1,000 fine for operating handheld device while riding"},
                {"label": "Smoking Cigarette While Riding", "value": "NT$1,200 fine if affecting the safety/comfort of others"},
                {"label": "Riding Motorcycle in Opposite Direction (Wrong Way)", "value": "NT$600 to NT$1,800 fine + 1 demerit point"},
                {"label": "Failing to Yield to Pedestrians on Crosswalk", "value": "NT$1,200 to NT$6,000 fine + 3 demerit points"},
                {"label": "Failing to Yield to Emergency Sirens (Ambulance)", "value": "NT$3,600 fine + Mandatory driver license revocation"},
                {"label": "Demerit Points Suspension Cap", "value": "Accumulating 12 demerit points in 1 year = 2 months license suspension"}
            ]
        },
        {
            "category": "🍷 4. Drunk Riding (DUI) Penalties & BAC Limits",
            "items": [
                {"label": "Administrative Fine BAC Threshold", "value": "0.15 mg/L breath alcohol (or 0.03% blood alcohol)"},
                {"label": "Criminal Offense Prosecution BAC Threshold", "value": "0.25 mg/L breath alcohol (or 0.05% blood alcohol)"},
                {"label": "Motorcycle Drunk Riding Fine (First Offense)", "value": "NT$15,000 to NT$90,000 + License suspension for 1 to 2 years"},
                {"label": "Refusing Sobriety Breathalyzer Test Penalty", "value": "NT$180,000 fine + Instant license revocation + Vehicle impoundment"},
                {"label": "Second Refusal to Sobriety Test (within 10 yrs)", "value": "NT$360,000 fine + Instant revocation + Public disclosure"},
                {"label": "Repeat Drunk Riding Window (10 Years)", "value": "Max fine + License revocation + Public photo/name disclosure"},
                {"label": "Passenger Riding with Drunk Rider Penalty", "value": "NT$6,000 to NT$15,000 fine for passengers 18+ (except seniors 70+)"}
            ]
        },
        {
            "category": "🪝 5. Hook-Turn (Two-Stage Left Turn) & Right-of-Way",
            "items": [
                {"label": "When Two-Stage Left Turn (Hook Turn) is Mandatory", "value": "1. Roads with 3+ lanes in same direction | 2. Where two-stage left turn sign is posted"},
                {"label": "Two-Stage Left Turn Proper Protocol", "value": "Ride straight into waiting box on far right, turn left in box, wait for green light"},
                {"label": "Turning Left Directly on Multi-Lane Roads", "value": "Strictly illegal (fine NT$600–1,800 + severe t-bone collision risk)"},
                {"label": "Intersection Right-of-Way: Straight vs Turning", "value": "Straight-going motorcycle has priority over turning vehicles"},
                {"label": "Intersection Right-of-Way: Left vs Right Turn", "value": "Left-turning vehicle MUST yield to Right-turning vehicle"},
                {"label": "Roundabout Right-of-Way", "value": "Entering vehicles MUST yield to vehicles circulating inside roundabout"}
            ]
        },
        {
            "category": "🔧 6. Maintenance, Tires, Brakes & Defensive Riding",
            "items": [
                {"label": "Minimum Tire Tread Depth (Motorcycle)", "value": "1.0 mm (worn tires cause blowouts and hydroplaning)"},
                {"label": "Tire Pressure Check Frequency", "value": "Check weekly when tires are cold"},
                {"label": "Brake Lever Free Play Standard", "value": "Free play clearance should be 10 to 20 mm"},
                {"label": "Optimal Braking Technique", "value": "Use both front and rear brakes simultaneously (approx. 70% front, 30% rear)"},
                {"label": "Riding Over Wet Manhole Covers & Painted Lines", "value": "Keep bike upright, avoid leaning, avoid harsh braking or acceleration"},
                {"label": "Large Truck Blind Spots & Inner Wheel Radius (Off-tracking)", "value": "Keep at least 2 meters lateral clearance from turning heavy trucks"},
                {"label": "Passing Parked Cars Safely", "value": "Maintain at least 1 meter buffer distance to prevent car door strikes"}
            ]
        },
        {
            "category": "🚑 7. Accident Response, CPR & First Aid Protocol",
            "items": [
                {"label": "Immediate Crash Action", "value": "Stop immediately, shut off engine, turn on hazard lights, place warning signs"},
                {"label": "Removing Injured Rider's Helmet", "value": "Do NOT remove helmet unless breathing is obstructed (prevents neck injury)"},
                {"label": "First Aid Medical Priority", "value": "1. Airway (A) → 2. Bleeding (B) → 3. Fractures (C)"},
                {"label": "CPR Ratio (Compressions to Breaths)", "value": "30 Chest Compressions to 2 Rescue Breaths (30:2)"},
                {"label": "CPR Speed and Depth", "value": "100 to 120 compressions per minute; 5 to 6 cm depth"},
                {"label": "Railroad Breakdown SOS 3-Step Action", "value": "1. Press Red Emergency SOS Button → 2. Push bike clear → 3. Move clear"}
            ]
        }
    ]

    with open('cheat_sheet.json', 'w', encoding='utf-8') as f:
        json.dump(moto_cheat, f, indent=2, ensure_ascii=False)

    print("Generated 100% comprehensive, high-yield cram cheat sheets for Car and Motorcycle!")

if __name__ == '__main__':
    expand_comprehensive_cheat_sheets()
