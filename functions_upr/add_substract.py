def sum_numbers(a, b):
    result = a + b
    return result


def substract(c):
    second_rersult = -c
    return second_rersult


def add_and_subtract(a, b, c):
    end_result = sum_numbers(a, b) + substract(c)
    return end_result

x = int(input())
y = int(input())
z = int(input())

print(add_and_subtract(x, y, z))

