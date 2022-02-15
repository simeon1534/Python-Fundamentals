ime = str(input())
counter = 1
graduation = 12
ocenka = 0
avg = 0
sredno=0
while counter <= graduation:
    ocenka = float(input())
    if ocenka < 4.00:
        ocenka = float(input())
    avg += ocenka
    counter += 1
sredno = avg / 12
print(f'{ime} graduated. Average grade: {sredno:.2f} ')
