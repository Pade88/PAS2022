from MainGUI import GUIBuilder
from IOManager import IOManager
from Logger import LogFile
from SuppliersManager import SupplierManager
from CompanyManager import CompanyManager
from ProductManager import ProductsManager

# Constants
SUPPLIERS_DB_FILE = "suppliers_db.json"
COMPANIES_DB_FILE = "companies_db.json"
DEBUG_MODE = True


if __name__ == '__main__':
    LogFile(DEBUG_MODE)
    # Load jsons data

    suppliers_raw_data = IOManager.load_json(SUPPLIERS_DB_FILE)
    companies_raw_data = IOManager.load_json(COMPANIES_DB_FILE)

    # Create transmissible-type object
    suppliers_handler = SupplierManager()
    companies_handler = CompanyManager()
    products_handler = ProductsManager()

    suppliers_handler.create_suppliers(suppliers_raw_data)
    companies_handler.create_companies(companies_raw_data)
    products_handler.create_products(suppliers_raw_data)

    GUI = GUIBuilder(companies_handler, suppliers_handler, products_handler)
