import json
import sys
import os

print("Олександра, IT-32")

settings_path = "settings.json"

default_settings = {
    "owner": "Ваше Ім'я",
    "group": "Ваша Група",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not os.path.exists(settings_path):
    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(default_settings, f, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
    sys.exit(0)

try:
    with open(settings_path, encoding="utf-8") as f:
        settings = json.load(f)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e.msg} at line {e.lineno} column {e.colno}", file=sys.stderr)
    sys.exit(1)

with open("data/expenses.json", encoding="utf-8") as f:
    records = json.load(f)

total_spent = sum(r["amount"] for r in records)
limit = settings["monthly_limit"]
left = limit - total_spent

print(f"limit: {limit:.2f} {settings['currency']}, spent: {total_spent:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")