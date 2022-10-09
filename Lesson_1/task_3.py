"""
Задание 3.

Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn.
"""
n = int(input("Enter integer number n: "))
result = n + n**2 + n**3
print(f"n + nn + nnn = {result}")

