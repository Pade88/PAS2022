from Company import Company
from IOManager import IOManager
from Logger import LogFile

COMPANIES_DB_FILE = "companies_db.json"


class CompanyManager:
    def __init__(self):
        self.companies_list = None

    def create_companies(self, raw_data):
        self.companies_list = [Company(*item.values()) for item in raw_data["Companies"] if Company.sanity_check(
                               Company(*item.values()))]
        LogFile.log_message(f"Company lists: {self.companies_list}", "debug")

    def get_companies_names(self):
        LogFile.log_message(f"Company {self.get_companies_names.__name__} called", "debug")
        return [company.name for company in self.companies_list]

    def get_company(self):
        LogFile.log_message(f"Company {self.get_company.__name__} called", "debug")
        return self.companies_list

    def get_company_suppliers(self, company_name):
        LogFile.log_message(f"Company {self.get_company_suppliers.__name__} called", "debug")
        for item in self.companies_list:
            if item.name == company_name:
                return item.suppliers

    def add_new_supplier(self, company, supplier):
        LogFile.log_message(f"Company {self.add_new_supplier.__name__} called with {locals()}", "debug")
        IOManager.expand_json(COMPANIES_DB_FILE, company, supplier)
        self.companies_list.clear()

        raw_data = IOManager.load_json(COMPANIES_DB_FILE)
        self.create_companies(raw_data)

    def remove_company(self, company_name):
        # Delete from json -> No check needed, is performed there
        try_del = IOManager.shrink_json(COMPANIES_DB_FILE, company_name)
        # Reload data
        self.companies_list.clear()
        raw_data = IOManager.load_json(COMPANIES_DB_FILE)
        self.create_companies(raw_data)
        return try_del

