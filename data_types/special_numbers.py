n=int(input())
for num in range (1,n+1):
    result=0
    num_as_string=str(num)
    for chr in num_as_string:
        result+=int(chr)
    if result ==5 or result ==7 or result ==11:
        print(f'{num} -> True')
    else :
        print(f'{num} -> False')