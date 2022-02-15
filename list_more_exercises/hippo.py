rows_of_the_field = int(input())
# starting from row 0
# list in list

row = 0
col = 0
col_previous = 0
row_previous = 0
length_columns = 0
block_food = 0
block_list = []
searching_food = True
finding_food = False
for i in range(rows_of_the_field):
    block_list.append(input().split(' '))
    length_columns = len(block_list[0])
while row < rows_of_the_field:  # for lists in block_list:

    while col < length_columns :  # for lists in block_list:

        if int(block_list[row][col]) == 1:

            row_previous = row - 1
            col_previous = col - 1
            if row > 0 and col > 0:
                if int(block_list[row_previous][col]) == 0 and int(block_list[row][col_previous]) == 0:
                    block_food += 1
                if int(block_list[row_previous][col]) == 1 and int(block_list[row][col_previous]) == 1 and  int(block_list[row_previous][col_previous]) == 0:
                    block_food -= 1
            if row > 0 and col == 0:
                if int(block_list[row_previous][col]) == 0:
                    block_food += 1
                if int(block_list[row_previous][col]) == 1:
                    pass
            if row == 0 and col > 0:
                if int(block_list[row][col_previous]) == 0:
                    block_food += 1
                if int(block_list[row][col_previous]) == 1:
                    pass
            if row == 0 and col == 0:
                    block_food += 1


        col += 1
    row += 1
    col = 0
    col_previous = 0
    row_previous = 0
    print(block_food)
print(block_food)
    # block_list[row][col] = str(int(block_list[row][col]) - 1)
    # elif col == length_columns and row < rows_of_the_field:
    #    row += 1
    # else:
    #    block_food+=1
    #    break
