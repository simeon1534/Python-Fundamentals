numbers_list=input().split()
string_list=list(input())
result=[]
def messaging(list_nums,list_string,res):
    for group_of_num in list_nums:
        index_for_text=0
        for num in group_of_num:
            index_for_text+=int(num)
        if index_for_text>len(list_string) - 1:
            while index_for_text>len(list_string)-1:
                index_for_text=index_for_text-len(list_string)
        removed_element=list_string.pop(index_for_text)
        res.append(removed_element)
    return res
messaging(numbers_list,string_list,result)
print(''.join(result))