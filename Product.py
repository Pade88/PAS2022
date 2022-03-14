from Logger import LogFile


class Product:
    def __init__(self, __owner, __name, __price, __quantity):
        self._owner = __owner
        self._name = __name
        self._price = __price
        self._quantity = __quantity

    def __repr__(self):
        return f'Furnizorul {self._owner} are produsul {self._name} costa {self._price} si sunt disponibile ' \
               f'{self._quantity} bucati!'

    @property
    def owner(self):
        LogFile.log_message(f"Product owner getter called!", "debug")
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        LogFile.log_message(f"Product owner setter called!", "debug")
        self._owner = new_owner

    @property
    def name(self):
        LogFile.log_message(f"Product name getter called!", "debug")
        return self._name

    @name.setter
    def name(self, new_name):
        LogFile.log_message(f"Product name getter called!", "debug")
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self.price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity