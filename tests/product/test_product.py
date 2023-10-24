from inventory_report.product import Product


def test_create_product() -> None:
    id = "2"
    product = "Popper-ram"
    company = "Company_example"
    manufacturing = "2023-10-23"
    expiration = "2023-10-24"
    serial = "789"
    storage = "Pesca_Esportiva"

    product_ex = Product(
        id,
        product,
        company,
        manufacturing,
        expiration,
        serial,
        storage,
    )

    assert product_ex.id == id
    assert product_ex.product_name == product
    assert product_ex.company_name == company
    assert product_ex.manufacturing_date == manufacturing
    assert product_ex.expiration_date == expiration
    assert product_ex.serial_number == serial
    assert product_ex.storage_instructions == storage
