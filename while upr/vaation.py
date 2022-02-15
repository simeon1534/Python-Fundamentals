money_needed = float(input())
money_owned = float(input())

days_spending = 0
days = 0

while money_owned < money_needed and days_spending < 5:
    deistvie = input()
    suma = float(input())
    days += 1
    if deistvie == 'save':
        money_owned += money_owned
        days_spending = 0
    elif deistvie == 'spend':
        money_owned = money_owned - suma
        days_spending += 1
        if money_owned < 0:
            money_owned = 0


if money_owned >= money_needed:
    print(f'You saved the money for {days} days.')

if days_spending == 5:
    print("You can't save the money.")
    print(days)
