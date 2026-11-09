import requests
import sys

print("Саша, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()
    
    print("status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("currencies:", len(rates))
    
    for rate in rates:
        if rate["cc"] in ("USD", "EUR"):
            print(f"{rate['cc']}: {rate['rate']} (date: {rate['exchangedate']})")
            
except requests.RequestException as e:
    print(f"Помилка мережі: {e}", file=sys.stderr)
    sys.exit(1)
