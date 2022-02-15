note = input()

to_do_list = [0 for _ in range(10)]
while not note == 'End':
    data = note.split('-')
    importance = int(data[0])
    task = data[1]
    to_do_list.insert(importance, task)

    note = input()
result = [task for task in to_do_list if not task==0]

#for el in to_do_list:
 #   if el != 0:
 #       result.append(el)
print(result)
