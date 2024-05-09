import json
from dataclasses import InitVar, field, dataclass
from datetime import datetime
from typing import Any
from itertools import count

from consts import CATEGORIES, FILE


def read_last_id(file: str) -> int:
    """ Чтение ID из файла. Если файла нет, начинает с 1. """
    try:
        with open(file, "r", encoding="utf-8") as f:
            last_note = f.readlines()[-1]
            last_id = json.loads(last_note)['id']
        return int(last_id) + 1 if last_id else 1
    except (FileNotFoundError, IndexError):
        return 1


CURRENT_ID = count(read_last_id(FILE))


@dataclass
class Note:
    id: int = field(default_factory=CURRENT_ID.__next__, init=False)
    _category: str = field(repr=False, init=False)
    _amount: int = field(repr=False, init=False)
    description: str

    category: InitVar[str]
    amount: InitVar[int]
    date: datetime = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

    def __post_init__(self, category: str, amount: int):
        self.category = category.lower()
        self.amount = amount

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value in CATEGORIES:
            self._category = value
        else:
            raise ValueError(f"Допустимые значения для категории {', '.join(CATEGORIES)}")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if int(value) > 0:
            self._amount = value
        else:
            raise ValueError(f"Сумма {value} должна быть больше нуля")

    def to_dict(self) -> dict[str, Any]:
        dict_note = {
            "id": self.id,
            "Дата": self.date,
            "Категория": self.category.lower(),
            "Сумма": str(self.amount),
            "Описание": self.description.lower()
        }
        return dict_note
