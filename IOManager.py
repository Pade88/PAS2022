import json


class IOManager:
    def __init__(self):
        pass

    @staticmethod
    def load_json(file_name):
        with open(file_name, "r") as input_file:
            data = json.load(input_file)
        return data

    # used to extend
    @staticmethod
    def expand_json(file_name, *new_value):
        with open(file_name, "r") as input_file:
            data = json.load(input_file)

        if file_name == "suppliers_db.json":
            data["Suppliers"].append(new_value[0])

            with open(file_name, "w+") as output_file:
                json.dump(data, output_file, indent=2)
        else:
            for cnt, item in enumerate(data["Companies"]):
                if new_value[0] == item["name"]:
                    supl_list = item["suppliers"].replace(" ", "").split(",")
                    supl_list.append(new_value[1])
                    supl_list = ", ".join(supl_list)
                    new_dict = {"name": new_value[0], "suppliers": supl_list}
                    data["Companies"][cnt] = new_dict
            with open(file_name, "w+") as output_file:
                json.dump(data, output_file, indent=2)

    @staticmethod
    def shrink_json(file_name, value):
        with open(file_name, "r") as input_file:
            data = json.load(input_file)
        if file_name == "suppliers_db.json":
            for lcl_idx in data["Suppliers"]:
                if lcl_idx["name"] == value:
                    successful_op = True
                    data["Suppliers"].remove(lcl_idx)
        else:
            # log data
            for lcl_idx in data["Companies"]:
                if lcl_idx["name"] == value:
                    successful_op = True
                    data["Companies"].remove(lcl_idx)

            # log data
        if successful_op:
            with open(file_name, "w+") as output_file:
                json.dump(data, output_file, indent=2)
            return True
        return False

    @staticmethod
    def update_product_list(file_name, args):
        owner, name, price, quantity = args
        product = {"name": name, "price": price, "quantity": quantity}
        with open(file_name, "r") as input_file:
            data = json.load(input_file)

        for supplier in data["Suppliers"]:
            if supplier["name"] == owner:
                supplier["product_list"].append(product)

        with open(file_name, "w+") as output_file:
            json.dump(data, output_file, indent=2)
