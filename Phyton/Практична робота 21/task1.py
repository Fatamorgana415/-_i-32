import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "data" / "expenses.csv"
JSON_PATH = BASE_DIR / "data" / "expenses.json"

class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @classmethod
    def from_csv_line(cls, line):
        date, category, amount, comment = line.strip().split(";")
        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"], float(data["amount"]),
                   data.get("comment", ""))

    @classmethod
    def from_input(cls):
        date = input("Дата (YYYY-MM-DD): ").strip()
        category = input("Категорія: ").strip()
        amount = float(input("Сума: ").strip())
        comment = input("Коментар: ").strip()
        return cls(date, category, amount, comment)

    def as_tuple(self):
        return (self.date, self.category, self.amount, self.comment)

    def describe(self):
        return f"{self.date} {self.category} {self.amount:.2f} ({self.comment})"

def load_csv(path=CSV_PATH):
    expenses = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.lower().startswith("date"):
                continue   
            expenses.append(Expense.from_csv_line(line))
    return expenses


def load_json(path=JSON_PATH):
    with open(path, encoding="utf-8") as f:
        return [Expense.from_dict(item) for item in json.load(f)]

if __name__ == "__main__":
    expense = Expense.from_csv_line("2026-09-21;food;85.50;lunch")
    print(expense.category, expense.amount)

    from_csv = load_csv()
    from_json = load_json()
    print("З CSV: ", len(from_csv))
    print("З JSON:", len(from_json))
    same = [e.as_tuple() for e in from_csv] == [e.as_tuple() for e in from_json]
    print("Дані однакові:", same)

    if input("Додати витрату з клавіатури? (y/n): ").strip().lower() == "y":
        print(Expense.from_input().describe())