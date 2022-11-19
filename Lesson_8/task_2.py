"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    """ MyZeroDivisionError Class Docstring """
    text = "*** Division by zero is prohibite!!! ***"

    def __str__(self):
        return self.text


class Number(float):
    """ Number Class Docstring """

    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number,
                                    input("Enter the dividend and the divider"
                                          " separated by a space: ").split())
            print(dividend / divider)
        except MyZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
            break
