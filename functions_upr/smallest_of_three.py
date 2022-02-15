def smallest_num(a, b, c):
    min_num = 0
    if a > c and b > c:
        min_num = c
        return min_num
    elif a > b and c > b:
        min_num = b
        return min_num
    if c > a and b > a:
        min_num = a
        return min_num


x = int(input())
y = int(input())
z = int(input())

print(smallest_num(x, y, z))
