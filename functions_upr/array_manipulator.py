import sys


def array_manipulator(string_nums):
    string_nums = string_nums.split(' ')
    result = ''
    #command = input().split(' ')
    loop = True
    while loop == True:
        command = input().split(' ')
        if command[0] == 'exchange':  # exchange command
            if int(command[1]) >= len(string_nums):
                result += 'Invalid index\n'
            else:
                for i in range(int(command[1]) + 1):
                    # Първо append-вам елементите до който индекс трябва после с команда pop махам първоначалните
                    string_nums.append(string_nums[i])
                for p in range(int(command[1]) + 1):
                    string_nums.remove(string_nums[0])
        elif command[0] == 'max':
            if command[1] == 'odd':

                max_odd = 0
                max_odd_index = 'No matches'
                for j in string_nums:  # Oбхождам листа ако индекса му е нечетно число ги прибавям към друг лист от които вземам най-голямото нечетно

                   if int(j) % 2 != 0 and int(j) >= max_odd:
                        max_odd = int(j)
                        max_odd_index = string_nums.index(f"{j}")


                result += f'{max_odd_index}\n'
            elif command[1] == 'even':

                max_even = 0
                max_even_index = 'No matches'
                for j in string_nums:

                    if int(j) % 2 == 0 and int(j) >= max_even:
                        max_even = int(j)
                        max_even_index = string_nums.index(f"{j}")

                result += f'{max_even_index}\n'

        elif command[0] == 'min':
            if command[1] == 'odd':
                min_odd = 1000
                min_odd_index = 'No matches'
                for j in string_nums:
                    if int(j) % 2 != 0 and int(j) <= min_odd:
                        min_odd = int(j)
                        min_odd_index = string_nums.index(f"{j}")

                result += f'{min_odd_index}\n'
            elif command[1] == 'even':

                min_even = 1000
                min_even_index = 'No matches'
                for j in string_nums:
                    if int(j) % 2 == 0 and int(j) <= min_even:
                        min_even = int(j)
                        min_even_index = string_nums.index(f"{j}")

                result += f'{min_even_index}\n'
        elif command[0] == 'first':
            if int(command[1]) > len(string_nums):
                result += 'Invalid count\n'
            else:
                if command[2] == 'odd':
                    list_odd = 0
                    list_odd = []
                    counter = int(command[1])
                    for i in string_nums:
                        if int(i) % 2 != 0:
                            list_odd.append(int(i))
                            counter -= 1
                        if counter == 0:
                            break
                    result += f'{list_odd}\n'
                elif command[2] == 'even':
                    list_even = 0
                    list_even = []
                    counter = int(command[1])
                    for i in string_nums:
                        if int(i) % 2 == 0:
                            list_even.append(int(i))
                            counter -= 1
                        if counter == 0:
                            break
                    result += f'{str(list_even)}\n'
        elif command[0] == 'last':
            if int(command[1]) > len(string_nums):
                result += 'Invalid count\n'
            else:
                if command[2] == 'odd':
                    list_odd_reverse = 0
                    list_odd_reverse = []
                    counter = len(string_nums)
                    for i in range(len(string_nums) - 1, -1, -1):
                        if int(string_nums[i]) % 2 != 0:
                            list_odd_reverse.append(int(string_nums[i]))

                        if counter == 0:
                            break
                        counter -= 1
                    result += f'{str(list_odd_reverse)}\n'
                elif command[2] == 'even':
                    list_even_reverse = 0
                    list_even_reverse = []
                    counter = len(string_nums)
                    for i in range(len(string_nums) - 1, -1, -1):
                        if int(string_nums[i]) % 2 == 0:
                            list_even_reverse.append(int(string_nums[i]))

                        if counter == 0:
                            break
                        counter -= 1
                    result += f'{str(list_even_reverse)}\n'
        if command[0] == 'end':
            break
    int_nums=f"[{(', '.join(string_nums))}]"
    return f'{result}{int_nums}'


x = input()
print(array_manipulator(x))
