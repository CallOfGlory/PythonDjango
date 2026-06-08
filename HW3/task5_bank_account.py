class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено на {amount} грн. Новий баланс: {self.balance} грн.")
        else:
            print("Сума поповнення має бути додатньою!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів на рахунку!")
        elif amount <= 0:
            print("Сума зняття має бути додатньою!")
        else:
            self.balance -= amount
            print(f"Знято {amount} грн. Новий баланс: {self.balance} грн.")

    def display_balance(self):
        print(f"Баланс рахунку {self.owner}: {self.balance} грн.")


if __name__ == "__main__":
    account = BankAccount("Іван Петренко", 1000)
    account.display_balance()

    account.deposit(500)
    account.withdraw(300)
    account.withdraw(1500)
    account.display_balance()
