import math

year = input()
p = int(input())  # praznici koito ne sa sybota ili nedelq
h = int(input())  # uikendi v rodniq si grad

h_sofia = 48 - h  # uikendi v sofia
h_sofia = h_sofia * (3 / 4)  # sybotni igri v sofia
p_sofia = p * (2 / 3)

vsichki_igri = h_sofia + p_sofia + h
if year == 'leap':
    vsichki_igri+=0.15*vsichki_igri
print(f'{math.floor(vsichki_igri)}')