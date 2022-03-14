from Logger import LogFile


class Supplier:
    def __init__(self, __name, __tax_identification, __product_list, __address, __in_charge, __phone):
        self._name = __name
        self._tax_identification = __tax_identification
        self._product_list = __product_list
        self._address = __address
        self._in_charge = __in_charge
        self._phone = __phone

    def __str__(self):
        return f'{self._name} with "{self._tax_identification}" tax identification, having address at {self.address} ' \
               f's represented by {self.in_charge} which can be called at {self.phone}!'

    def __repr__(self):
        args = [self._name, self.tax_identification, self._product_list, self.address, self.in_charge, self._phone]
        return f"Supplier({','.join(args)})"

    def sanity_check(self):
        # FIXME
        """
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
        """
        return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def tax_identification(self):
        return self._tax_identification

    @tax_identification.setter
    def tax_identification(self, new_tax_id):
        self._tax_identification = new_tax_id

    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, new_product_list):
        self._product_list = new_product_list

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    @property
    def in_charge(self):
        return self._in_charge

    @in_charge.setter
    def in_charge(self, new_in_charge):
        self._in_charge = new_in_charge

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        self._phone = new_phone