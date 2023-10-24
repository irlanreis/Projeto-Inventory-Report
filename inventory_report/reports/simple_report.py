from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import date, datetime


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventory: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory.append(inventory)

    def generate(self) -> str:
        data = self.inventory
        oldest = self.oldest_making_date(data)
        closest = self.shutest_expiration_date(data)
        larget = self.largest_inventory(data)

        return (
            f"Oldest manufacturing date: {oldest} "
            f"Closest expiration date: {closest} "
            f"Company with the largest inventory: {larget}"
        )

    def oldest_making_date(self, data: list[Inventory]) -> str:
        oldest_data = date.today()

        for inventory in data:
            products = inventory.data
            oldest = min(item.manufacturing_date for item in products)

            if datetime.strptime(oldest, "%Y-%m-%d").date() < oldest_data:
                oldest_data = datetime.strptime(oldest, "%Y-%m-%d").date()

        return str(oldest_data)

    def shutest_expiration_date(self, data: list[Inventory]) -> str:
        today = date.today()
        closest_data = datetime.strptime("2500-01-01", "%Y-%m-%d").date()

        for inventory in data:
            products = inventory.data
            closest = min(
                item.expiration_date
                for item in products
                if datetime.strptime(item.expiration_date, "%Y-%m-%d").date()
                > today
            )

            if datetime.strptime(closest, "%Y-%m-%d").date() < closest_data:
                closest_data = datetime.strptime(closest, "%Y-%m-%d").date()

        return str(closest_data)

    def largest_inventory(self, data: list[Inventory]) -> str:
        companies: dict[str, int] = {}

        for inventory in data:
            for item in inventory.data:
                if not companies.get(item.company_name):
                    companies[item.company_name] = 1
                else:
                    companies[item.company_name] += 1

        return max(companies, key=lambda item: companies[item])
