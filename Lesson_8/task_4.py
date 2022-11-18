"""
Задание 4.

Начните работу над проектом «Склад оргтехники».

Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого
типа оргтехники.
"""


class Storage:
    """ Class Storage Docstring """
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        """ retail_price docstring """
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        """ wholesale_price docstring """
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    """ Class Printer Docstring """
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Printer', *args)


class Scanner(OfficeEquipment):
    """ Class Scanner Docstring """
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('Scanner', *args)


class Xerox(OfficeEquipment):
    """ Class Xerox Docstring """
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('Xerox', *args)


if __name__ == '__main__':
    p1 = Printer("HP", "LaserJet 6L", "White", 4010)
    print(p1)
