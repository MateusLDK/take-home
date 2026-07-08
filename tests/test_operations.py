# balance tests
import pytest

from src.models.exceptions import InexistingAccountError, InsufficientFundsError
from src.services.account_service import AccountService


@pytest.fixture
def accountService():
    return AccountService()


def test_get_balance(accountService):
    accountService.deposit("1234", 100)
    assert accountService.get_balance("1234") >= 0


def test_get_balance_no_account(accountService):
    assert accountService.get_balance("1234") == 0


# deposit tests
def test_deposit_no_account(accountService):
    accountService.deposit("1234", 100)
    assert accountService.get_balance("1234") == 100


def test_deposit_existing_account(accountService):
    accountService.deposit("1234", 100)
    accountService.deposit("1234", 100)
    assert accountService.get_balance("1234") == 200


# withdraw tests
def test_withdraw(accountService):
    accountService.deposit("1234", 100)
    accountService.withdraw("1234", 50)
    assert accountService.get_balance("1234") == 50


def test_withdraw_no_account(accountService):
    with pytest.raises(InexistingAccountError):
        accountService.withdraw("1234", 50)


def test_withdraw_insufficient_funds(accountService):
    accountService.deposit("1234", 100)
    with pytest.raises(InsufficientFundsError):
        accountService.withdraw("1234", 200)

    assert accountService.get_balance("1234") == 100


# transfer tests
def test_transfer(accountService):
    accountService.deposit("1234", 100)
    accountService.deposit("5678", 100)
    accountService.transfer("1234", "5678", 50)
    assert accountService.get_balance("1234") == 50
    assert accountService.get_balance("5678") == 150


def test_transfer_no_from_account(accountService):
    with pytest.raises(InexistingAccountError):
        accountService.transfer("1234", "5678", 50)


def test_transfer_no_funds(accountService):
    accountService.deposit("1234", 100)
    accountService.deposit("5678", 100)
    with pytest.raises(InsufficientFundsError):
        accountService.transfer("1234", "5678", 150)

    assert accountService.get_balance("1234") == 100
    assert accountService.get_balance("5678") == 100


# reset assignment
def test_reset(accountService):
    accountService.deposit("1234", 100)
    accountService.reset()
    assert accountService.get_balance("1234") == 0
