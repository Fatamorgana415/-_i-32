class Wallet:
    def __init__(self, owner, balance):
        if not str(owner).strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.__owner = owner
        self.__balance = round(balance, 2)

    @property
    def owner(self):
        return self.__owner

    def __del__(self):
        owner = getattr(self, "_Wallet__owner", "unknown")
        print(f"wallet of {owner} deleted")


if __name__ == "__main__":
    print("1) del wallet (єдине посилання)")
    wallet = Wallet("Sasha Romanitch", 1500)
    del wallet
    print("   після del\n")

    print("2) є друге посилання other = wallet")
    wallet = Wallet("Oksana Makarchuk", 800)
    other = wallet
    del wallet
    print("   після del wallet: обʼєкт ще живий через other")
    del other
    print("   після del other\n")

    print("3) обʼєкт живе до кінця програми")
    last = Wallet("Final Owner", 100)
    print("   кінець програми")