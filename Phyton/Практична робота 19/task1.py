class Wallet:
    def __init__(self, owner, balance):
        if not str(owner).strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner
        self.balance = round(balance, 2)


if __name__ == "__main__":
    ok = Wallet("Sasha Romanitch", 1500.555)
    print("Створено:", ok.owner, ok.balance)

    for owner, balance in [("", 100), ("Sasha Romanitch", -50)]:
        try:
            Wallet(owner, balance)
        except ValueError as e:
            print(f"Помилка для ({owner!r}, {balance}): {e}")