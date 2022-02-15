string = input()
first_num = int(input())
second_num = int(input())


def calc(operator, a, b):
    if operator == 'multiply':
        result = a * b
        return result
    elif operator == 'divide':
        result = a // b
        return result
    elif operator == 'add':
        result = a + b
        return result
    elif operator == 'subtract' :
        result = a - b
        return result

print(calc(string,first_num,second_num))