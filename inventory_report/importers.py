from abc import ABC, abstractmethod
import csv
import json
from typing import Dict, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        data_import = list()

        with open(self.path) as file:
            products_path = json.load(file)

        for i in products_path:
            data_import.append(
                Product(
                    i["id"],
                    i["product_name"],
                    i["company_name"],
                    i["manufacturing_date"],
                    i["expiration_date"],
                    i["serial_number"],
                    i["storage_instructions"],
                )
            )
        return data_import


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        data_import = list()

        with open(self.path, encoding="utf-8") as file:
            information = csv.reader(file, delimiter=",", quotechar='"')
            header, *products_path = information

        for i in products_path:
            data_import.append(
                Product(
                    i[0],
                    i[1],
                    i[2],
                    i[3],
                    i[4],
                    i[5],
                    i[6],
                )
            )
        return data_import


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
