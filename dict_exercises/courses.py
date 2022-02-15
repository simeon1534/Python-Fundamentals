data=input()
dictionary={}
names=[]
while not data=="end":
    course,name=data.split(" : ")
    if course in dictionary:
        dictionary[course].append(name)
    else:
        dictionary[course]=[]
        dictionary[course].append(name)
    data=input()

#ordered_name_list=sorted(dictionary.items(),key=lambda x:x[1])
sorted_names=3
ordered_courses=dict(sorted(dictionary.items(),key=lambda x :len(x[1]),reverse=True))
for course,name_list in ordered_courses.items():
    print(f"{course}: {len(name_list)}")
    name_list.sort()
    for name in name_list:
        print(f"-- {name}")

