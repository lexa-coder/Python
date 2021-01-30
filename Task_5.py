"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('file_task_5.txt', 'w', encoding='utf-8') as f:
    file_num = (input('Введите набо чисел, разделённых пробелами: '))
    f.writelines(file_num)

with open('file_task_5.txt', encoding='utf-8') as f:
    for i in f:
        num = i.split()
    print(f'Сумма введёных чисел в файле равна: {sum(map(int, num))}')
