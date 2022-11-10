"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""
from dataclasses import dataclass


@dataclass
class Worker:
    """ Worker Class docstring"""

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        """
        :param name: workers's name
        :param surname: worker's surname
        :param position: worker's position
        :param wage: worker's wage
        :param bonus: worker's bonus
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """ Position Class docstring """

    def get_full_name(self, reverse=False):
        """ Collects the full name for the position in the order specified by reverse
        :param reverse: sequence order if False (default) 'name surname'
         если True, то 'surname name'
        :return: full name
        """
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        """ Calculates the total income (salary + bonus)
        :return: The amount of salary and bonus
        """
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Andrew',
            'surname': 'Alekseenkov',
            'position': 'SAP DevOps',
            'wage':  7000,
            'bonus': 2500
        },
        {
            'name': 'Ulad',
            'surname': 'Harelikau',
            'position': 'SAP ABAP Boss',
            'wage':  9000,
            'bonus': 3000
        },
    ]

    for item in position_data:
        person = Position(**item)

        print('#######################################')
        print(f'From data: {item}')
        print(f'Person name: {person.name}')
        print(f'Person surname: {person.surname}')
        print(f'Person full name: {person.get_full_name()}')
        print(
            f'Person full name reverse: {person.get_full_name(reverse=True)}')
        print(f'Person persontion: {person.position}')
        print(f'Person total income: {person.get_total_income()}')
        print('#######################################\n\n')
