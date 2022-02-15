list_string_first=input().split(", ")
list_string_second=input().split(", ")

list_result=[i for i in list_string_first for j in list_string_second  if i in j ]

#for i in list_string_first:
#    for j in list_string_second:
  #      if i in j:
  #          list_result.append(i)
#for p in list_result:
   # if list_result.count(p)>1:
   #     list_result.remove(p)

print(sorted(set(list_result) , key=list_result.index))