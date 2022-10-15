"""
Задание 5.

Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
rating_list = [7, 7, 7, 5, 3, 3, 2]
print(f'Initial: {rating_list}')

while True:
    new_el = int(input('Enter a new element: '))
    print(f'Current: {rating_list}')

    if rating_list.count(new_el) > 0:
        pos = rating_list.index(new_el) + rating_list.count(new_el)
        rating_list.insert(rating_list.index(new_el) + rating_list.count(new_el), new_el)
        print(f'End=>: {rating_list}')
    else:
        rating_list.append(new_el)
        rating_list.sort(reverse=True)
        print(f'The End: {rating_list}')

    is_continue = input('Would you like to continue? (y/n): ') 

    if is_continue == 'y':
        continue
    else:
        break
