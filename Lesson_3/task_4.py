"""
Задание 4.

Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень!

ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(int_x, int_y):
    """my_func docstring"""
    try:
        if int_y < 0:
            result = 1
            for _ in range(int_y, 0):
                result = result * int_x
            result = 1 / result
            return f'For values x = {int_x}, y = {int_y} result: {result}'
        return "The number y must be strictly negative"
    except TypeError:
        return "Please enter only numbers"
    except ZeroDivisionError:
        return "You can't divide by zero"


print(my_func(5, -3))
