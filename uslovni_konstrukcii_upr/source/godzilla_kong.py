budget_film = float(input())
statists = int(input())
budget_clothes = float(input())

if statists > 150:
    budget_clothes = budget_clothes - (budget_clothes * 0.1)

decor = budget_film * 0.1
statists_clothes = statists * budget_clothes
total_spendings = decor + statists_clothes

if total_spendings > budget_film:
    print('Not enough money!')
    print(f'Wingard needs {total_spendings - budget_film:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget_film - total_spendings:.2f} leva left.')
