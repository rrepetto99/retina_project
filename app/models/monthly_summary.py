from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass(slots= True)
class MonthlySummary:
    month: date
    income: Decimal
    expenses: Decimal
    savings: Decimal
    savings_rate: Decimal
    