"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение. В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""
from math import floor
from typing import List, Tuple, Union


class Number(int):
    """ Number Class Docstring """

    def __str__(self):
        return f"{self:02}"


class Date:
    """ Date Class Docstring """
    day_month_year = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        fragments = date.split('-')

        if not self.validate(*fragments):
            raise ValueError(f"{date} invalid date format")

        self.day, self.month, self.year = self.transform(fragments)

    def __iter__(self):
        for attr in self.day_month_year:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date: Union[List[str], Tuple[str]]) -> List[Number]:
        """ Conversion to the Number type """
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date: Union[List[str], Tuple[str]]) -> bool:
        """ Date's Validation """
        try:
            day, month, year = [int(x) for x in date]
        except TypeError:
            return False

        bis_sextus = bool(not (year % 400 and year % 4) and year % 100)
        end_mon_day = 28 + (month + floor(month / 8)) % 2 + \
            2 % month + 2 * floor(1 / month)
        end_mon_day += bis_sextus if month == 2 else 0

        return all([1 <= day <= end_mon_day, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    for date in ('24-10-2001', '21-06-1941', '29-02-2016', '29-02-2017'):
        try:
            print(Date(date))
        except ValueError as e:
            print(e)
