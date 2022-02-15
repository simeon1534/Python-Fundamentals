etaji = int(input())
stai = int(input())
counter_l = 0
counter_o = 0
counter_a = 0
only_floor=False



for e in range( etaji ,0,-1):
 #   if e!=etaji:
    #    print(f'\n')
    if etaji == 1:
        only_floor = True
        break
    for s in range(1, stai + 1):
        if e == etaji:
            print(f'L{etaji}{counter_l}', end=" ")
            counter_l += 1

        elif e != etaji and e % 2 == 0:
            print(f'O{e}{counter_o}', end=" ")
            counter_o += 1
            if counter_o==stai:
                counter_o=0
        elif e != etaji and e % 2 != 0:
            print(f'A{e}{counter_a}', end=" ")
            counter_a += 1
            if counter_a == stai:
                counter_a = 0
    print()

if only_floor:
    for e in range(etaji, 0, -1):
        for s in range(1, stai + 1):
            if e == etaji:
                print(f'L{etaji}{counter_l}', end=' ')
                counter_l += 1






