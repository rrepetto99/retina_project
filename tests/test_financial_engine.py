from decimal import Decimal

from app.data_loader import load_bank_data
from app.services.financial_engine import calculate_total_income
from app.services.financial_engine import calculate_total_expenses
from app.services.financial_engine import calculate_savings

from app.services.monthly_analysis import calculate_monthly_summary
from app.services.financial_engine import calculate_expenses_by_category

def test_calculate_monthly_summary() -> None:
    user = load_bank_data()

    summaries = calculate_monthly_summary(user)

    assert len(summaries) == 6

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
    


def test_monthly_summary_has_six_months() -> None:
    user = load_bank_data()

    summaries = calculate_monthly_summary(user)

    assert len(summaries) == 6


def test_monthly_savings_equals_income_minus_expenses() -> None:
    user = load_bank_data()

    summaries = calculate_monthly_summary(user)

    for summary in summaries:
        assert summary.savings == summary.income - summary.expenses


def test_monthly_savings_rate_is_correct() -> None:
    user = load_bank_data()

    summaries = calculate_monthly_summary(user)

    for summary in summaries:
        if summary.income > 0:
            assert summary.savings_rate == (
                summary.savings / summary.income
            )
            
            
def test_calculate_expenses_by_category() -> None:
    user = load_bank_data()

    expenses = calculate_expenses_by_category(user)

    assert "groceries" in expenses
    assert "housing" in expenses
    assert "restaurants" in expenses
    assert "transport" in expenses
    assert "transfer" not in expenses
    assert expenses["housing"] == Decimal("4320")
    
    