dragons_count = int(input())

dragons_stats = {}
avg_color = {}
list_colors = []
for i in range(dragons_count):
    color, name, dmg, health, armor = input().split()
    # checking for default
    if dmg == "null":
        dmg = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    dmg = int(dmg)
    health = int(health)
    armor = int(armor)
    id = name + "-" + color

    if not id in dragons_stats:
        dragons_stats[id] = [dmg, health, armor]
        list_colors.append(color)
    elif id in dragons_stats:
        dragons_stats[id] = [dmg, health, armor]

for key,value in dragons_stats.items():
    name,color=key.split("-")
    dmg = value[0]
    health = value[1]
    armor = value[2]
    if not color in avg_color:
        avg_color[color] = [dmg, health, armor]
    elif color in avg_color:
        avg_color[color] = [(avg_color[color][0] + dmg), (avg_color[color][1] + health),
                            (avg_color[color][2] + armor)]
ordered_dragons_stat = sorted(dragons_stats.items(), key=lambda x: x[0])

for key, value in avg_color.items():
    avg_color[key] = [value[0] / list_colors.count(key), value[1] / list_colors.count(key),
                      value[2] / list_colors.count(key)]
    print(
        f"{key}::({value[0] / list_colors.count(key):.2f}/{value[1] / list_colors.count(key):.2f}/{value[2] / list_colors.count(key):.2f})")
    for key1, value1 in ordered_dragons_stat:
        name, color = key1.split("-")
        if color == key:
            print(f"-{name} -> damage: {value1[0]}, health: {value1[1]}, armor: {value1[2]}")
