cena_whiskey = float(input())
beer = float(input())
wine = float(input())
rakiq = float(input())
whiskey = float(input())

cena_rakiq = cena_whiskey / 2
cena_wine = cena_rakiq - (0.4 * cena_rakiq)
cena_beer = cena_rakiq - (0.8 * cena_rakiq)

sum_rakiq = cena_rakiq * rakiq
sum_wine = cena_wine * wine
sum_beer = cena_beer * beer
sum_whiskey = cena_whiskey * whiskey
sum=sum_rakiq+sum_wine+sum_beer+sum_whiskey
print(f'{sum:.2f}')
