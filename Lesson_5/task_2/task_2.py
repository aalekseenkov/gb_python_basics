"""
Задание 2.

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
COUNT_LINES = 0
COUNT_WORDS = 1

with open("input.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                COUNT_WORDS += 1
        COUNT_LINES += 1
        print(f"Number of words in the line {COUNT_LINES} is {COUNT_WORDS} \n")
        COUNT_WORDS = 1
    print(f"This file has got {COUNT_LINES} line(s)")
