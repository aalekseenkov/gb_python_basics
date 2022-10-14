"""
Задание 3.

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
"""
months_list = [
    'Winter', 'Winter', 'Spring',
    'Spring', 'Spring', 'Summer',
    'Summer', 'Summer', 'Autumn',
    'Autumn',  'Autumn', 'Winter'
] 

months_dict = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

months_num = int(input("Enter one month's number: "))

if 0 < months_num < 13:
    print(f'Result over the list: {months_list[months_num - 1]}')
    print(f'Result over the dictinary: {months_dict[months_num]}')
else:
    print("You have entered the wrong month's number")
