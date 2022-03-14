from Logger import LogFile


class Company:
    def __init__(self, _name, _suppliers):
        self.name = _name
        self.suppliers = _suppliers

    def __str__(self):
        return "{} company have the following suppliers: {}".format(self.name, self.suppliers)

    def sanity_check(self):
        if not isinstance(self.name, str):
            LogFile.log_message(f"{self.name} should be string!", "error")
            return False
        elif not isinstance(self.suppliers, list) or not isinstance(self.suppliers, str):
            LogFile.log_message(f"{self.suppliers} should be list!", "error")
            return False
        LogFile.log_message("All parameters from Company class are checked!")
        return True

    def get_company_name(self):
        LogFile.log_message(f"{self.get_company_name.__name__} called!", "info")
        return self.name

    def set_company_name(self, new_name):
        LogFile.log_message(f"{self.set_company_name.__name__} called with {locals()}", "info")
        self.name = new_name

    def get_company_suppliers(self):
        LogFile.log_message(f"{self.get_company_suppliers.__name__} called!", "info")
        return self.suppliers.split(",")

    def set_company_suppliers(self, new_company_suppliers):
        LogFile.log_message(f"{self.set_company_suppliers.__name__} called with {locals()}", "info")
        self.suppliers = new_company_suppliers
