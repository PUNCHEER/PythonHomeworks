letters = 'Па-па-ра-ра пам-пам-парам па-рапам-па'
letters_2 = 'Пум-пурум-пум пумпум парам-пам-пам'
letters = letters.split(' ')
letters_2 = letters_2.split(' ')
def compare(objects):
    count_vouwels = lambda x: sum(map(x.count, 'аоиыеуёэюя'))
    if len(set(map(count_vouwels, objects))) == 1:
         print('Парам пам-пам')
    else:print('Пам парам')
compare(letters)
compare(letters_2)