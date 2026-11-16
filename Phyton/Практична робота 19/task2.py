class Wallet:
    def __init__(self, owner, balance):
        if not str(owner).strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner
        self.__balance = round(balance, 2)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.__balance:
            raise ValueError("not enough money")
        self.__balance = round(self.__balance - amount, 2)


if __name__ == "__main__":
    wallet = Wallet("Sasha Romanitch", 1500)
    wallet.deposit(500)
    wallet.withdraw(300)
    print("Баланс через метод:", wallet.get_balance())

    try:
        wallet.withdraw(10000)
    except ValueError as e:
        print("Помилка зняття:", e)

    try:
        print(wallet.__balance)
    except AttributeError as e:
        print("wallet.__balance ->", type(e).__name__ + ":", e)

    print("wallet._Wallet__balance ->", wallet._Wallet__balance)
    print("wallet.__dict__ ->", wallet.__dict__)

    wallet._Wallet__balance = -999   
    print("Після обходу захисту:", wallet.get_balance())