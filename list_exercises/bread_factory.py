events_ingredients_numbers = input().split('|')
initial_energy = 100
initial_coins = 100

failed_day = False
for event_ingredient_number in events_ingredients_numbers:
    event_ingredient_number_divided = event_ingredient_number.split('-')
    if event_ingredient_number_divided[0] == 'rest':
        initial_energy += int(event_ingredient_number_divided[1])
        if initial_energy > 100:
            over_initial_energy = initial_energy - 100
            energy_gained = int(event_ingredient_number_divided[1]) - over_initial_energy
            print(f'You gained {energy_gained} energy.')
            initial_energy = 100
            print(f"Current energy: {initial_energy}.")
        else:
            print(f'You gained {int(event_ingredient_number_divided[1])} energy.')
            print(f"Current energy: {initial_energy}.")

    elif event_ingredient_number_divided[0] == 'order':

        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += int(event_ingredient_number_divided[1])
            print(f"You earned {int(event_ingredient_number_divided[1])} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")
    else:

        if initial_coins > int(event_ingredient_number_divided[1]):
            initial_coins -= int(event_ingredient_number_divided[1])
            print(f"You bought {event_ingredient_number_divided[0]}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient_number_divided[0]}.")
            failed_day = True
            break
if failed_day:
    pass
else:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
