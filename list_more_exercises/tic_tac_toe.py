import sys
first_row = input().split(' ')
second_row = input().split(' ')
third_row = input().split(' ')
a=0
if a==0:

#rows
    if first_row.count('1') == 3 or second_row.count('1') == 3 or third_row.count('1') == 3:
        print('First player won')
        sys.exit()
    elif first_row.count('2') == 3 or second_row.count('2') == 3 or third_row.count('2') == 3:
        print('Second player won')
        sys.exit()
#columns
    if first_row[0] == '1' and second_row[0] == '1' and third_row[0] == '1':
        print('First player won')
        sys.exit()
    elif first_row[0] == '2' and second_row[0] == '2' and third_row[0] == '2':
        print('Second player won')
        sys.exit()
    if first_row[1] == '1' and second_row[1] == '1' and third_row[1] == '1':
        print('First player won')
        sys.exit()
    elif first_row[1] == '2' and second_row[1] == '2' and third_row[1] == '2':
        print('Second player won')
        sys.exit()
    if first_row[2] == '1' and second_row[2] == '1' and third_row[2] == '1':
        print('First player won')
        sys.exit()
    elif first_row[2] == '2' and second_row[2] == '2' and third_row[2] == '2':
        print('Second player won')
        sys.exit()
#diagonals
    if first_row[0] == '1' and second_row[1] == '1' and third_row[2] == '1':
        print('First player won')
        sys.exit()
    elif first_row[0] == '2' and second_row[1] == '2' and third_row[2] == '2':
        print('Second player won')
        sys.exit()
    if first_row[2] == '1' and second_row[1] == '1' and third_row[0] == '1':
        print('First player won')
        sys.exit()
    elif first_row[2] == '2' and second_row[1] == '2' and third_row[0] == '2':
        print('Second player won')
        sys.exit()

print('Draw!')