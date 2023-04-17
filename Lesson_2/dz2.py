from random import randint as rd
#Exercise2
#first_num = rd(0, 1000)
#second_num = rd(0, 1000)
#print(first_num, second_num)
#summ = first_num + second_num
#multi = first_num * second_num
#for i in range(first_num + 1):
#    for j in range(second_num + 1):
#        if i * j == multi and i + j == summ:
#            print(f'Одно из чисел = {i},второе число = {j}')
#Exercise1
#coin = rd(0, 100)
#print(coin)
#count_eagle = 0
#count_tail = 0
#for i in range(coin):
#    count = rd(0,1)
#    if count == 1:
#        count_eagle += 1
#    else:
#        count_tail += 1
#if count_eagle > count_tail:
#    print(count_tail)
#else:
#    print(count_eagle)
#Exercise3
N = rd(0,15)
print(N)
i = 1
while 2 ** i < N:
    print(2 ** i)
    i += 1