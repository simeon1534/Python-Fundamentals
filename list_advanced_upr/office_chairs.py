rooms = int(input())
result_free = 0
result_needed = 0
for i in range(1, rooms + 1):
    chairs_people = input().split()
    free_chairs_left = [int(chairs_people[0].count('X')) - int(chairs_people[1]) for p in range(1, 2) if
                        int(chairs_people[0].count('X')) > int(chairs_people[1])]
    needed_chairs = [int(chairs_people[1]) - int(chairs_people[0].count('X')) for p in range(1, 2) if
                     int(chairs_people[0].count('X')) < int(chairs_people[1])]
    if not free_chairs_left == []:
        result_free += free_chairs_left[0]
    if not needed_chairs == []:
        result_needed += needed_chairs[0]
        print(f'{needed_chairs[0]} more chairs needed in room {i}')
if not result_free == 0 and result_needed == 0:
    print(f'Game On, {result_free} free chairs left')
if  result_free == 0 and result_needed == 0:
    print(f'Game On, 0 free chairs left')