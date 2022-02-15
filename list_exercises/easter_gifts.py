gift_list = input().split(' ')
command = input().split(' ')
new_gift_list = []

for gifts in gift_list:
    new_gift_list.append(gifts)

while command != 'No Money':
    index = 0
    if 'OutOfStock' in command:
        for gift in new_gift_list:
            if gift == command[1]:
                new_gift_list[index] = None
            index += 1
            # do tuk vqrno
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(new_gift_list):
             new_gift_list[index] = command[1]
    elif 'JustInCase' in command:
        new_gift_list[-1] = command[1]
    command = input()
while 'None' in new_gift_list:
    new_gift_list.remove('None')

for i in new_gift_list:
    print(i, end=" ")
