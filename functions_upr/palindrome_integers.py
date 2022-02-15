def palindrome(string_nums):
    result = ''
    string_nums = string_nums.split(', ')  # creating list
    for i in string_nums:  # every element in list
        if i == i[::-1]:
            result += f'True\n'
        else:
            result += f'False\n'
    return result


x = input()
print(palindrome(x))
