import math


def center_point(x1, y1, x2, y2, x3, y3, x4, y4):
    result1 = math.sqrt(math.pow(y1, 2) + math.pow(x1, 2))
    result2 = math.sqrt(math.pow(y2, 2) + math.pow(x2, 2))

    result3 = math.sqrt(math.pow(y3, 2) + math.pow(x3, 2))
    result4 = math.sqrt(math.pow(y4, 2) + math.pow(x4, 2))



    result_first = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    result_second = math.sqrt((x4 - x3) * (x4 - x3) + (y4 - y3) * (y4 - y3))

    if result_first > result_second:
        if result1 > result2:
            return f'({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})'
        elif result1 < result2:
            return f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})'

    elif result_first < result_second:
        if result3 > result4:
            return f'({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})'
        elif result3 < result4:
            return f'({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})'



first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
third_x = float(input())
third_y = float(input())
fourth_x = float(input())
fourth_y = float(input())

print(center_point(first_x, first_y, second_x, second_y, third_x, third_y, fourth_x, fourth_y))
