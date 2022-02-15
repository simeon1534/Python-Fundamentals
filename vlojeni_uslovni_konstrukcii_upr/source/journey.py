budget = float(input())
season = input()
mqsto = 0
pochivka=0
if season == 'summer':
    if budget <= 100:
        budget = 0.3 * budget
        mqsto = 'Bulgaria'
        pochivka = 'Camp'
    elif budget <= 1000:
        budget = 0.4 * budget
        mqsto = 'Balkans'
        pochivka = 'Camp'
    elif budget > 1000:
        budget = 0.9 * budget
        mqsto = 'Europe'
        pochivka = 'Hotel'
if season == 'winter':
    pochivka = 'Hotel'
    if budget <= 100:
        budget = 0.7 * budget
        mqsto = 'Bulgaria'
    elif budget <= 1000:
        budget = 0.8 * budget
        mqsto = 'Balkans'
    elif budget > 1000:
        budget = 0.9 * budget
        mqsto = 'Europe'

print(f'Somewhere in {mqsto}')
print(f'{pochivka} - {budget:.2f}')