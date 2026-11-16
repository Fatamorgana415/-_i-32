from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "data" / "expenses.csv"


class Expense:
    currency = "UAH"   
    count = 0          
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.count += 1

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

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def describe(self):
        return (f"{self.date} {self.category} "
                f"{self.amount:.2f} {self.currency} ({self.comment})")


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
    expenses = load_csv()
    print("Створено обʼєктів:", Expense.count)

    print("\nВалюта:", Expense.currency)
    for e in expenses:
        print(" ", e.describe())

    Expense.set_currency("USD")
    print("\nПісля Expense.set_currency('USD'):")
    for e in expenses:
        print(" ", e.describe())