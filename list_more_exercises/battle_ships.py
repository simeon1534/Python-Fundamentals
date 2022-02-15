rows_of_the_field = int(input())
# starting from row 0
# list in list
ships_destroyed=0
coord_list = []
for i in range(rows_of_the_field):
    coord_list.append(input().split(' '))
cols=len(coord_list[0])
attacks = input().split(' ')
for elements in attacks:
    element = elements.split('-')
    row = int(element[0])
    col = int(element[1])
    print(f'{row} {col}', end=' ')
    print(coord_list[row][col])
    if int(coord_list[row][col]) > 0:
        coord_list[row][col] = str(int(coord_list[row][col]) - 1)
        if int(coord_list[row][col])==0:
            ships_destroyed+=1
    print(coord_list[row][col])
print(coord_list)
print(ships_destroyed)
