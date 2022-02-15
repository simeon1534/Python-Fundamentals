dni_za_prestoi = int(input())
vid_pomeshtenie = input()
ocenka = input()

noshtuvki = dni_za_prestoi - 1
kraina_cena=0
if vid_pomeshtenie == 'room for one person':
    cena = noshtuvki * 18
    kraina_cena=cena
elif vid_pomeshtenie == 'apartment':
    cena = noshtuvki * 25
    if dni_za_prestoi < 10:
        kraina_cena = cena - (0.30 * cena)
    elif 10 <= dni_za_prestoi <= 15:
        kraina_cena = cena - (0.35 * cena)
    elif dni_za_prestoi > 15:
        kraina_cena = cena - (0.50 * cena)
elif vid_pomeshtenie == 'president apartment':
    cena = noshtuvki * 35
    if dni_za_prestoi < 10:
        kraina_cena = cena - (0.10 * cena)
    elif 10 <= dni_za_prestoi <= 15:
        kraina_cena = cena - (0.15 * cena)
    elif dni_za_prestoi > 15:
        kraina_cena = cena - (0.20 * cena)

if ocenka == 'positive':
    kraina_cena += 0.25 * kraina_cena
elif ocenka == 'negative':
    kraina_cena -= 0.10 * kraina_cena
print(f'{kraina_cena:.2f}')
