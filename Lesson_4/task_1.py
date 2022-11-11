"""
Задание 1.

Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys
f_obj, name_v, rate_v, hours_v = sys.argv[0:4]
print(f_obj)


def calculate_salary(rate, hours):
    """calculate_salary() docstring"""
    try:
        print(
            f"The employee {name_v} earned {int(rate) * int(hours) * 1.25}")
    except TypeError:
        print("Operation was applied to an object of an inappropriate type")
        sys.exit()


calculate_salary(rate_v, hours_v)
