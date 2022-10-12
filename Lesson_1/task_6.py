"""
Задание 6.

Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчёте на одного сотрудника.
"""
gain = int(input("Enter gain of your company: "))
cost = int(input("Enter cost of your company: "))
if gain > cost:
    profit = gain - cost
    print(f"The financial result is PROFIT! The value of {profit}...")
    profitability = profit / gain
    print(f"The profitability of your company is {profitability}.")
    employees = int(input("Enter your employees' number: "))
    profit_for_person = profit / employees
    print(f"The company's profit per employee is {profit_for_person}.")
elif gain < cost:
    loss = cost - gain
    print(f"The financial result is LOSS! The value of {loss}...")
else:
    print(f"The financial result is NO PROFIT/NO LOSS!")
