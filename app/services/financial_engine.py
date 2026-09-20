from decimal import Decimal

from app.models.user import User


def calculate_total_income(user: User) -> Decimal:
	total_income = Decimal("0")

	for account in user.accounts:
		for transaction in account.transactions:
			if transaction.category == "income":
				total_income += transaction.amount

	return total_income

def calculate_total_expenses(user: User) -> Decimal:
    total_expenses = Decimal("0")

    for account in user.accounts:
        for transaction in account.transactions:
            if transaction.amount < 0 and transaction.category not in {"income", "transfer"}:
                total_expenses += abs(transaction.amount)

    return total_expenses