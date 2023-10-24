from typing import Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        self._data = data if data else []

    @property
    def data(self) -> list[Product]:
        return self._data.copy()

    def add_data(self, data: list[Product]) -> None:
        self._data.extend(data)
