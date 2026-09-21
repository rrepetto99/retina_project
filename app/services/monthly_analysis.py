from app.models.user import User
from app.models.monthly_summary import MonthlySummary
from app.services.financial_engine import calculate_savings, calculate_total_expenses,calculate_total_income

def calculate_monthly_summary(user: User) -> list[MonthlySummary]:
    monthly_transactions ={}
    for account in user.accounts:
            for transaction in account.transactions:
                month = transaction.date.replace(day=1)
                monthly_transactions.setdefault(month,[]).append(transaction)
    
    summaries = []
    for month, transactions in monthly_transactions.items():
        income = calculate_total_income(transactions)
        expenses = calculate_total_expenses(transactions)
        savings, savings_rate = calculate_savings(income, expenses)
        
        summary = MonthlySummary(
            month=month,
            income=income,
            expenses=expenses,
            savings=savings,
            savings_rate=savings_rate
        )
        
        summaries.append(summary)
    return summaries
    
    