width = int(input())
length = int(input())

torta = width * length

stop_command = False
parcheta=0
total_parcheta=0
while torta > total_parcheta:
    command = input()
    if command == 'STOP':
        stop_command = True
        break
    parcheta=int(command)
    total_parcheta=total_parcheta+parcheta

if stop_command:
    print(f'{torta-total_parcheta} pieces are left.')
else:
    print(f'No more cake left! You need {total_parcheta-torta} pieces more.')
