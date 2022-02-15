data = input()

dictionary = {}
users = {}
while not data == "Lumpawaroo":
    if "|" in data:
        forceSide, forceUser = data.split(" | ")
        if not forceUser in users:
            users[forceUser] = ""
            if forceSide in dictionary:
                dictionary[forceSide].append(forceUser)
            else:
                dictionary[forceSide] = []
                dictionary[forceSide].append(forceUser)
    if "->" in data:
        forceUser, forceSide = data.split(" -> ")
        if forceUser in users:
            for key in dictionary:
                if forceUser in dictionary[key]:
                    dictionary[key].remove(forceUser)
            if forceSide in dictionary:
                dictionary[forceSide].append(forceUser)
            else:
                dictionary[forceSide] = []
                dictionary[forceSide].append(forceUser)
        else:
            if forceSide in dictionary:
                dictionary[forceSide].append(forceUser)
            else:
                dictionary[forceSide] = []
                dictionary[forceSide].append(forceUser)
        print(f"{forceUser} joins the {forceSide} side!")
    data = input()
ordered_sides = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))
for forceSide, forceUser in ordered_sides:
    if len(dictionary[forceSide])>0:
        print(f"Side: {forceSide}, Members: {len(dictionary[forceSide])}")
    dictionary[forceSide].sort()
    for user in dictionary[forceSide]:
        print(f"! {user}")
