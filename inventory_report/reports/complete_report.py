from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        data = self.inventory
        oldest = self.oldest_making_date(data)
        closest = self.shutest_expiration_date(data)
        largest = self.largest_inventory(data)
        companies = self.get_all_companies(data)

        return (
            f"Oldest manufacturing date: {oldest}\n"
            f"Closest expiration date: {closest}\n"
            f"Company with the largest inventory: {largest}\n"
            f"Stocked products by company:\n"
            f"{companies}"
        )

    def get_all_companies(self, data: list[Inventory]) -> str:
        companies: dict[str, int] = {}

        for inventory in data:
            for i in inventory.data:
                if not companies.get(i.company_name):
                    companies[i.company_name] = 1
                else:
                    companies[i.company_name] += 1

        string_to_return = ""

        for key, value in companies.items():
            company = f"- {key}: {value}\n"
            string_to_return += company

        return string_to_return
