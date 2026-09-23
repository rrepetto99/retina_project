from decimal import Decimal
from collections import defaultdict
from app.models.transaction import Transaction
from app.models.user import User


def _flatten_transactions(source: User | list[Transaction]) -> list[Transaction]:
    if isinstance(source, User):
        transactions: list[Transaction] = []
        for account in source.accounts:
            transactions.extend(account.transactions)
        return transactions    

    return list(source)


def calculate_total_income(transactions: User | list[Transaction]) -> Decimal:
    total_income = Decimal("0")

    for transaction in _flatten_transactions(transactions):
        if transaction.category == "income":
            total_income += transaction.amount

    return total_income


def calculate_total_expenses(transactions: User | list[Transaction]) -> Decimal:
    total_expenses = Decimal("0")

    for transaction in _flatten_transactions(transactions):
        if transaction.amount < 0 and transaction.category not in {"income", "transfer"}:
            total_expenses += abs(transaction.amount)

    return total_expenses


def calculate_savings(total_income: Decimal, total_expenses: Decimal) -> tuple[Decimal, Decimal]:
    total_savings = total_income - total_expenses

    if total_income == Decimal("0"):
        savings_rate = Decimal("0")
    else:
        savings_rate = total_savings / total_income

    return total_savings, savings_rate

def calculate_expenses_by_category(
    transactions: User | list[Transaction],
) -> dict[str, Decimal]:
    expenses_by_category: dict[str, Decimal] = defaultdict(lambda: Decimal("0"))

    for transaction in _flatten_transactions(transactions):
        if (
            transaction.amount < 0
            and transaction.category not in {"income", "transfer"}
        ):
            category = transaction.category or "uncategorized"
            expenses_by_category[category] += abs(transaction.amount)

    return dict(expenses_by_category)