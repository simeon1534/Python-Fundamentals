projection = input()
r = int(input())
c = int(input())
hora = r * c
pari = 0
if projection == 'Premiere':
    pari = hora * 12
elif projection == 'Normal':
    pari = hora * 7.50
elif projection == 'Discount':
    pari = hora * 5
print(f'{pari:.2f} leva')