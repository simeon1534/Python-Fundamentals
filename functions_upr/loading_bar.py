def loading_bar_function(num):
    loading_bar ='['
    procenti = num // 10
    for i in range(1, procenti + 1):
        loading_bar+='%'
    tochki=10-procenti
    for p in range (1,tochki+1):
        loading_bar += '.'
    loading_bar+=']'
    if num<100:
        return f'{num}% {loading_bar}\nStill loading...'
    else:
        return f'{num}% Complete!\n{loading_bar}'

x = int(input())
print(loading_bar_function(x))

