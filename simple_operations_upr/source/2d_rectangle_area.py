x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1 - x2)
width = abs(y1 - y2)

area = length * width
print(f'{area:.2f}')

perimeter = 2 * length + 2 * width
print(f'{perimeter:.2f}')
