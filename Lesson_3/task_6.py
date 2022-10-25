"""
Задание 6.

Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(string):
    """int_func docsting"""
    return string.title()


def title_func(string):
    """title_func docsting"""
    list_title = []
    lst = string.split()
    for value in lst:
        list_title.append(int_func(value))
    print(*list_title)


print(int_func("text"))
title_func("every word will now be capitalized")
