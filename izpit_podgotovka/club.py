wanted_money = float(input())
stop = False
total_cocktail_1=0
total_cocktail=0

while wanted_money >total_cocktail:
    cocktail = input()
    if cocktail == 'Party!':
        stop = True
        break

    cena_cocktail = len(cocktail)
    cocktail_count = int(input())
    total_cocktail_1=cena_cocktail * cocktail_count

    if total_cocktail_1 % 2 != 0:
            total_cocktail_1=(cena_cocktail * cocktail_count)-25/100*cena_cocktail * cocktail_count
    total_cocktail += total_cocktail_1
if wanted_money <total_cocktail:
    print('Target acquired.')
    print(f'Club income - {total_cocktail:.2f} leva.')
else:
    print(f'We need {wanted_money - total_cocktail:.2f} leva more.')
    print(f'Club income - {total_cocktail:.2f} leva.')
