"""
Задание 2.

Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.

Реализуйте вариант без и с генераторным выражением
"""
primary_list = [400, 5, 16, 33, 2, 2, 5, 11, 6, 3, 97, 321, 75]

# without generator
result_list_1 = []
for el in range(1, len(primary_list)):
    if primary_list[el] > primary_list[el - 1]:
        result_list_1.append(primary_list[el])

print(result_list_1)

# with generator
result_list_2 = (primary_list[el] for el in range(
    1, len(primary_list)) if primary_list[el] > primary_list[el - 1])

print(result_list_2)
