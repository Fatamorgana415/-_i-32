import csv
import json
import os

print("Олександра, IT-32")

csv_path = "data/expenses.csv"
json_path = "data/expenses.json"

records = []
with open(csv_path, encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        if not row or row[0].startswith("#"):
            continue
        if "date" in row[0] or "amount" in row:
            continue
            
        date, category, amount, comment = row
        records.append({
            "date": date,
            "category": category,
            "amount": float(amount),
            "comment": comment
        })

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)

file_size = os.path.getsize(json_path)

print(f"records: {len(records)}")
print(f"saved: {json_path} ({file_size} bytes)")