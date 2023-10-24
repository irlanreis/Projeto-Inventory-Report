from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import date, datetime


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventory: list[Inventory]

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory.append(inventory)

    def generate(self) -> str:
        data_curr = self.inventory
        oldest_making = self.oldest_making_date(data_curr)
        shutest = self.shutest_expiration_date(data_curr)
        larget = self.largest_inventory(data_curr)

        return (
            f"Oldest manufacturing date: {oldest_making} "
            f"Closest expiration date: {shutest} "
            f"Company with the largest inventory: {larget}"
        )

    def oldest_making_date(self, data: list[Inventory]) -> str:
        oldest_data = date.today()

        for inventory in data:
            products = inventory.data
            oldest = min(
                item.manufacturing_date for item in products
            )

            if datetime.strptime(oldest, "%Y-%m-%d").date() < oldest_data:
                oldest_data = datetime.strptime(oldest, "%Y-%m-%d").date()

        return str(oldest_data)

    def shutest_expiration_date(self, data: list[Inventory]) -> str:
        today = date.today()
        shutest_date = datetime.strptime("2500-01-01", "%Y-%m-%d").date()

        for inventory in data:
            products_inventory = inventory.data
            shutest = min(
                item.expiration_date
                for item in products_inventory
                if datetime.strptime(item.expiration_date, "%Y-%m-%d").date()
                > today
            )

            if datetime.strptime(shutest, "%Y-%m-%d").date() < shutest_date:
                shutest_date = datetime.strptime(shutest, "%Y-%m-%d").date()

        return str(shutest_date)

    def largest_inventory(self, data: list[Inventory]) -> str:
        companies: dict[str, int] = {}

        for inventory in data:
            for i in inventory.data:
                if not companies.get(i.company_name):
                    companies[i.company_name] = 1
                else:
                    companies[i.company_name] += 1

        return max(companies, key=lambda i: companies[i])
