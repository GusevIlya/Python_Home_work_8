"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.

"""

from os.path import exists
from os import remove, rename


def get_info():
    info = []
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    info.append(first_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неверное количество цифр')
            else:
                flag = True
        except ValueError:
            print('Некорректный номер')
        info.append(phone_number)
        return info


def create_file():
    with open('phone.txt', 'w', encoding='utf-8') as data:
        data.write('Фамилия; Имя; Телефон\n')


def write_file(lst):
    with open('phone.txt', 'a', encoding='utf-8') as data:
        data.write(f'{lst[0]} {lst[1]} {lst[2]}\n')


def read_file():
    with open('phone.txt', encoding='utf-8') as data:
        phone_book = data.readlines()
        return phone_book


def record_info():
    lst = get_info()
    write_file(lst)


def search():
    flag = False
    with open('phone.txt', encoding='utf-8') as data:
        phone_book = data.readlines()
        word = input('Кого ищем? > ')
        for line in phone_book:
            if word in line:
                print(line)
                flag = True
    return flag


def delete():
    with open('phone.txt', encoding='utf-8') as old_data, open('new_phone.txt', 'w', encoding='utf-8') as new_data:
        old_phone_book = old_data.readlines()
        word = input('Чья запись будет удалена? > ')
        for line in old_phone_book:
            if word not in line:
                new_data.write(line)
    remove('phone.txt')
    rename('new_phone.txt', 'phone.txt')


def change():
    with open('phone.txt', encoding='utf-8') as old_data, open('new_phone.txt', 'w', encoding='utf-8') as new_data:
        old_phone_book = old_data.readlines()
        word = input('Чья запись будет изменена? > ')
        for line in old_phone_book:
            if word not in line:
                new_data.write(line)
    remove('phone.txt')
    rename('new_phone.txt', 'phone.txt')


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.txt'):
                print('Файл не создан. Для создания введите команду "w"')
                break
            print(*read_file())
        elif command == 'w':
            if not exists('phone.txt'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'c':
            if search():
                change()
                record_info()
            else:
                print('Запись не найдена')
        elif command == 's':
            if search():
                continue
            else:
                print('Запись не найдена')
        elif command == 'd':
            if search():
                delete()
            else:
                print('Запись не найдена')


main()
