"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

# Create file "file_task_7.txt" (no program)

import json
my_dict = {}
profit = 0
i = 0
with open('file_task_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, firm, earnings, loss = line.split()
        my_dict[name] = int(earnings) - int(loss)
        i += 1
        profit += my_dict[name]
        average_profit = {'average_profit': round(profit / i)}

    print(f'{my_dict}, {average_profit}')

out_info = [my_dict, average_profit]

with open('file_task_7.json', 'w') as f_json:
    json.dump(out_info, f_json)

# with open('file_task_7.json') as f_json:
#     print(json.load(f_json))
