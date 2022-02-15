import math


def center_point(x1, y1, x2, y2):
    result1 = math.sqrt(math.pow(y1, 2) + math.pow(x1, 2))
    result2 = math.sqrt(math.pow(y2, 2) + math.pow(x2, 2))
    if result1 > result2:
        return f'({math.floor(x2)}, {math.floor(y2)})'
    elif result1 < result2:
        return f'({math.floor(x1)}, {math.floor(y1)})'


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
print(center_point(first_x, first_y, second_x, second_y))
