import os
import json
import google.genai as genai
from dotenv import load_dotenv

# load .env so the key is available both from CLI and when imported by app
load_dotenv()

def extract_case_summary(cleaned_text):
    """Return a structured summary or an error dict.

    The caller expects a dictionary with either the parsed JSON or an "error"
    key describing what went wrong. A missing/invalid API key is handled
    explicitly to make debugging easier.
    """

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY is missing.  Please set it in your .env file or environment."}

    # ensure the installed genai library supports the new Client API
    if not hasattr(genai, 'Client'):
        return {"error": "Installed google-genai package is outdated; please run 'pip install -U google-genai' and restart the app."}

    try:
        client = genai.Client(api_key=api_key)
    except AttributeError as e:
        # this shouldn't happen because we checked above, but catch explicitly
        return {"error": "genai.Client not available; upgrade the google-genai package."}
    except Exception as e:
        return {"error": f"failed to initialize Gemini client: {e}"}

    prompt = f"""
You are a legal AI. Extract details strictly in JSON format.

{{
  "fir_details": "",
  "accused": [],
  "victims": [],
  "incident_facts": "",
  "legal_sections": []
}}

Text:
{cleaned_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        raw = response.text.strip()

        if raw.startswith("```"):
            raw = raw.replace("```json", "").replace("```", "").strip()

        return json.loads(raw)
    except Exception as e:
        msg = str(e)
        if "API key not valid" in msg or "API_KEY_INVALID" in msg:
            return {"error": "Invalid Gemini API key. Please generate a new key in the Google Cloud console and update GEMINI_API_KEY."}
        return {"error": msg}