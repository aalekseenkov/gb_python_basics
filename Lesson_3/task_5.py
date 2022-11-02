"""
Задание 5.

Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
после этого завершить программу.
"""
import sys


def get_str_for_sum(my_sum=0):
    """get_str_for_sum() docstring"""
    lst = input("Enter the numbers separated by a space:").split()
    # for element in range(len(lst)):
    for _, value in enumerate(lst):
        if value != "Q":
            my_sum = my_sum + int(value)
        else:
            break
    print(my_sum)
    if "Q" in lst:
        sys.exit("Exit from the program")
    else:
        get_str_for_sum(my_sum)


get_str_for_sum()
