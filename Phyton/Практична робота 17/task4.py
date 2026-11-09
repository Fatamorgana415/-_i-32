import requests
import sys

print("Саша, IT-32")

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

print("1. Тестуємо таймаут (timeout=0.001):")
try:
    requests.get(URL, timeout=0.001)
except requests.Timeout:
    print("  -> Спіймано requests.Timeout", file=sys.stderr)
except requests.RequestException as e:
    print(f"  -> Інша помилка: {e}", file=sys.stderr)

print("\n2. Тестуємо неіснуючу адресу (404):")
try:
    bad_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/nonexistent"
    response = requests.get(bad_url, timeout=10)
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"  -> Спіймано requests.HTTPError: {e}", file=sys.stderr)

print("\n3. Тестуємо відсутність інтернету (ConnectionError):")
try:
    bad_domain = "https://this-domain-does-not-exist-12345.com"
    requests.get(bad_domain, timeout=10)
except requests.ConnectionError:
    print("  -> Спіймано requests.ConnectionError", file=sys.stderr)