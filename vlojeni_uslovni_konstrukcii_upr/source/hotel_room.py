season = input()
nights = int(input())

studio = 0
apartment = 0
# cena=0
if season == 'May' or season == 'October':
    studio = 50 * nights
    apartment = 65 * nights
    if 14>nights > 7:
        studio -= 0.05 * studio
    elif nights > 14:
        studio -= 0.30 * studio
elif season == 'June' or season == 'September':
    studio = 75.20 * nights
    apartment = 68.70 * nights
    if nights > 14:
        studio -= 0.20 * studio
elif season == 'July' or season == 'August':
    studio = 76 * nights
    apartment = 77 * nights
if nights>14:
    apartment-=0.1*apartment
print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')

