"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток —
издержки больше выручки. Выведите соответствующее сообщение.
"""
gain = int(input("Enter gain of your company: "))
cost = int(input("Enter cost of your company: "))
if gain > cost:
    print("The financial result is PROFIT!")
else:
    print("The financial result is LOSS!")
