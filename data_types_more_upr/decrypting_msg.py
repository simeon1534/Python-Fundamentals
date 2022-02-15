key=int(input())
number_of_lines=int(input())
for line in range(1,number_of_lines+1):
    character=input()
    num_character=ord(character)
    print(f'{chr(num_character+key)}' , end='')