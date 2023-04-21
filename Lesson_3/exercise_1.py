import array as arr
import random

lenght_array = int(input('Введите длину массива:'))
fillnum = int(input('Введите число:'))
count = 0
number = arr.array('i', [0]*lenght_array)
for i in range(len(number)):
    number[i] = random.randint(0, 10)
    if number[i] == fillnum:
        count += 1
print(*number)
print(f'Число - {fillnum} повторялось - {count} раз')
