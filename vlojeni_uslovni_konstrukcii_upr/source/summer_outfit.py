gradusi=int(input())
vreme=input()
Outfit=0
Shoes=0
if vreme=='Morning':
    if 10 <= gradusi <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif 18 < gradusi <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif gradusi >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
elif vreme=='Afternoon':
    if 10 <= gradusi <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < gradusi <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif gradusi >= 25:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
elif vreme == 'Evening':
    if 10 <= gradusi <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < gradusi <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif gradusi >= 25:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
print(f"It's {gradusi} degrees, get your {Outfit} and {Shoes}.")