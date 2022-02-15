number_of_electrons = int(input())

electrons=[]
cell_number= 1

while number_of_electrons > 0:
    possible_electrons = 2*cell_number**2
    if number_of_electrons<possible_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(possible_electrons)
    cell_number += 1
    number_of_electrons-=possible_electrons
print(electrons)
