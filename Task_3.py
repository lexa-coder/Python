"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
# Create file "file_task_3.txt" (no program)

# Create 15 string with number (no program):
#
# import random
# i = 0
# while i < 15:
#     i += 1
#     print(f'{random.uniform(1, 100000):.2f}')
salar = []
with open('file_task_3.txt', encoding='utf-8') as f:

    for i in f:
        name, sal = i.split()
        salar.append(float(sal))

        if float(sal) < 20000:
            print(f'{name} - оклад меньше 20000 (оклад составляет {sal})')

    print(f'\nCредняя величина дохода сотрудников = {sum(salar) / len(salar):.2f}')
