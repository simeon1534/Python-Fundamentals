factor=int(input())
count=int(input())
list_multiple=[]
multi_num=0
for num in range(count):
    multi_num+=factor
    list_multiple.append(multi_num)
print(list_multiple)