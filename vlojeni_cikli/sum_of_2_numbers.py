start = int(input())
end = int(input())
magic_num = int(input())

combination = 0
found=False
for first_number in range(start, end+1):
    for second_number in range(start, end+1):
        combination += 1
        if first_number + second_number==magic_num:
            print(f'Combination N:{combination} ({first_number} + {second_number} = {magic_num})')
            found=True
            break
    if found:
        break
if not found:
    print(f'{combination} combinations - neither equals {magic_num}')

