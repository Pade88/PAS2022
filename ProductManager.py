from Product import Product
from Logger import LogFile
from IOManager import IOManager

SUPPLIERS_DB_FILE = "suppliers_db.json"


class ProductsManager:
    def __init__(self):
        self.products_list = list()

    def create_products(self, raw_data):
        for supplier in raw_data["Suppliers"]:
            for product in supplier["product_list"]:
                name = product["name"]
                price = product["price"]
                quantity = product["quantity"]
                self.products_list.append(Product(supplier["name"], name, price, quantity))

        for item in self.products_list:
            LogFile.log_message(repr(item), "info")

    def get_products(self, owner):
        LogFile.log_message(f"ProductManager {self.get_products.__name__} called!", "debug")
        return [prod for prod in self.products_list if prod.owner == owner]

    def add_product(self, product):
        LogFile.log_message(f"ProductManager {self.add_product.__name__} called with {locals()}", "debug")
        IOManager.update_product_list(SUPPLIERS_DB_FILE, [product.owner, product.name,
                                                          product.price, product.quantity])
        self.products_list.append(product)
