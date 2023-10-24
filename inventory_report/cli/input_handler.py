from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    types = ["simple", "complete"]
    if report_type not in types:
        raise ValueError("Report type is invalid.")

    inventory = Inventory()
    report = None

    for file in file_paths:
        process_returns(file, inventory)

    if report_type == "simple":
        report = SimpleReport()

    else:
        report = CompleteReport()

    report.add_inventory(inventory)
    return report.generate()


def process_returns(file_path: str, inventory: Inventory) -> None:
    if file_path.endswith(".json"):
        json_data = JsonImporter(file_path)
        inventory.add_data(json_data.import_data())
    elif file_path.endswith(".csv"):
        csv_data = CsvImporter(file_path)
        inventory.add_data(csv_data.import_data())
