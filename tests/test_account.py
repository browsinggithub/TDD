import pytest
from bank.bank import Bank

@pytest.fixture(
    name="account"
)
def make_account():
    bank = Bank()
    
    return bank.open_account( name = "Cameron")


def test_open_account(account):
     assert account.name == "Cameron"

def test_deposit_money(account):
   
   
    account.make_money(
        100
    )
    assert account.balance == 100