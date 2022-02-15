import sys

n = int(input())

sum_even = 0
sum_odd = 0
max_odd = -sys.maxsize
min_odd = sys.maxsize
max_even = -sys.maxsize
min_even = sys.maxsize
i = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even = float(input())
        sum_even += even
        if even > max_even:
            max_even = even
            if min_even==sys.maxsize:
                min_even=max_even
            #if min_even>even > max_even and i<3:
              #  min_even=max_even

        elif even < min_even:
            min_even = even
            #if i<3:
               # min_even=max_even

    else:
        odd = float(input())
        sum_odd += odd
        if odd > max_odd:
            max_odd = odd
            if min_odd==sys.maxsize:
                min_odd=max_odd
           # if min_odd>odd > max_odd:
            #    min_odd=max_odd
        elif odd < min_odd:
            min_odd = odd
           # if i<3:
               # min_odd=max_odd
#if i == 1:
 #   min_odd = max_odd
#elif i == 2:
 #   min_odd = max_odd
 #   min_even = max_even
#elif i == 3:
 #   min_even = max_even

print(f'OddSum={sum_odd:.2f},')
if min_odd == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={min_odd:.2f},')
if max_odd==-sys.maxsize:
    print(f'OddMax=No,')
else:

    print(f'OddMax={max_odd:.2f},')

print(f'EvenSum={sum_even:.2f},')
if min_even == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={min_even:.2f},')
if max_even==-sys.maxsize:
    print(f'EvenMax=No')
else:

    print(f'EvenMax={max_even:.2f}')
