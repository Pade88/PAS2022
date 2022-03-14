from Logger import LogFile


class Company:
    def __init__(self, __name, __suppliers):
        self._name = __name
        self._suppliers = __suppliers.split(",")

    def __str__(self):
        return "{} company have the following suppliers: {}".format(self._name, self._suppliers)

    def sanity_check(self):
        # FIXME
        return True

    @property
    def name(self):
        LogFile.log_message(f"Company name getter called!", "info")
        return self._name

    @name.setter
    def name(self, new_name):
        LogFile.log_message(f"Company name setter called with {locals()}", "info")
        self._name = new_name

    @property
    def suppliers(self):
        LogFile.log_message(f"Suppliers getter called!", "info")
        return self._suppliers

    @suppliers.setter
    def suppliers(self, new_suppliers):
        LogFile.log_message(f"Supplier setter called with {locals()}", "info")
        self._suppliers = new_suppliers
