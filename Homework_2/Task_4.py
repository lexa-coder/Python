# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Введите несколько слов, разделённых пробелами: ')

words = string.split()
words_len = len(words)

for i in range(words_len):

    if len(words[i]) >= 10:
        print(i+1, words[i][:10])
    else:
        print(i+1, words[i])