import random
n = random.randint(1, 10)
m = random.randint(1, 10)
list_2 = list()
set_result = set()
list_1 = list()
for i in range(n):
    i = random.randint(1, 10)
    list_1.append(i)
set_1 = set(list_1)
for i in range(m):
    i = random.randint(1, 10)
    list_2.append(i)
set_2 = set(list_2)
set_result = set_1.union(set_2)
print(*set_result)
