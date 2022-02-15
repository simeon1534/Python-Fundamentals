number_of_commands = int(input())
dictionary = {}

for i in range(1, number_of_commands + 1):
    data = input().split()
    # data[0]=command
    # data[1]=username
    # data[2]=license_plate
    if data[0] == "register":
        if data[1] in dictionary:
            print(F"ERROR: already registered with plate number {dictionary[data[1]]}")
        else:
            dictionary[data[1]] = data[2]
            print(f"{data[1]} registered {data[2]} successfully")
    elif data[0] == "unregister":
        if not data[1] in dictionary:
            print(f"ERROR: user {data[1]} not found")
        elif data[1] in dictionary:
            dictionary.pop(data[1])
            print(f"{data[1]} unregistered successfully")

for user, car in dictionary.items():
    print(f"{user} => {car}")
