from decimal import Decimal

from app.data_loader import load_bank_data
from app.services.financial_engine import calculate_total_income
from app.services.financial_engine import calculate_total_expenses
from app.services.financial_engine import calculate_savings

def test_calculate_total_income() -> None:
    user = load_bank_data()

    income = calculate_total_income(user)

    assert income == Decimal("16830")
    

def test_calculate_total_expense() -> None:
    user = load_bank_data()

    expense = calculate_total_expenses(user)

    assert expense == Decimal("9604.27")
    
def test_calculate_savings() -> None:
    
    savings, savings_rate = calculate_savings(Decimal("1000"), Decimal("700"))
    assert savings == Decimal("300")
    assert savings_rate == Decimal("0.3")
    
def test_calculate_with_zero_income() -> None:
    
    savings, savings_rate = calculate_savings(Decimal("0"), Decimal("500"))
    assert savings == Decimal("-500")
    assert savings_rate == Decimal("0")