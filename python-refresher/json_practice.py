import json
from pathlib import Path

# === 1) Python object → JSON string with dumps ===
expense = {
    "amount": 12.50,
    "category": "food",
    "date": "2026-05-12",
    "tags": ["lunch", "weekday"],
    "is_recurring": False,
    "notes": None,
}

# Compact (default): single line, minimal whitespace
compact = json.dumps(expense)
print("Compact JSON:")
print(compact)
print()

# Pretty-printed: easy to read for humans
pretty = json.dumps(expense, indent=2, sort_keys=True)
print("Pretty JSON:")
print(pretty)
print()

# === 2) JSON string → Python object with loads ===
raw_text = '{"name": "Paolo", "score": 42, "active": true, "tags": ["py", "ml"]}'
parsed = json.loads(raw_text)

print("Parsed type :", type(parsed))
print("Parsed value:", parsed)
print("Name field  :", parsed["name"])
print("First tag   :", parsed["tags"][0])

text = json.dumps(expense)
restored = json.loads(text)
assert restored == expense, "Round-trip failed!"
print("✅ Round-trip OK")

expenses = [
    {"amount": 12.50, "category": "food",      "date": "2026-05-10"},
    {"amount": 45.00, "category": "transport", "date": "2026-05-11"},
    {"amount": 8.00,  "category": "food",      "date": "2026-05-12"},
]

#es 3
DATA = Path("practice.json")

with DATA.open("w") as f:
    json.dump(expenses, f, indent=2)

with DATA.open("r") as f:
    expensesReloaded = json.load(f)

print(len(expensesReloaded))

#es 4
with open("sample_input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Loaded", len(data["users"]), "users")
top = max(data["users"], key=lambda u: u["score"])
print(f"Top scorer: {top['name']} with {top['score']}")

#es 5
#json.dumps({1,2,3})

#es 6
data = {"city": "Café Roma", "owner": "Józef"}
print(json.dumps(data))                                # default: escapes accents
print(json.dumps(data, ensure_ascii=False))            # preserves accents