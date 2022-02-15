age = int(input())

if age < 1 or age > 77:
    age = int(input())

peralnq = float(input())

if peralnq < 1 or peralnq > 10000:
    peralnq = float(input())

cena_igrachka = int(input())

if cena_igrachka < 0 or cena_igrachka > 40:
    cena_igrachka = int(input())

vsichki_pari=0

vsichki_igrachki = 0
taken_money=0
pari = 0
for i in range(1, age + 1):

    if i % 2 != 0:
        vsichki_igrachki += cena_igrachka

    else:

        pari+=10
        vsichki_pari+=pari
        taken_money=taken_money+1

total=(vsichki_pari+vsichki_igrachki)-taken_money
if total>=peralnq:
    print(f'Yes! {total-peralnq:.2f}')
else:
    print(f'No! {peralnq- total:.2f}')

