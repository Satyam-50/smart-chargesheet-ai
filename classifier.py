def classify_crime_type(extracted_sections, checklists):
    if not extracted_sections:
        return {"crime_type": "UNKNOWN", "reason": "No sections provided"}

    for crime_key, schema in checklists.items():
        typical_sections = schema.get("typical_sections", [])
        for section in extracted_sections:
            if any(str(ts).lower() in str(section).lower() or str(section).lower() in str(ts).lower() for ts in typical_sections):
                return {"crime_type": crime_key, "display_name": schema["display_name"]}
                
    return {"crime_type": "UNKNOWN", "reason": "No match"}
