import json

with open("spells.json", "r") as f:
    content = f.read()
    db = json.loads(content)
    for spell in db:
        entry = db[spell]
        desc = entry["description"]