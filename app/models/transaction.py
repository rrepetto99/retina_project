from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any


@dataclass(slots=True)
class Transaction:
	id: str
	date: date
	amount: Decimal
	currency: str
	description: str
	transaction_type: str
	merchant: str | None = None
	category: str | None = None

	@classmethod
	def from_dict(cls, data: dict[str, Any]) -> Transaction:
		return cls(
			id=data["id"],
			date=date.fromisoformat(data["date"]),
			amount=Decimal(str(data["amount"])),
			currency=data["currency"],
			description=data["description"],
			merchant=data.get("merchant"),
			category=data.get("category"),
			transaction_type=data["transaction_type"],
		)
