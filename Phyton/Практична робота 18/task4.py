from task3 import Expense, load_expenses


class ExpenseBook:
    def __init__(self):
        self.items = []

    def add(self, expense):
        self.items.append(expense)

    def total(self):
        return sum(e.amount for e in self.items)

    def by_category(self, category):
        return sum(e.amount for e in self.items if e.category == category)

    def top(self, n):
        return sorted(self.items, key=lambda e: e.amount, reverse=True)[:n]


if __name__ == "__main__":
    book = ExpenseBook()
    for e in load_expenses():
        book.add(e)

    print(f"Всього: {book.total():.2f}")
    for cat in sorted({e.category for e in book.items}):
        print(f"  {cat}: {book.by_category(cat):.2f}")
    print("Топ-3 витрати:")
    for e in book.top(3):
        print(" ", e.describe())
        