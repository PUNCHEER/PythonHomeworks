import os


def add_number():
    name = input('Введите имя:')
    surname = input('Введите фамилию:')
    number = input('Введите номер телефона:')
    comment = input('Введите комментарий:')
    contact = [name, '|', surname, '|', number, '|', comment, '|']
    with open('handbook_txt.txt', 'a') as f:
        print(*contact, file=f)
    print('Успешно добавлен')
    look_handbook()


def menu():
    print('Меню справончника\n'
          'Выберите пункт:\n1. Создать контакт\n2. Найти контакт\n3. Просмотреть контакты\n')
    select = int(input('Введите число:'))
    if select == 1:
        add_number()
    elif select == 2:
        find_contact()
    elif select == 3:
        look_handbook()
    else:
        return print('Неверный пункт'), menu()


def look_handbook():
    with open('handbook_txt.txt', 'r') as file:
        print(*file)
        menu()


def find_contact():
    i = 0
    while True:
        find_surname = input('Введите фамилию')
        find_surname.upper()
        remind = list()
        with open('handbook_txt.txt', 'r') as file:
            for line in file:
                line.upper()
                if line.find(find_surname) != -1:
                    print(f'{i + 1}.{line}')
                    i += 1
                    remind.append(line.rstrip('\n'))
        if len(remind) >= 1:
            break
        if len(remind) < 1:
            print('Такого контакта не существует!')
    select = int(input('Выберите запись для редактирования:'))
    print(remind[select - 1].rstrip('\n'))
    print('Что хотите сделать с контактом:\n1.Удалить контакт\n2.Изменить контакт\n3.Отмена')
    while True:
        action = int(input('Выберите действие:'))
        if action == 1:
            delete(remind[select - 1])
            break
        elif action == 2:
            rename(remind[select - 1])
            break
        elif action == 3:
            menu()
        else:
            print('Неверное действие')


def delete(contact):
    found = False
    search = contact
    choose = int(input('Вы действительно хотите удалить контакт?\n1.Да\n2.Нет'))
    if choose == 1:
        names = open('handbook_txt.txt', 'r')
        temp_file = open('test.txt', 'w')
        descr = names.readline()
        while descr != '':
            descr = descr.rstrip('\n')
            if descr != search:
                temp_file.write(descr + '\n')
            else:
                found = True
            descr = names.readline()
        names.close()
        temp_file.close()
        os.remove('handbook_txt.txt')
        os.rename('test.txt', 'handbook_txt.txt')
        if found:
            print('Успешно удалено!')
            menu()
            print(' ')
        else:
            print('Что-то не так!')
    else:
        menu()


def rename(contact):
    choice_2 = 0
    found = False
    while choice_2 != 2:
        search = contact
        choice = int(input(f'Что хотите изменить:\n1.Фамилия\n2.Имя\n3.Телефон\n4.Комментарий'))
        if choice <= 4:
            new_characteristic = input('Введите изменения:')
            name = search.split(' | ')
            name[choice - 1] = new_characteristic

        else:
            print('Неверный выбор')
        chracteristic = ' | '.join(name)
        print(chracteristic)
        contact = chracteristic
        names = open('handbook_txt.txt', 'r')
        temp_file = open('test.txt', 'w')
        descr = names.readline()
        while descr != '':
            descr = descr.rstrip('\n')
            if descr == search:
                temp_file.write(chracteristic + '\n')
                found = True
            elif descr != search:
                temp_file.write(descr + '\n')
            descr = names.readline()
        names.close()
        temp_file.close()
        os.remove('handbook_txt.txt')
        os.rename('test.txt', 'handbook_txt.txt')
        if found:
            choice_2 = int(input('Успешно изменили!\nЖелаете изменить что-то еще?\n1.Да\n2.Нет'))
            if choice_2 == 2:
                print('Переходим в главное меню!')
                menu()
                print()
        else:
            print('Что-то не так!')


menu()
