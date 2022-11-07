"""
Задание 5.

Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""
STR_OBJ = "1 2 3 4 5"
RES = 0

with open("output.txt", "w", encoding='utf-8') as f_obj:
    f_obj.write(STR_OBJ)

with open("output.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.read().split(" ")
    for n in content:
        RES = RES + int(n)
    print(f"Sum of numbers = {RES}")
