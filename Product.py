from Logger import LogFile


class Product:
    def __init__(self, owner, name, price, quantity):
        self.owner = owner
        self.name = name
        self.price = price
        self.quantity = quantity

    def print_product(self):
        return f'Furnizorul {self.owner} are produsul {self.name} costa {self.price} si sunt disponibile ' \
               f'{self.quantity} bucati!'

    def get_owner(self):
        LogFile.log_message(f"Product {self.get_owner.__name__} called!", "debug")
        return self.owner

    def get_name(self):
        LogFile.log_message(f"Product {self.get_name.__name__} called!", "debug")
        return self.name

    def get_price(self):
        LogFile.log_message(f"Product {self.get_price.__name__} called!", "debug")
        return self.price

    def get_quantity(self):
        LogFile.log_message(f"Product {self.get_quantity.__name__} called!", "debug")
        return self.quantity

    def set_owner(self, new_owner):
        LogFile.log_message(f"Product {self.set_owner.__name__} called! with {locals()}", "debug")
        self.owner = new_owner

    def set_name(self, new_name):
        LogFile.log_message(f"Product {self.set_name.__name__} called! with {locals()}", "debug")
        self.name = new_name

    def set_price(self, new_price):
        LogFile.log_message(f"Product {self.set_price.__name__} called! with {locals()}", "debug")
        self.price = new_price

    def set_quantity(self, new_quantity):
        LogFile.log_message(f"Product {self.set_quantity.__name__} called! with {locals()}", "debug")
        self.quantity = new_quantity
