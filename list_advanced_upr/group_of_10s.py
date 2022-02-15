import math
list_of_numbers=input().split(", ")
max_value=0
step=10

for num in list_of_numbers:
    if int(num)>max_value:
        max_value=int(num)
for i in range(10,int(math.ceil(max_value/10.0)*10)+1,10):
    list_dobaven=[int(num) for num in list_of_numbers if step-9<=int(num)<=step]
    #for num in list_of_numbers:
    #    if step-9<=int(num)<=step:
           # list_of_numbers.remove(int(num))
     #       list_dobaven.append(int(num))
    print(f"Group of {step}'s: {list_dobaven}")
    step+=10
