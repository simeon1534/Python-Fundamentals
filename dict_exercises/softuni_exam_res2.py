data = input()
dict_name_points = {}
dict_language_names={}
banned=[]
while not data == "exam finished":
    data = data.split("-")
    if data[1] == "banned":
        banned_person = data[0]
        banned.append(banned_person)
    #   dictionary[language[data[0]]
    else:
        name, language, points = data
        if language in dict_language_names:
            dict_language_names[language]+=1
        else:
            dict_language_names[language]=0
            dict_language_names[language]+=1
        if name in dict_name_points:
            if dict_name_points[name]<points:
                dict_name_points[name] = points
        else:
            dict_name_points[name]=points
    data = input()

# non_delete_dict = dict(dictionary)
# print(non_delete_dict)
#
ordered_name_points=sorted(dict_name_points.items(),key=lambda x:(-int(x[1]), x[0]))
# print(ordered_name_points)
ordered_language_names=sorted(dict_language_names.items(),key=lambda x:(-x[1], x[0]))
print("Results:")
for name, points in ordered_name_points:
    if not name in banned:
        print(f"{name} | {points}")# print(f"{name} banned")
        #dict_name_points.pop(name)
    # else:


print("Submissions:")
for language, names_list in ordered_language_names:
    print(f"{language} - {names_list}")


# print(dict_language_names)
# print(dict_name_points)