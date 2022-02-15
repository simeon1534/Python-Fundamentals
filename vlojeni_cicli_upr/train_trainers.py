jury=int(input())
presentacions=input()

obshta_ocenka=0
broi_ocenki=0
while presentacions != 'Finish':
        obshta_ocenka_za_edin=0
        for ocenka in range(1,jury+1):
            broi_ocenki+=1
            ocenka_per_jury=float(input())
            obshta_ocenka_za_edin +=ocenka_per_jury
        print(f'{presentacions} - {obshta_ocenka_za_edin/jury:.2f}.')

        obshta_ocenka+=obshta_ocenka_za_edin

        presentacions = input()

print(f"Student's final assessment is {obshta_ocenka/broi_ocenki:.2f}.")










