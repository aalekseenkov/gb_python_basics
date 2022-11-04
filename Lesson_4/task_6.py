"""
Задание 6.

Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

# 1. The iterator that generates integers starting from the specified

list_int = []

first_number = int(input("Specify the first number of your sequence >>> "))
last_number = int(input("Specify the last number of your sequence >>> "))

print()

for x in count(first_number):
    if x > last_number:
        break
    print(x)
    list_int.append(x)

print()
print(list_int)
print()

# 2. The iterator that repeats the elements of some list defined in advance

COUNT = 0
for item in cycle(list_int):
    if COUNT >= len(list_int):
        break
    print(item)
    COUNT += 1
