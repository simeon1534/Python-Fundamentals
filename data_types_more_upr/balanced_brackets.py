lines = int(input())
bracket_1 = 0
bracket_2 = 0
is_opened=False
is_balanced=True
for line in range(1, lines + 1):
    string = input()

    if string == '(':
        if is_opened==False:
            is_opened=True
        else:
            is_balanced=False
        bracket_1 += 1
    if string == ')':
        if is_opened:
            is_opened = False
        else:
            is_balanced = False
        bracket_2 += 1

if bracket_1 == bracket_2 and  is_balanced == True and  is_opened == False :
    print('BALANCED')
else:
    print('UNBALANCED')
