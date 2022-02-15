import re
string_of_participants=input().split(", ")
dict_of_participants=dict.fromkeys(string_of_participants, 0)

pattern_name=r"[A-Za-z]+"
pattern_km=r"\d"

data=input()

while not data=="end of race":
    name_letters=re.findall(pattern_name,data)
    name="".join(name_letters)
    if name in dict_of_participants:
        km = re.findall(pattern_km, data)
        total_km = sum(int(i) for i in km)
        #print(total_km)
        dict_of_participants[name]+=total_km
    data = input()
#print(dict_of_participants)
ordered_dict=sorted(dict_of_participants.items(),key=lambda x:x[1],reverse=True)
#print(ordered_dict)
mesta=['1st','2nd','3rd']
index_mesta=0
for name,km in ordered_dict:
    print(f"{mesta[index_mesta]} place: {name}")
    index_mesta+=1
    if index_mesta>2:
        break
