"""
Задание 5.

Продолжить работу над четвертым заданием.

Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.

Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""


class StorageError(Exception):
    """ Class StorageError Docstring """

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    """ Class AddStorageError Docstring """

    def __init__(self, text):
        self.text = "It's not possible to add an item "\
                    f"to the warehouse:\n {text}"


class TransferStorageError(StorageError):
    """ Class TransferStorageError Docstring """

    def __init__(self, text):
        self.text = f"Hardware transfer error:\n {text}"


class Storage:
    """ Class Storage Docstring """

    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        """ add docstring """
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} is not office equipment")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        """ transfer docstring """
        if not isinstance(idx, int):
            raise TransferStorageError(f"Invalid type '{type(idx)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(
                f"Equipment {item} is already assigned "
                "to the department {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        """ filter_by docstring """
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"Devices in stock now - {len(self.__storage)}"


class OfficeEquipment:
    """ Class OfficeEquipment Docstring """

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    """ Class Printer Docstring """

    def __init__(self, *args):
        super().__init__('Printer', *args)


class Scanner(OfficeEquipment):
    """ Class Scanner Docstring """

    def __init__(self, *args):
        super().__init__('Scanner', *args)


class Xerox(OfficeEquipment):
    """ Class Xerox Docstring """

    def __init__(self, *args):
        super().__init__('Xerox', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("Epson", "XP-400"))
    storage.add(Scanner("OKI", "5367-AD"))
    storage.add(Xerox("Xerox", "F123"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("We transfer 1 device")
    storage.transfer(last_idx, 'JF Department')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Deleting 1 device")
    del storage[last_idx]
    print(storage)
