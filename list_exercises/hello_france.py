items_with_prices = input().split('|')
budget = float(input())
starting_budget=budget
over_estimated_budget = 0
for items_with_prices_indexes in items_with_prices:
    item_price = items_with_prices_indexes.split('->')
    if item_price[0] == 'Clothes' and float(item_price[1]) <= 50.00:
        if budget >= float(item_price[1]):
            budget -= float(item_price[1])
            overestimated_item_price = 0.40 * float(item_price[1]) + float(item_price[1])
            over_estimated_budget += overestimated_item_price
            print(f'{overestimated_item_price:.2f}', end=' ')
    elif item_price[0] == 'Shoes' and float(item_price[1]) <= 35.00:
        if budget >= float(item_price[1]):
            budget -= float(item_price[1])
            overestimated_item_price = 0.40 * float(item_price[1]) + float(item_price[1])
            over_estimated_budget += overestimated_item_price
            print(f'{overestimated_item_price:.2f}', end=' ')
    elif item_price[0] == 'Accessories' and float(item_price[1]) <= 20.50:
        if budget >= float(item_price[1]):
            budget -= float(item_price[1])
            overestimated_item_price = 0.40 * float(item_price[1]) + float(item_price[1])
            over_estimated_budget += overestimated_item_price
            print(f'{overestimated_item_price:.2f}', end=' ')
profit = over_estimated_budget - starting_budget + budget
print(f'\nProfit: {profit:.2f}')
if profit + starting_budget >= 150.00:
    print('Hello, France!')
else:
    print('Not enough money.')
