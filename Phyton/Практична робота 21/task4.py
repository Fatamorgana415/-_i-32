from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "data" / "expenses.csv"

class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, date, source, amount):
        self.date = date
        self.source = source
        self.amount = amount

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, date, from_card, to_card, amount):
        self.date = date
        self.from_card = from_card
        self.to_card = to_card
        self.amount = amount

    def balance_change(self):
        return 0


def load_expenses(path=CSV_PATH):
    result = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.lower().startswith("date"):
                continue
            date, category, amount, _comment = line.strip().split(";")
            result.append(Expense(date, category, float(amount)))
    return result


if __name__ == "__main__":
    items = load_expenses()
    items += [
        Income("2026-09-05", "scholarship", 2600.00),
        Income("2026-09-18", "part-time", 1500.00),
        Transfer("2026-09-10", "card A", "card B", 500.00),
    ]

    income = expenses = transfers = 0.0
    for item in items:                     
        change = item.balance_change()
        if change > 0:
            income += change
        elif change < 0:
            expenses += change
        else:
            transfers += change

    print("Sasha Romanitch, IT-32")
    print(f"income:   {income:10.2f}")
    print(f"expenses: {expenses:10.2f}")
    print(f"transfers:{transfers:10.2f}")
    print(f"balance:  {income + expenses + transfers:10.2f}")