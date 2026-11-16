import csv
from pathlib import Path

from task3 import Wallet

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "data" / "expenses.csv"

BUDGET = 8000  

wallet = Wallet("Sasha Romanitch", BUDGET)
total = 0.0
processed = 0

with open(CSV_PATH, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        amount = float(row["amount"])
        try:
            wallet.withdraw(amount)
        except ValueError as e:
            print(f"Зупинка на витраті {row['date']} {row['category']} "
                  f"{amount:.2f} ({row['comment']}): {e}")
            break
        total += amount
        processed += 1

print(f"Оброблено витрат: {processed}")
print(f"Бюджет: {BUDGET:.2f}, списано: {total:.2f}")
print(f"Залишок: {wallet.balance:.2f}")