def perfect_number(num):
    result = 0
    end_result = ''
    for i in range(1, num ):
        if num % i == 0:
            result += i
    if result == num:
        end_result += f'We have a perfect number!\n'
    elif result != num:
        end_result += f"It's not so perfect.\n"
    return end_result


x = int(input())
print(perfect_number(x))
