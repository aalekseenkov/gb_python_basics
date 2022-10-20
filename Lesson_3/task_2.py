"""
Задание 2.

Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон.

Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user(name, surname, birth_year, city, email, phone):
    """pass docstring"""

    print(f'{name} {surname} was born in {birth_year} and lives in {city}. '
          f'E-mail: {email}, phone: {phone}.')


user(
    name="Andrew",
    surname="Alekseenkov",
    birth_year="1971",
    city="Homel",
    email="admin@site.ru",
    phone="+375291234567")
