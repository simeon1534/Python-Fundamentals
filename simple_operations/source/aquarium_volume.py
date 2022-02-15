# 1. Read dimensions
length = int(input())
width = int(input())
height = int(input())
# 2. Read volume percentage of other stuff
percent_other_stuff = float(input())
# 3. Calculate total volume of the aquarium
total_volume_cm = length * width * height
# 3.1. Turn cm3 to liters
total_liters = total_volume_cm * 0.001
# 4. Calculate percent volume of other stuff
other_stuff_liters = total_liters * (percent_other_stuff * 0.01)
# 5. Calculate left over volume
left_volume = total_liters - other_stuff_liters
# 6. Format and print
print(f'{left_volume:.3f}')