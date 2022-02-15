import math

party_size = int(input())
days = int(input())
current_coins = 50*days
# drink_coins=0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        party_size = party_size - 2
    if current_day % 15 == 0:
        party_size = party_size + 5
    current_coins -= 2 * party_size

    if current_day % 3 == 0:
        current_coins = current_coins - 3 * party_size
    if current_day % 5 == 0:
        current_coins = current_coins + 20 * party_size
        if current_day % 3 == 0:
            current_coins = current_coins - 2 * party_size
  #  if current_day % 10 == 0:
    #    party_size = party_size - 2
  #  if current_day % 15 == 0:
     #   party_size = party_size + 5

coins=current_coins //party_size
print(f'{party_size} companions received {int(coins)} coins each.')
