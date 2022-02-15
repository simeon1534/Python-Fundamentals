# import sys

grad = input()
vid_paket = input()
vip = input()  # yes or no
dni_prestoi = int(input())

if dni_prestoi < 1:
    print('Days must be positive number!')
#elif grad != 'Burgas ''Borovets ''Varna ''Bansko ': #or vid_paket != 'noEquipment ''withEquipment ''noBreakfast ''withBreakfast ':

else:
    if dni_prestoi > 7:
        dni_prestoi -= 1
    if grad == 'Borovets ' or grad == 'Bansko ':
        if vid_paket == 'noEquipment ':
            cost_per_day = 80
            if vip == 'yes ':
                cost_per_day -= 5 / 100 * cost_per_day
            print(f'The price is {dni_prestoi * cost_per_day:.2f}lv! Have a nice time!')
        elif vid_paket == 'withEquipment ':
            cost_per_day = 100
            if vip == 'yes ':
                cost_per_day -= 10 / 100 * cost_per_day
            print(f'The price is {dni_prestoi * cost_per_day:.2f}lv! Have a nice time!')
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
    else:
        print('Invalid number!')