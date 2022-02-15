broi_masi = int(input())
length = float(input())
width = float(input())

pokrivki_plosht = broi_masi * (length + 2 * 0.30) * (width + 2 * 0.30)
kareta_plosht = broi_masi * (length / 2) * (length / 2)

dollars = pokrivki_plosht * 7 + kareta_plosht * 9
lev = dollars * 1.85
print(f'{dollars:.2f} USD')
print(f'{lev:.2f} BGN')