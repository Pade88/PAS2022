import unittest
from Supplier import Supplier

class TestSum(unittest.TestCase):

    @staticmethod
    def test_supplier_creation():
        NAME = "NUME"
        TAX_ID = "123456789"
        PRODUCT_LIST = [{"A": 30, "X": "string"}, {"B": 50, "Y": 22.1515}, {"C": 60, "Z": 1}]
        ADDRESS = "ADDRESS"
        IN_CHARGE = "IN_CHARGE"
        PHONE = "123456789"

        test_supplier = Supplier(NAME, TAX_ID, PRODUCT_LIST, ADDRESS, IN_CHARGE, PHONE)

        assert isinstance(test_supplier, Supplier)
        assert test_supplier.name == NAME
        assert test_supplier.name != "NAME"
        assert test_supplier.tax_identification == TAX_ID

        assert len(test_supplier.product_list) == 3
        assert "A" in test_supplier.product_list[0]
        assert "string" in test_supplier.product_list[0].values()
        assert test_supplier.product_list[1]["B"] == 50
        assert all(key in test_supplier.product_list[2].keys() for key in ["C", "Z"])
        assert not all(key in test_supplier.product_list[2].keys() for key in ["C", "WWW"])

        assert test_supplier.address != "SOME_RANDOM_ADDRESS"
        assert isinstance(test_supplier.phone, str)

if __name__ == '__main__':
    unittest.main()