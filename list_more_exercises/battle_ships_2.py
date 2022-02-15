rows_of_the_field = int(input())
the_field=''
field=''
# starting from row 0
# list in list
ships_destroyed=0
coord_list = []
cols=0

for i in range(rows_of_the_field):
    field = input()
    cols = int((int(len(field))+1)/2)
    if the_field=='':
        the_field = the_field + field
    else:
        the_field = the_field + ' ' + field


coord_list=the_field.split(" ")

attacks = input().split(' ')
print(the_field)
print(coord_list)
print(cols)

for elements in attacks:
    element = elements.split('-')
    row = int(element[0])
    col = int(element[1])
    print(f'{row} {col}', end=' ')
    print(row*cols+col)

    if int(coord_list[row*cols+col])> 0:
        coord_list[row*cols+col] = str(int(coord_list[row*cols+col]) - 1)
        if int(coord_list[row*cols+col])==0:
            ships_destroyed+=1
    print(coord_list[row*cols+col])
print(coord_list)
print(ships_destroyed)
