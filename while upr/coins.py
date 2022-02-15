resto = float(input())

resto=int(resto*100)
# coins_total=0
coins = 0
done=False
while 0 < resto:
    coins += 1
    if resto >= 200:
        resto = resto - 200
    elif resto >= 100:
        resto = resto - 100
    elif resto >=50:
        resto=resto-50
    elif resto>=20:
        resto=resto-20
    elif resto >= 10:
        resto = resto - 10
    elif resto >= 5:
        resto = resto - 5
    elif resto>=2:
        resto=resto-2
    elif resto >= 1:
        resto = resto - 1

print(coins)
