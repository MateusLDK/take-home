class AccountException(Exception):
    "Base class for account exceptions"

    pass


class InsufficientFundsError(AccountException):
    "Exception raised when an account has insufficient funds"

    def __init__(self, message):
        super().__init__(message)


class InexistingAccountError(AccountException):
    "Exception raised when an account does not exits"

    def __init__(self, message):
        super().__init__(message)
