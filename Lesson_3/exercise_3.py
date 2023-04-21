letters = [('AEIOULNSTRАВЕИНОРСТ', 1),
          ('DGДКЛМПУ', 2),
          ('BCMPБГЁЬЯ', 3),
          ('FHVWYЙЫ', 4),
          ('KЗЖЗХЦЧ', 5),
          ('JXШЭЮ', 8),
          ('QZФЩЪ', 10)]
scrable = dict()
for i in letters:
    for j in i[0]:
        scrable[j] = i[1]

word = input('Введите слово:')
def Point(scrable, word):
    word = word.upper()
    summa = 0
    for i in word:
        summa += scrable[i]
    return summa
print(f'Ваше количество очков - {Point(scrable, word)}')
