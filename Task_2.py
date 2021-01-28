"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# Create file "file_task_2.txt" (no program)
# Create some string and words (no program)


with open('file_task_2.txt', 'r', encoding='utf-8') as f:  # x
    #   f.seek(0)
    for count, string in enumerate(f):
        if len(string.split()) == 1:
            print(f'В {count + 1} строке {len(string.split())} слово')
        elif 1 < len(string.split()) <= 4:
            print(f'В {count + 1} строке {len(string.split())} слова')
        else:
            print(f'В {count + 1} строке {len(string.split())} слов')
