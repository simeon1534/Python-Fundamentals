def factoriel_function(x):
    if x < 2:  # result=1
        return 1  # for num in range(2,x+1 )
    else:  # result*=num
        result_x = x * factoriel_function(x - 1)  # return result
        return result_x


result_x = 0
first = int(input())
second = int(input())
print(f'{factoriel_function(first)/factoriel_function(second):.2f}')
