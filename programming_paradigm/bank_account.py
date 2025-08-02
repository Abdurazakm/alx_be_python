class BankAccount:
    def __init__(self):
        self.account_balance = 0.0
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account_balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.account_balance -= amount
    def display(self):
        print(f"Current account balance: ${self.account_balance:.2f}")
user1 = BankAccount()
user1.deposit(100.0)
user1.withdraw(50.0)
user1.display()
