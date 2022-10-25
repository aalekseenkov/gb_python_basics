"""
Задание 3.

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_v1(*args):
    """my_func_v1() docstring"""
    print(sum(sorted(list(args), reverse=True)[:2]))


def my_func_v2(*args):
    """my_func_v2() docstring"""
    args_lst = list(args)
    i = 0
    result = 0
    while i != 2:
        max_value = max(args_lst)
        result += max_value
        args_lst.remove(max_value)
        i += 1
    print(result)


my_func_v1(22, 5, 34)
my_func_v2(22, 5, 34)
