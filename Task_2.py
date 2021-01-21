# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def func_person(name, surname, birth, curr_city, email, phone):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {birth}, Город проживания: {curr_city}, '
          f'Email: {email}, Телефон: {phone} ')


func_person(name='Ivan', surname='Ivanov', birth=1993, curr_city='Samara', email='alex@mail.ru', phone='+7903333')
