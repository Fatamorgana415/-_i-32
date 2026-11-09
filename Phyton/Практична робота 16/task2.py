import json
from datetime import date

print("Олександра, IT-32")

input_path = "data/expenses.json"
output_path = "data/expenses_updated.json"

with open(input_path, encoding="utf-8") as f:
    records = json.load(f)

initial_count = len(records)

new_record = {
    "date": date.today().isoformat(),
    "category": "other",
    "amount": 50.0,
    "comment": "new record"
}
records.append(new_record)

filtered_records = [r for r in records if r["amount"] >= 10]
deleted_count = len(records) - len(filtered_records)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(filtered_records, f, indent=2, ensure_ascii=False)

print(f"added: 1")
print(f"deleted: {deleted_count}")
print(f"saved: {output_path} ({len(filtered_records)} records)")