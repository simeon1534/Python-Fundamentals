city = input()
prodajbi = float(input())

if city == 'Sofia':
    if 0 <= prodajbi <= 500:
        com = prodajbi * 0.05
        print(f'{com:.2f}')
    elif 500 <= prodajbi <= 1000:
        com = prodajbi * 0.07
        print(f'{com:.2f}')
    elif 1000 <= prodajbi <= 10000:
        com = prodajbi * 0.08
        print(f'{com:.2f}')
    elif prodajbi > 10000:
        com = prodajbi * 0.12
        print(f'{com:.2f}')
    else:
        print('error')
elif city == 'Varna':
    if 0 <= prodajbi <= 500:
        com = prodajbi * 0.045
        print(f'{com:.2f}')
    elif 500 <= prodajbi <= 1000:
        com = prodajbi * 0.075
        print(f'{com:.2f}')
    elif 1000 <= prodajbi <= 10000:
        com = prodajbi * 0.10
        print(f'{com:.2f}')
    elif prodajbi > 10000:
        com = prodajbi * 0.13
        print(f'{com:.2f}')
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= prodajbi <= 500:
        com = prodajbi * 0.055
        print(f'{com:.2f}')
    elif 500 <= prodajbi <= 1000:
        com = prodajbi * 0.08
        print(f'{com:.2f}')
    elif 1000 <= prodajbi <= 10000:
        com = prodajbi * 0.12
        print(f'{com:.2f}')
    elif prodajbi > 10000:
        com = prodajbi * 0.145
        print(f'{com:.2f}')
    else:
        print('error')
else:
    print('error')
