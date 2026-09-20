from decimal import Decimal

from app.data_loader import load_bank_data
from app.services.financial_engine import calculate_total_income
from app.services.financial_engine import calculate_total_expenses

def test_calculate_total_income() -> None:
    user = load_bank_data()

    income = calculate_total_income(user)

    assert income == Decimal("16830")
    

def test_calculate_total_expense() -> None:
    user = load_bank_data()

    expense = calculate_total_expenses(user)

    assert expense == Decimal("9604.27")
    
