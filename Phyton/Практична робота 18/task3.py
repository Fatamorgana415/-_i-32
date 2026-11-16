import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
DEFAULT_CSV = BASE_DIR / "data" / "expenses.csv"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return f"{self.date} {self.category} {self.amount:.2f} ({self.comment})"

def load_expenses(path=DEFAULT_CSV):
    expenses = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            expenses.append(
                Expense(row["date"], row["category"], row["amount"], row["comment"])
            )
    return expenses

if __name__ == "__main__":
    LIMIT = 55 
    expenses = load_expenses()
    print("Обʼєктів Expense:", len(expenses))
    print(f"Великі витрати (> {LIMIT}):")
    for e in expenses:
        if e.is_big(LIMIT):
            print(" ", e.describe())
