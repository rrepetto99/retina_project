from decimal import Decimal
from datetime import date

from app.data_loader import load_bank_data



def test_load_bank_data_returns_expected_user_and_accounts() -> None:
	user = load_bank_data()
	transaction_count = sum(
		len(account.transactions) for account in user.accounts
	)

	assert user.id == "user_001"
	assert len(user.accounts) == 3
	assert transaction_count == 192
	assert user.total_balance == Decimal("15110.73")
	assert user.base_currency == "EUR"


def test_transactions_have_correct_types() -> None:
    user = load_bank_data()

    transaction = user.accounts[0].transactions[0]

    assert isinstance(transaction.date, date)
    assert isinstance(transaction.amount, Decimal)