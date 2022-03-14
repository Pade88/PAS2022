from Supplier import Supplier
from IOManager import IOManager
from Logger import LogFile

SUPPLIERS_DB_FILE = "suppliers_db.json"


class SupplierManager:
    def __init__(self):
        self.suppliers_list = []

    def create_suppliers(self, raw_data):
        self.suppliers_list = [Supplier(*item.values()) for item in raw_data["Suppliers"]
                               if True]

        for supplier in self.suppliers_list:
            LogFile.log_message(str(supplier), "info")

    def update_suppliers_list(self):
        LogFile.log_message(f"Supplier {self.update_suppliers_list.__name__} called", "debug")
        self.suppliers_list.clear()
        raw_data = IOManager.load_json(SUPPLIERS_DB_FILE)
        self.create_suppliers(raw_data)

    def add_new_supplier(self, *args):
        LogFile.log_message(f"Supplier {self.add_new_supplier.__name__} called with {locals()}", "debug")
        new_supplier = Supplier(*args)

        supplier_to_json = {"name": new_supplier.get_name(),
                            "tax_identification": new_supplier.get_tax_identification(),
                            "product_list": new_supplier.get_product_list(),
                            "address": new_supplier.get_address(),
                            "in_charge": new_supplier.get_in_charge(),
                            "phone": new_supplier.get_phone()}
        IOManager.update_json(SUPPLIERS_DB_FILE, supplier_to_json)
        LogFile.log_message(f"Furnizorul {supplier_to_json} a fost adaugat", "info")
        self.update_suppliers_list()

    def get_suppliers_names(self):
        LogFile.log_message(f"Supplier {self.get_suppliers_names.__name__} called", "debug")
        return [supplier.get_name() for supplier in self.suppliers_list]

    def get_suppliers(self):
        LogFile.log_message(f"Supplier {self.get_suppliers.__name__} called", "debug")
        return self.suppliers_list

    def get_suppliers_update(self, suppliers_names):
        LogFile.log_message(f"Supplier {self.get_suppliers_update.__name__} called with {locals()}", "debug")
        return [spl_item for item in suppliers_names for spl_item in self.suppliers_list
                if item.strip() == spl_item.get_name()]

    def search_supplier_by_tax(self, tax_number):
        LogFile.log_message(f"Supplier {self.search_supplier_by_tax.__name__} called with {locals()}", "debug")
        LogFile.log_message(f"Functia de cautare a furnizorilor dupa CUI a fost apelata!", "info")
        for supplier in self.suppliers_list:
            if supplier.get_tax_identification() == tax_number:
                return str(supplier)
