main_menu = '''\nГлавное меню:
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Добавить контакт
        5. Найти контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход\n'''
input_choice = 'Выберите пункт меню: '

load_successfull = 'Телефонная книга успешно открыта!'

save_successfull = 'Телефонная книга успешно сохранена!'

def change_successfull(name: str) -> str:
    return f'Контакт "{name}" успешно изменен'
pb_empty = 'Телефонная книга пуста или не загружена!'

input_new_contact = 'Введите данные нового контакта:'

new_contact = {'name': 'Введите имя: ',
               'phone': 'Введите номер телефона: ',
               'comment': 'Введите комментарий: '}

def new_contact_succesfull(name: str):
    return f'Контакт {name} успешно добавлен'

input_search = 'Что будем искать: '
def empty_search(word: str) -> str:
    return f'Контакты содержащи слово "{word}" не найдены'

input_change = 'Какой контакт будем менять: '

input_index = 'Введите индекс контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтобы не менять:'

def delete_successfull(name: str) -> str:
    return f'Контакт "{name}" успешно удален'

input_delete_contact = 'Введите какой контакт хотите удалить: '



