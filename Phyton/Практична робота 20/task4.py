from task3 import Expense, build_expenses, total_monthly


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


if __name__ == "__main__":
    expenses = build_expenses()
    before = total_monthly(expenses)

    expenses.append(YearlyExpense("01.01.2026", "subscription", 1200))
    after = total_monthly(expenses)

    for e in expenses:
        print(f"{type(e).__name__:17} {e.category:12} {e.monthly_cost():9.2f}")
    print(f"До додавання річної витрати: {before:.2f}")
    print(f"Після додавання:             {after:.2f}")
    