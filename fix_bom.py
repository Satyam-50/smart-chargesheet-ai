import os

for fname in ['checklists.json', '.env']:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8-sig') as f:
            text = f.read()
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Rewrote {fname} without BOM")
    else:
        print(f"{fname} not found")
