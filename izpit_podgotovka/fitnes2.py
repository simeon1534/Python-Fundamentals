posetiteli = int(input())

back = 0
for chovek in range(1, posetiteli + 1):
    deinost = input()
    if deinost == 'Back':
        back += 1