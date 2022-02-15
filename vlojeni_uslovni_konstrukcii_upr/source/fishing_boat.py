budget = int(input())
season = input()
fishermen = int(input())
naem_korab = 0
if season == 'Spring':
    naem_korab = 3000
elif season == 'Summer':
    naem_korab = 4200
elif season == 'Autumn':
    naem_korab = 4200
elif season == 'Winter':
    naem_korab = 2600

if fishermen <= 6:
    naem_korab -= 0.1 * naem_korab
elif 6 < fishermen <= 11:
    naem_korab -= 0.15 * naem_korab
elif fishermen >= 12:
    naem_korab -= 0.25 * naem_korab

if fishermen % 2 == 0 and season!='Autumn':
    naem_korab-=0.05*naem_korab
if budget>=naem_korab:
    print(f'Yes! You have {(budget-naem_korab):.2f} leva left.')
else:
    print(f"Not enough money! You need {(naem_korab-budget):.2f} leva.")