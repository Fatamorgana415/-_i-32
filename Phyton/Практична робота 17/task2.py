import requests
import csv
import sys

print("Саша, IT-32")

def get_rate(valcode):
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    try:
        response = requests.get(URL, params={"valcode": valcode, "json": ""}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[0]["rate"], data[0]["exchangedate"]
    except requests.RequestException as e:
        print(f"Помилка мережі: {e}", file=sys.stderr)
        sys.exit(1)

total_uah = 0.0
try:
    with open("data/expenses.csv", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if not row or row[0].startswith("#") or "date" in row[0]:
                continue
            total_uah += float(row[2])
except FileNotFoundError:
    print("Файл data/expenses.csv не знайдено!", file=sys.stderr)
    sys.exit(1)

rate_usd, date = get_rate("USD")
rate_eur, _ = get_rate("EUR")

print(f"rate date: {date}")
print(f"total: {total_uah:.2f} UAH = {total_uah / rate_usd:.2f} USD = {total_uah / rate_eur:.2f} EUR")