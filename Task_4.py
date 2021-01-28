"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1

Two — 2

Three — 3

Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

# Create file "file_task_4.txt" (no program)

rus_num = {'One': 'Один',  # можно было и в одну строчку, но так читать мне кажется удобнее
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'
           }

# print(rus_num['One'])
with open('file_task_4.txt', 'r', encoding='utf-8') as f:
    my_list = []
    a = f.read().replace('\n\n', ',').split(',')
    for i in a:
        word, number = (i.split(' — '))
        my_list.append(f'{rus_num[word]} - {number}\n\n')

with open('file_task_4(new).txt', 'w', encoding='utf-8') as file:
    file.writelines(my_list)
