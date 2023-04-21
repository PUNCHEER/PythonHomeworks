import array as arr
import random
def fill_array(length):
    number = arr.array('i', [0] * lenght_array)
    for i in range(len(number)):
        number[i] = random.randint(0, 30)
    return number
def Searching(array):
    around_num = max_num
    count_summa = abs(max_num - num_count)
    for i in range(len(array)):
        summa = abs(num_count - array[i])
        if summa < count_summa:
            around_num = array[i]
            count_summa = summa
    return around_num
lenght_array = int(input('Введите длину массива:'))
numbers = fill_array(lenght_array)
num_count = int(input('Введите число:'))
max_num = max(numbers)
print(*numbers)
print(f'Ближайшее число или равное заданному числу - {num_count}, будет - {Searching(numbers)}')