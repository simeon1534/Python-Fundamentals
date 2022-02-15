from math import pi

radius = float(input())
# radius**2 * pi
area = radius * radius * pi
perimeter = 2 * pi * radius
print(f'{area:.2f}')
print(f'{perimeter:.2f}')