"""
Задание 2.

Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
elements = input("Enter integers separated by a space: ").split()
print(f'Input:  {elements}')
for el in range(0, len(elements) - 1, 2):
    tmp = elements[el]
    elements[el] = elements[el + 1]
    elements[el + 1] = tmp
print(f'Output: {elements}')
