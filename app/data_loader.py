from __future__ import annotations

import json
from pathlib import Path

from app.models.user import User


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "mock_bank_data.json"


def load_bank_data(path: str | Path = DEFAULT_DATA_PATH) -> User:
	"""Load bank data from JSON and return the typed user model."""
	data_path = Path(path)

	with data_path.open(encoding="utf-8") as data_file:
		data = json.load(data_file)

	if not isinstance(data, dict):
		raise ValueError("Bank data must contain a JSON object at the root")

	return User.from_dict(data)
