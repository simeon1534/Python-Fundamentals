dni = int(input())
sladkari = int(input())
torti = int(input())
gofreti = int(input())
palachinki = int(input())

cena_torti = torti * 45
cena_gofreti = gofreti * 5.80
cena_palachinki = palachinki * 3.20
za_den = (cena_torti + cena_gofreti + cena_palachinki) * sladkari
obshto = za_den * dni

total = obshto - (obshto * (1 / 8))
print(f'{total:.2f}')
