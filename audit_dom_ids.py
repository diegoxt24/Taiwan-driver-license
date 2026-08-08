import re
import json

def audit_js_dom_references():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Find all document.getElementById('id') calls in app.js
    ids_in_js = set(re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", js))
    
    # Find all id="..." in index.html
    ids_in_html = set(re.findall(r'id=["\']([^"\']+)["\']', html))
    
    missing_in_html = ids_in_js - ids_in_html
    print("=== DOM ELEMENT AUDIT ===")
    print(f"Total IDs referenced in JS: {len(ids_in_js)}")
    print(f"Total IDs present in HTML: {len(ids_in_html)}")
    print(f"IDs referenced in JS but MISSING in HTML: {missing_in_html}")
    return missing_in_html

if __name__ == '__main__':
    audit_js_dom_references()
