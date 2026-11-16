from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "data" / "expenses.csv"

class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";")
        if len(parts) != 4:
            raise ValueError(f"очікується 4 поля, знайдено {len(parts)}")
        date, category, amount, comment = parts
        if not cls.is_valid_date(date):
            raise ValueError(f"некоректна дата {date!r}")
        if not cls.is_valid_amount(amount):
            raise ValueError(f"некоректна сума {amount!r}")
        return cls(date, category, float(amount), comment)

    def describe(self):
        return f"{self.date} {self.category} {self.amount:.2f} ({self.comment})"

def load_csv(path=CSV_PATH):
    expenses = []
    with open(path, encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            if not line.strip() or line.lower().startswith("date"):
                continue
            try:
                expenses.append(Expense.from_csv_line(line))
            except ValueError as e:
                print(f"Пропущено рядок {number}: {e}")
    return expenses

if __name__ == "__main__":
    print(Expense.is_valid_date("2026-02-30"))   
    print(Expense.is_valid_date("2026-09-21"))   
    print(Expense.is_valid_amount("85.50"))      
    print(Expense.is_valid_amount("abc"))        
    print(Expense.is_valid_amount(-5))           

    for bad in ["2026-02-30;food;10;x", "2026-09-21;food;abc;x", "2026-09-21;food"]:
        try:
            Expense.from_csv_line(bad)
        except ValueError as e:
            print(f"{bad!r} -> {e}")

    expenses = load_csv()
    print("Завантажено коректних витрат:", len(expenses))