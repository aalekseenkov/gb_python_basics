"""
Задание 7.

Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать. Далее реализовать список. Он должен содержать
словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

profit = {}
firms_profit = {}
data = [firms_profit, profit]
SUM_MARGIN = 0
COUNT_FIRM_AVG = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, form, salary, cost = line.split()
        margin = float(salary) - float(cost)
        if margin > 0:
            COUNT_FIRM_AVG = COUNT_FIRM_AVG + 1
            SUM_MARGIN = SUM_MARGIN + margin
            firms_profit[name] = margin
        else:
            firms_profit[name] = margin
if COUNT_FIRM_AVG > 0:
    profit["average_profit"] = SUM_MARGIN / COUNT_FIRM_AVG

with open("output.json", "w", encoding="utf-8") as write_f:
    json.dump(data, write_f)
print(f"{firms_profit} {profit}")
