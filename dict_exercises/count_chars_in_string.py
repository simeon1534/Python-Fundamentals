data=input()
listed_data=list(data)

dictionary={}

for character in listed_data:
        if not character==' ':
            dictionary.update({character : listed_data.count(character)})

for key,value in dictionary.items():
    print(f"{key} -> {value}")
print(dictionary.items())