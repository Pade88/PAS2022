from Logger import LogFile


class Supplier:
    def __init__(self, _name, _tax_identification, _product_list, _address, _in_charge, _phone):
        self.name = _name
        self.tax_identification = _tax_identification
        self.product_list = _product_list
        self.address = _address
        self.in_charge = _in_charge
        self.phone = _phone

    def __str__(self):
        return '{SName} with "{taxId}" tax identification, having address at {addr}, is represented by {ich} ' \
               'which can be called at {phn}!'.format(SName=self.name, taxId=self.tax_identification, addr=self.address,
                                                      ich=self.in_charge, phn=self.phone)

    def sanity_check(self):
        LogFile.log_message("sanity_check called!", "info")

        if not isinstance(self.name, str):
            LogFile.log_message("Name -> {}, should be a string!".format(self.name), "error")
            return False
        if not isinstance(self.tax_identification, str) and len(self.tax_identification) == 9:
            LogFile.log_message("Tax identification -> {}, should be a 9 digits string or int!".format(
                self.tax_identification), "error")
            return False
        if not isinstance(self.product_list, list) or not isinstance(self.product_list, str):
            LogFile.log_message("Product list -> {}, should be a list!".format(self.product_list), "error")
            return False
        if not (isinstance(self.address, str) or len(self.address)) > 0:
            LogFile.log_message("Invalid address -> {}, should be non-empty string ".format(self.address), "error")
            return False
        if not (isinstance(self.in_charge, str) or len(self.in_charge) > 0):
            LogFile.log_message("Invalid in charge person -> {}, should be non-empty string ".format(
                self.in_charge), "error")
            return False
        if not (isinstance(self.phone, str) or isinstance(self.phone, int) or len(self.phone) == 10):
            LogFile.log_message("Invalid phone -> {}, should be non-empty, 10 digits string or int".format(
                self.phone), "error")
            return False

        LogFile.log_message("Valid object created, {}".format(self.__str__()), "info")
        return True

    def get_name(self):
        LogFile.log_message(f"Supplier {self.get_name.__name__} called!", "debug")
        return self.name

    def get_tax_identification(self):
        LogFile.log_message(f"Supplier {self.get_tax_identification.__name__} called!", "debug")
        return self.tax_identification

    def get_product_list(self):
        LogFile.log_message(f"Supplier {self.get_product_list.__name__} called!", "debug")
        return self.product_list

    def get_address(self):
        LogFile.log_message(f"Supplier {self.get_address.__name__} called!", "debug")
        return self.address

    def get_in_charge(self):
        LogFile.log_message(f"Supplier {self.get_in_charge.__name__} called!", "debug")
        return self.in_charge

    def get_phone(self):
        LogFile.log_message(f"Supplier {self.get_phone.__name__} called!", "debug")
        return self.phone

    def set_phone(self, new_phone):
        LogFile.log_message(f"Supplier {self.set_phone.__name__} called! with params {locals()}", "debug")
        self.phone = new_phone

    def set_in_charge(self, new_in_charge):
        LogFile.log_message(f"Supplier {self.set_in_charge.__name__} called! with params {locals()}", "debug")
        self.in_charge = new_in_charge

    def set_address(self, new_address):
        LogFile.log_message(f"Supplier {self.set_address.__name__} called! with params {locals()}", "debug")
        self.address = new_address

    def set_product_list(self, new_product_list):
        LogFile.log_message(f"Supplier {self.set_product_list.__name__} called! with params {locals()}", "debug")
        self.product_list = new_product_list

    def set_tax_identification(self, new_tax_identification):
        LogFile.log_message(f"Supplier {self.set_tax_identification.__name__} called! with params {locals()}", "debug")
        self.tax_identification = new_tax_identification

    def set_name(self, new_name):
        LogFile.log_message(f"Supplier {self.set_name.__name__} called! with params {locals()}", "debug")
        self.name = new_name
