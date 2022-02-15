
total_money_saved=0
while True:
    destination=input()
    if destination=='End':

        break
    money_needed=float(input())
    while True:
        money_saved=float(input())
        total_money_saved+=money_saved
        if total_money_saved>=money_needed:
            total_money_saved=0
            print(f'Going to {destination}!')
            break




