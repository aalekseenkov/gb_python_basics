"""
Задание 1.

Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).
"""


def div(p_num_1, p_num_2):
    """pass docstring"""
    try:
        return p_num_1 / p_num_2
    except ZeroDivisionError:
        return "Trying to divide by zero!"


try:
    num_1 = int(input("Enter your 1st digit: "))
    num_2 = int(input("Enter your 2nd digit: "))
    print(div(num_1, num_2))
except ValueError:
    print("Please, enter only digits not strings and others")
