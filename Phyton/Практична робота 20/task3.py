class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount

class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month

class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people

def total_monthly(expenses):
    total = 0.0
    for e in expenses:
        total += e.monthly_cost()  
    return total

def build_expenses():
    return [
        Expense("05.09.2026", "food", 85.50),
        RecurringExpense("01.09.2026", "transport", 20, 22),
        RecurringExpense("01.09.2026", "mobile", 150, 1),
        SharedExpense("01.09.2026", "rent", 9000, 3),
        SharedExpense("10.09.2026", "internet", 400, 2),
    ]

if __name__ == "__main__":
    expenses = build_expenses()
    for e in expenses:
        print(f"{type(e).__name__:17} {e.category:10} {e.monthly_cost():9.2f}")
    print(f"Загальна місячна вартість: {total_monthly(expenses):.2f}")