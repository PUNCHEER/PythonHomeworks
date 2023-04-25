first_num = int(input('Введите число:'))
second_num = int(input('Введите второе число:'))
def summ(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summ(a, b)
    else: return a
print(summ(first_num, second_num))