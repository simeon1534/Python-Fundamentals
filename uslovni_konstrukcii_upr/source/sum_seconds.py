import math
racer1_sec = int(input())
racer2_sec = int(input())
racer3_sec = int(input())

total = racer1_sec + racer2_sec + racer3_sec
sum_min = math.floor(total / 60)
sum_sec = total % 60

if sum_sec<10:
  print(f'{sum_min}:0{sum_sec}')
else:
    print(f'{sum_min}:{sum_sec}')



