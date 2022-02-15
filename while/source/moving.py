width = int(input())
length = int(input())
height = int(input())

command = input()
s = width * length * height

while command != 'Done':
    kashoni = int(command)
    s -= kashoni
    if s < 0:
        break
    command=input()
if command == 'Done':
    print(f'{s} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(s)} Cubic meters more.')
