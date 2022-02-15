fires_with_cells = input().split('#')
water_given = int(input())
total_effort = 0
total_fire = 0
print('Cells:')
for fires_with_cells_indexes in fires_with_cells:
    fire_cell = fires_with_cells_indexes.split(' = ')
    if fire_cell[0] == 'High' and 80 < int(fire_cell[1]) < 126:
        if water_given >= int(fire_cell[1]):
            water_given -= int(fire_cell[1])
            effort = 0.25 * int(fire_cell[1])
            total_effort += effort
            total_fire += int(fire_cell[1])
            print(f' - {int(fire_cell[1])}')
    elif fire_cell[0] == 'Medium' and 50 < int(fire_cell[1]) < 81:
        if water_given >= int(fire_cell[1]):
            water_given -= int(fire_cell[1])
            effort = 0.25 * int(fire_cell[1])
            total_effort += effort
            total_fire += int(fire_cell[1])
            print(f' - {int(fire_cell[1])}')
    elif fire_cell[0] == 'Low' and 0 < int(fire_cell[1]) < 51:
        if water_given >= int(fire_cell[1]):
            water_given -= int(fire_cell[1])
            effort = 0.25 * int(fire_cell[1])
            total_effort += effort
            total_fire += int(fire_cell[1])
            print(f' - {int(fire_cell[1])}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
