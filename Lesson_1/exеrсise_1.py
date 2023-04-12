from random import randint as rd
a = rd(100,999)
print(a)
sum = a //100 + ((a // 10) % 10) + ((a % 100) % 10)
print(sum)