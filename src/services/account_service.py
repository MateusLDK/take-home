from src.models.account import Account
from src.models.exceptions import InexistingAccountError


class AccountStore:
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def reset(self):
        self._accounts.clear()

    def get(self, account_id: str) -> Account | None:
        return self._accounts.get(account_id)

    def get_or_create(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            self._accounts[account_id] = Account(account_id, 0)
        return self._accounts[account_id]


class AccountService:
    def __init__(self):
        self.store = AccountStore()

    def reset(self):
        self.store.reset()

    def get_balance(self, account_id: str) -> int:
        account = self.store.get(account_id)
        if account is None:
            return None
        return account.get_balance()

    def deposit(self, account_id: str, amount: int) -> Account:
        account = self.store.get_or_create(account_id)
        account.deposit(amount)
        return account

    def withdraw(self, account_id: str, amount: int) -> Account:
        account = self.store.get(account_id)
        if account is None:
            raise InexistingAccountError(f"Account {account_id} does not exist")
        account.withdraw(amount)
        return account

    def transfer(
        self, from_account_id: str, to_account_id: str, amount: int
    ) -> tuple[Account, Account]:

        from_account = self.withdraw(from_account_id, amount)
        to_account = self.deposit(to_account_id, amount)

        return from_account, to_account
