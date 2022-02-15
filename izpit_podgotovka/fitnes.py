posetiteli = int(input())

back = 0
chest = 0
legs = 0
abs = 0
prot_shake=0
prot_bar=0


trenirashti=0
protein=0
for chovek in range(1, posetiteli + 1):


    deinost = input()
    if deinost == 'Back':
        back += 1
    elif deinost == 'Chest':
        chest += 1
    elif deinost == 'Legs':
        legs += 1
    elif deinost == 'Abs':
        abs += 1
    elif deinost == 'Protein shake':
        prot_shake += 1
    elif deinost == 'Protein bar':
        prot_bar += 1
    trenirashti = back + chest + legs + abs
    protein = prot_shake + prot_bar
print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{prot_shake} - protein shake')
print(f'{prot_bar} - protein bar')
print(f'{(trenirashti/posetiteli)*100:.2f}% - work out')
print(f'{(protein/posetiteli)*100:.2f}% - protein')
