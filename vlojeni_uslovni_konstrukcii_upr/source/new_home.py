flowers_kind = input()
flowers_count = int(input())
budget = int(input())
flowers_price=0
if flowers_kind == 'Roses':
    flowers_price = 5
elif flowers_kind == 'Dahlias':
    flowers_price = 3.80
elif flowers_kind == 'Tulips':
    flowers_price = 2.80
elif flowers_kind == 'Narcissus':
    flowers_price = 3
elif flowers_kind == 'Gladiolus':
    flowers_price= 2.50

cena = flowers_price * flowers_count

if flowers_kind == 'Roses' and flowers_count > 80:
    cena -= 0.1 * cena
elif flowers_kind == 'Dahlias' and flowers_count > 90:
    cena -= 0.15 * cena
elif flowers_kind == 'Tulips' and flowers_count > 80:
    cena -= 0.15 * cena
elif flowers_kind == 'Narcissus' and flowers_count < 120:
    cena += 0.15 * cena
elif flowers_kind == 'Gladiolus' and flowers_count < 80:
    cena += 0.20 * cena

if budget >= cena:
    print(
        f'Hey, you have a great garden with {flowers_count} {flowers_kind} and {(budget - cena):.2f} leva left.')
elif budget < cena:
    print(f'Not enough money, you need {(cena - budget):.2f} leva more.')
