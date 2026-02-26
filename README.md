# Smart Chargesheet Review Assistant
1. `pip install -r requirements.txt`
2. **Obtain a valid Gemini API key** from Google Cloud Console:
   - Go to https://console.cloud.google.com/apis/credentials
   - Create or select a project, then make an API key.
   - Enable the **Generative Language API** (aka generativelanguage.googleapis.com).
   - Copy the key and place it in a file named `.env` (same folder as `app.py`):
     ```
     GEMINI_API_KEY=AIzaSyYourRealKeyGoesHere
     ```
   - **Tip:** The key must be valid and unrestricted or suitably scoped; the placeholder
     in examples (`AIzaSyNewGeneratedKeyHere`) will trigger a 400 error.
   - Add `.env` to `.gitignore` so you don’t accidentally commit it (already done).
3. Run the app with `streamlit run app.py`.

> If you see `Error loading checklists.json: Unexpected UTF-8 BOM`
> resave the JSON with **UTF‑8 without BOM** or use the built‑in loader which
> already handles BOM automatically.
