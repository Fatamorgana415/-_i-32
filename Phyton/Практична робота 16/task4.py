import json
from datetime import date

print("Олександра, IT-32")

data_with_date = {
    "id": 1,
    "date": date(2026, 9, 21),
    "description": "Test date serialization"
}

print("--- Спроба 1: без обробки ---")
try:
    json.dumps(data_with_date)
except TypeError as e:
    print(f"TypeError: {e}")

print("\n--- Спосіб 1: default=str ---")
def date_converter(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

json_str_1 = json.dumps(data_with_date, default=date_converter)
print("Серіалізовано:", json_str_1)
data_loaded_1 = json.loads(json_str_1)

print("\n--- Спосіб 2: повний цикл ---")
data_to_save = data_with_date.copy()
data_to_save["date"] = data_to_save["date"].isoformat()
json_str_2 = json.dumps(data_to_save)
print("Серіалізовано:", json_str_2)

data_loaded_2 = json.loads(json_str_2)
data_loaded_2["date"] = date.fromisoformat(data_loaded_2["date"])

print(f"Дані збігаються: {data_loaded_2 == data_with_date}")
print(f"Тип дати після читання: {type(data_loaded_2['date']).__name__}")