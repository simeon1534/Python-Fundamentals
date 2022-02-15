age = float(input())
sx = input()

if sx == 'f':
    if age<16:
        print('Miss')
    else:
        print('Ms.')
else:
    if age<16:
        print('Master')
    else :
        print('Mr.')
