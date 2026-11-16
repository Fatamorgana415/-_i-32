class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner       
        self.balance = balance   

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not str(value).strip():
            raise ValueError("owner name can not be empty")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.__balance == 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.__balance:
            raise ValueError("not enough money")
        self.balance = self.__balance - amount


if __name__ == "__main__":
    wallet = Wallet("Sasha Romanitch", 1500)
    print(wallet.balance)
    wallet.balance = 1200.555
    print(wallet.balance)

    try:
        wallet.balance = -10
    except ValueError as e:
        print("ValueError:", e)

    try:
        wallet.owner = "   "
    except ValueError as e:
        print("ValueError:", e)

    try:
        wallet.is_empty = True
    except AttributeError as e:
        print("AttributeError:", e)

    print("is_empty:", wallet.is_empty)