import sys


grad=input()
if grad != 'Burgas''Varna''Bansko''Borovets':
    print('Invalid number!')
    sys(exit)
vid_paket=input()
vip=input()  # yes or no
dni_prestoi=int(input())


if dni_prestoi<1:
    print('Days must be positive number!')
    sys.exit()


if dni_prestoi>7:
    dni_prestoi-=1

cost_per_day=0
if grad=='Borovets ' or grad=='Bansko ':
    if vid_paket=='noEquipment ':
        cost_per_day=80
        if vip == 'yes ':
            cost_per_day-=5/100* cost_per_day
        print(f'The price is {dni_prestoi * cost_per_day:.2f}lv! Have a nice time!')
    elif vid_paket=='withEquipment ':
        cost_per_day = 100
        if vip=='yes ':
            cost_per_day -= 10 / 100 * cost_per_day
        print(f'The price is {dni_prestoi*cost_per_day:.2f}lv! Have a nice time!')
    else:
        print('Invalid number!')
elif grad == 'Burgas ' or grad == 'Varna ':
    if vid_paket == 'noBreakfast ':
        cost_per_day = 100
        if vip == 'yes ':
            cost_per_day -= 7 / 100 * cost_per_day
        print(f'The price is {dni_prestoi * cost_per_day:.2f}lv! Have a nice time!')
    elif vid_paket == 'withBreakfast ':
        cost_per_day = 130
        if vip == 'yes ':
            cost_per_day -= 12 / 100 * cost_per_day
        print(f'The price is {dni_prestoi * cost_per_day:.2f}lv! Have a nice time!')
    else:
        print('Invalid number!')


