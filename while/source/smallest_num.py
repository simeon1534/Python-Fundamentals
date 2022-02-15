import sys

broi = int(input())  # chislo ili Stop
max_num = sys.maxsize
counter=1

while counter <= broi:
    number = int(input())
    if number < max_num:
        max_num = number
    counter+=1


print(max_num)
