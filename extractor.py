import os
import json
import google.generativeai as genai

def extract_case_summary(cleaned_text):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY is missing."}
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
    You are a legal AI. Extract details strictly in JSON without markdown.
    {{
      "fir_details": "FIR number, date, PS",
      "accused": ["Name 1"],
      "victims": ["Name 1"],
      "incident_facts": "Incident facts",
      "legal_sections": ["IPC 379"]
    }}
    Text: {cleaned_text}
    """
    
    try:
        response = model.generate_content(prompt)
        raw_json = response.text.strip().replace('"```json', '').replace('"```', '')
        return json.loads(raw_json)
    except Exception as e:
        return {"error": str(e)}
