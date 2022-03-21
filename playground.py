# This file is used to try abstract new features


class test_structure:
    def __init__(self, __first = [1, 2, 3], __second = [4, 5, 6]):
        self._first = __first
        self._second = __second

    def __str__(self):
        return f"Obiect test_structure({self._first}, {self._second})"

    def __delitem__(self, key):
        self._first.remove(self._first[key])
        self._second.remove(self._second[key])

    def __call__(self, *args, **kwargs):
        print("Called")

    # list implementation
    def __getitem__(self, item):
        return self._first[item]

    def __setitem__(self, key, value):
        self._first[key] = value

    def __iter__(self):
        return iter(zip(self._first, self._second))

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, new_first):
        self._first = new_first

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, new_second):
        self._second = new_second


if __name__ == "__main__":
    """ # Testing getter and setter
    obj = test_structure(5, 6)
    print(obj.first)
    obj.first = 6
    print(obj.first)
    """

    """ Testing dunder getitem/setitem
    obj = test_structure(["obj1", "obj2", "obj3"], ["obj5", "obj6", "obj7"])
    print(obj[1])
    obj[1] = "test"
    print(obj[1])
    print(obj.__getitem__(1))
    """

    """ Testing iter method
    obj = test_structure(["obj1", "obj2", "obj3"], ["obj5", "obj6", "obj7"])
    for item in obj:
        print(item)
    """
    """ Test str/delitem
    obj = test_structure(["obj1", "obj2", "obj3"], ["obj5", "obj6", "obj7"])
    print(obj)
    del obj[1]
    print(obj)
    """
    """ Testint call
    obj = test_structure(["obj1", "obj2", "obj3"], ["obj5", "obj6", "obj7"])
    obj()
    """