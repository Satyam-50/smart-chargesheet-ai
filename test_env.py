import os
from dotenv import load_dotenv
from checklist_engine import load_checklists

load_dotenv(dotenv_path='.env')
print('API key in env:', os.getenv('GEMINI_API_KEY'))
print('Loaded checklists count:', len(load_checklists('checklists.json')))
