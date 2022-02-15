n = int(input())
max_capacity = 255
current_capacity=0
for i in range(1, n + 1):
    quantity_of_water = int(input())

    if current_capacity+quantity_of_water<255:
        current_capacity += quantity_of_water
    else:
        print('Insufficient capacity!')

print(current_capacity)