from random import randint as rd
while True:
      a = str(rd(100000,999999))
      print(a)
      SumFirstHalf = int(a[0]) + int(a[1]) + int(a[2])
      SumLastHalf = int(a[-3]) + int(a[-2]) + int(a[-1])
      if SumFirstHalf == SumLastHalf:
        print('yeah baby')
        break
      else: print('Looooser')