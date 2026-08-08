import json
import re

def audit_codebase_bugs():
    bugs = []
    
    with open('app.js', 'r', encoding='utf-8') as f:
        js = f.read()
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Bug 1: Dead event listener for 'profileBtn'
    if "document.getElementById('profileBtn')" in js:
        bugs.append({
            "id": "BUG_01",
            "severity": "Low",
            "desc": "Dead event listener for 'profileBtn' in app.js line 239 (HTML uses <select id='profileSelect'>).",
            "fix": "Remove dead profileBtn listener from app.js."
        })

    # Bug 2: Missing error state when filteredQuestions is empty
    if "if (filteredQuestions.length === 0)" in js:
        # Check how renderCurrentQuestion handles empty filteredQuestions
        if "filteredQuestions.length === 0" in js and "document.getElementById('questionText').textContent =" in js:
            pass
        else:
            bugs.append({
                "id": "BUG_02",
                "severity": "Medium",
                "desc": "Empty search or filter leads to potential rendering error if not handled gracefully.",
                "fix": "Ensure empty question state displays 'No matching questions found' card."
            })

    # Bug 3: Master Rule card match question count display
    with open('car_master_rules.json', 'r', encoding='utf-8') as f:
        cmr = json.load(f)
    for c in cmr:
        if c['matched_question_count'] == 0:
            bugs.append({
                "id": "BUG_03",
                "severity": "High",
                "desc": f"Master Rule card {c['id']} has 0 matched questions.",
                "fix": "Re-map master rule keywords to ensure all 61 cards have matched questions."
            })

    print("=== DEEP CODEBASE AUDIT RESULTS ===")
    print(f"Total Bugs Discovered: {len(bugs)}")
    for b in bugs:
        print(f"[{b['severity']}] {b['id']}: {b['desc']}")
        print(f"   FIX: {b['fix']}\n")

if __name__ == '__main__':
    audit_codebase_bugs()
