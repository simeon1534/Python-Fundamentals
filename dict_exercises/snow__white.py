data = input()
name_hat_dict = {}
colors_count = {}


def plus_one(def_hat_color, def_colors_count):
    if def_hat_color in def_colors_count:
        def_colors_count[def_hat_color] += 1
    else:
        def_colors_count[def_hat_color] = 1


while not data == "Once upon a time":
    name, hat_color, physics = data.split(" <:> ")
    physics = int(physics)
    if name in name_hat_dict and hat_color not in name_hat_dict[name]:
        name_hat_dict[name][1] = physics
        plus_one(hat_color, colors_count)


    elif name in name_hat_dict and hat_color in name_hat_dict[name]:
        if name_hat_dict[name][1] < physics:
            name_hat_dict[name][1] = physics

    else:
        name_hat_dict[name] = []
        name_hat_dict[name].append(hat_color)
        name_hat_dict[name].append(physics)
        plus_one(hat_color, colors_count)

    data = input()
print(name_hat_dict)
print(colors_count)
print(name_hat_dict.items())
#ordered_dict = sorted(name_hat_dict.items(), key=lambda name: name_hat_dict[name])
#ordered_total_count = sorted(colors_count.items(), key=lambda x: x[1])
#
#for hat, value in ordered_total_count:
  #  print(f"({hat})")
    #  f"{name} <-> {physics}")

#for name, value in ordered_dict:
 #   print(f"{name} <-> {value}")
#print(ordered_dict)