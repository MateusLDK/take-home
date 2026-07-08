from exceptions import InsufficientFundsError


class Account:
    def __init__(self, account_number: str, balance: int):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Account {self.account_number} has insufficient funds"
            )
        self.balance -= amount
        return self.balance
