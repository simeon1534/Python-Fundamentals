data=input()
dictionary={}
while not data=="End":
    company,employee_id=data.split(" -> ")
    if company in dictionary:
        dictionary[company].append(employee_id)
    else:
        dictionary[company]=[]
        dictionary[company].append(employee_id)
    data=input()

#ordered_name_list=sorted(dictionary.items(),key=lambda x:x[1])
ordered_companies=dict(sorted(dictionary.items(),key=lambda x :x[0]))
for company,id_list in ordered_companies.items():
    print(f"{company}")
    unique_id_list=list(dict.fromkeys(id_list))
    for id in unique_id_list:
        print(f"-- {id}")

