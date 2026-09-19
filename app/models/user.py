from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

from app.models.account import Account

@dataclass(slots=True)
class User:
	id: str
	name: str
	country: str
	base_currency: str
	accounts: list[Account] = field(default_factory=list)

	@classmethod
	def from_dict(cls, data: dict[str, Any]) -> User:
		user_data = data.get("user", data)
		return cls(
			id=user_data["id"],
			name=user_data["name"],
			country=user_data["country"],
			base_currency=user_data["base_currency"],
			accounts=[
				Account.from_dict(account)
				for account in data.get("accounts", [])
			],
		)

	@property
	def total_balance(self) -> Decimal:
		return sum((account.balance for account in self.accounts), Decimal("0"))

