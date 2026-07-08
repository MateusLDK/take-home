class AccountExceptions(Exception):
    "Base class for account exceptions"

    pass


class InsufficientFundsError(AccountExceptions):
    "Exception raised when an account has insufficient funds"

    def __init__(self, message):
        self.message = message
