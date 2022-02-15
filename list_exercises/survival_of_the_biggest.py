import sys

str_numbers = input().split(' ')
removed_num_count = int(input())

min_num = sys.maxsize

removed_list = []

for str_num in str_numbers:
    num = int(str_num)
    removed_list.append(num)
for i in range(1,removed_num_count+1):

    for num in removed_list:
        if num < min_num:
            min_num = num
            delete_num=min_num

    removed_list.remove(min_num)
    min_num=sys.maxsize

removed_list_str=[]

for num in removed_list:
    num=str(num)
    removed_list_str.append(num)

print(', '.join(removed_list_str))