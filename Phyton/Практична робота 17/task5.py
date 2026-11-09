import requests
import json
import os
import time
import sys

print("Саша, IT-32")

CACHE_DIR = "cache"
CACHE_FILE = os.path.join(CACHE_DIR, "rates.json")
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_TTL = 3600

def get_from_api():
    try:
        response = requests.get(URL, params={"json": ""}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Помилка мережі: {e}", file=sys.stderr)
        sys.exit(1)

os.makedirs(CACHE_DIR, exist_ok=True)

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, encoding="utf-8") as f:
        cache_data = json.load(f)
    
    age = time.time() - cache_data["timestamp"]
    if age < CACHE_TTL:
        print(f"source: cache (age {int(age)} s)")
        sys.exit(0)

data = get_from_api()
with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump({"timestamp": time.time(), "data": data}, f, ensure_ascii=False)

print("source: api (cache saved)")