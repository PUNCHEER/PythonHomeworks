first_num = int(input('Введите число:'))
second_num = int(input('Введите в какую степень возвести:'))
def degree(a, b):
    if b == 0:
        return 1
    else: return a * degree(a, b - 1)
print(degree(first_num, second_num))