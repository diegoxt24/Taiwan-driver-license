import json

def build_standalone():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    with open('app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    with open('questions.json', 'r', encoding='utf-8') as f:
        moto_qs = json.load(f)

    with open('car_questions.json', 'r', encoding='utf-8') as f:
        car_qs = json.load(f)

    with open('cheat_sheet.json', 'r', encoding='utf-8') as f:
        moto_cheat = json.load(f)

    with open('car_cheat_sheet.json', 'r', encoding='utf-8') as f:
        car_cheat = json.load(f)

    with open('moto_master_rules.json', 'r', encoding='utf-8') as f:
        moto_rules = json.load(f)

    with open('car_master_rules.json', 'r', encoding='utf-8') as f:
        car_rules = json.load(f)

    # Embed CSS
    html = html.replace('<link rel="stylesheet" href="styles.css">', f'<style>\n{css}\n</style>')

    # Modify JS loadModuleData to use embedded objects directly
    embedded_data_js = f"""
const EMBEDDED_MOTO_QS = {json.dumps(moto_qs, ensure_ascii=False)};
const EMBEDDED_CAR_QS = {json.dumps(car_qs, ensure_ascii=False)};
const EMBEDDED_MOTO_CHEAT = {json.dumps(moto_cheat, ensure_ascii=False)};
const EMBEDDED_CAR_CHEAT = {json.dumps(car_cheat, ensure_ascii=False)};
const EMBEDDED_MOTO_RULES = {json.dumps(moto_rules, ensure_ascii=False)};
const EMBEDDED_CAR_RULES = {json.dumps(car_rules, ensure_ascii=False)};
"""

    modified_js = js.replace(
        "async function loadModuleData(mod) {",
        f"async function loadModuleData(mod) {{\n  currentModule = mod;\n  if (mod === 'car') {{\n    allQuestions = EMBEDDED_CAR_QS;\n    cheatSheetData = EMBEDDED_CAR_CHEAT;\n    masterRulesData = EMBEDDED_CAR_RULES;\n  }} else {{\n    allQuestions = EMBEDDED_MOTO_QS;\n    cheatSheetData = EMBEDDED_MOTO_CHEAT;\n    masterRulesData = EMBEDDED_MOTO_RULES;\n  }}\n  updateModuleHeaderUI();\n  updateCategoryAndTopicDropdowns();\n  updateFilteredQuestions();\n  return;\n"
    )

    full_script = f"<script>\n{embedded_data_js}\n{modified_js}\n</script>"
    html = html.replace('<script src="app.js"></script>', full_script)

    with open('standalone_app.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully built standalone_app.html!")

if __name__ == '__main__':
    build_standalone()
