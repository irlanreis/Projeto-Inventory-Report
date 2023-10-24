from inventory_report.product import Product


def test_product_report() -> None:
    id = "2"
    product_name = "Popper-ram"
    company = "Company_example"
    manufacturing = "2023-10-23"
    expiration = "2023-10-24"
    serial = "789"
    storage = "Pesca_Esportiva"

    product_ex = Product(
        id,
        product_name,
        company,
        manufacturing,
        expiration,
        serial,
        storage,
    )

    report_product = str(product_ex)

    assert report_product == (
        f"The product {id} - {product_name} "
        f"with serial number {serial} "
        f"manufactured on {manufacturing} "
        f"by the company {company} "
        f"valid until {expiration} "
        f"must be stored according to the following instructions: "
        f"{storage}."
    )
