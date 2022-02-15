start_list = input().split(' ')
k = int(input())
indexes_moved = k - 1



end_list = []
while len(start_list)!=0:
    for str_number in start_list:
        if str_number == start_list[indexes_moved]:
            number = int(str_number)
            end_list.append(number)
            indexes_moved += k
        if indexes_moved> len(start_list)-1:          #kogato indexa stane po golqm ot masiva
            indexes_moved=indexes_moved-len(start_list)
            counter = 0
            for i in start_list:
                if int(i)==end_list[0+counter]:
                    start_list.remove(i)
                    counter+=1

            break
