materials = input().split()
materials = [w.lower() for w in materials]
keywords = {"fragments": 0, "motes": 0, "shards": 0}
dictionary = {}


for index in range(0, len(materials), 2):
    quantity = int(materials[index])
    material = materials[index + 1]
    if material in dictionary:
        dictionary[material] = int(dictionary[material]) + int(quantity)
    else:
        dictionary[material] = quantity
    if material in keywords:
        keywords[material] = int(keywords[material]) + int(quantity)

    if material in keywords and  keywords[material]  >=250:
        if material == "fragments":
            print(f"Valanyr obtained!")
        elif material == "motes":
            print(f"Dragonwrath obtained!")
        elif material == "shards":
            print(f"Shadowmourne  obtained!")
        dictionary[material] = dictionary[material]  - 250
        keywords[material] = keywords[material]  - 250
        break

ordered_key_materials = sorted(keywords.items(), key=lambda x: (-x[1], x[0]))

for key_item,quantity in ordered_key_materials:
    print(f"{key_item}: {quantity}")

junk_items={key_item:quantity for key_item,quantity in dictionary.items() if not key_item in keywords}

ordered_junk_items=sorted(junk_items.items(), key=lambda  x: (x[0]))
for key_item,quantity in ordered_junk_items:
    print(f"{key_item}: {quantity}")

