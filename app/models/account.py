from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

from app.models.transaction import Transaction


@dataclass(slots=True)
class Account:
	id: str
	bank: str
	account_name: str
	account_type: str
	currency: str
	opening_balance: Decimal
	balance: Decimal
	transactions: list[Transaction] = field(default_factory=list)

	@classmethod
	def from_dict(cls, data: dict[str, Any]) -> Account:
		return cls(
			id=data["id"],
			bank=data["bank"],
			account_name=data["account_name"],
			account_type=data["account_type"],
			currency=data["currency"],
			opening_balance=Decimal(str(data["opening_balance"])),
			balance=Decimal(str(data["balance"])),
			transactions=[
				Transaction.from_dict(transaction)
				for transaction in data.get("transactions", [])
			],
		)
