key = input()
dictionary = {}
while not key == "stop":
    value = int(input())
    if key in dictionary:
        dictionary[key]=dictionary[key]+value
    else:
        dictionary[key] = value
    key = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")
