import json

def load_checklists(filepath="checklists.json"):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_missing_items_check(cleaned_text, crime_type, checklists):
    if crime_type == "UNKNOWN" or crime_type not in checklists:
        return []

    required_items = checklists[crime_type]["required_items"]
    text_lower = cleaned_text.lower()
    results = []
    
    for item in required_items:
        keywords = item.lower().replace("/", " ").replace("(", "").replace(")", "").split()
        valid_keywords = [k for k in keywords if len(k) > 3]
        
        if not valid_keywords:
            continue
            
        matched_keywords = sum(1 for kw in valid_keywords if kw in text_lower)
        
        if matched_keywords >= len(valid_keywords) * 0.7:
             status = "✅ PRESENT"
             detail = f"Found '\''{item}'\'\'."
        elif matched_keywords > 0:
             status = "⚠ PARTIAL"
             detail = f"Partial match for '\''{item}'\'\'."
        else:
             status = "❌ MISSING"
             detail = "Item not detected."
             
        results.append({"item": item, "status": status, "detail": detail})
        
    return results
