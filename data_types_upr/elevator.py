import math
n = int(input())
p = int(input())
courses = n / p
if p >= n:
    print(1)
else:
    print(math.ceil(courses))