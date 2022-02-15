data = input()
dictionary = {}  # language-key name,points-value
banned = []
while not data == "exam finished":
    data = data.split("-")
    if data[1] == "banned":
        banned_person = data[0]
        banned.append(banned_person)
    #   dictionary[language[data[0]]
    else:
        name, language, points = data
        if language in dictionary:
            dictionary[language][name]=points
        else:
            dictionary[language]={"name":name,"points":points}
    data = input()
non_delete_dict = dict(dictionary)
print(non_delete_dict)

# ordered_results=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
print("Results")
for language, name_points in dictionary.items():
    for name,points in name_points.items():
        if dictionary[language]["name"] in banned:
            dictionary[language].pop("name")
            dictionary[language].pop("points")
print(dictionary)
print(non_delete_dict)
# print(f"{name}")
