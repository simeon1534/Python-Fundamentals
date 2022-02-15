n = int(input())
odd=[]
even=[]
positive=[]
negative=[]
filtered_list = []
num = 0
for i in range(1, n + 1):
    num = int(input())
    if num >= 0:
        positive.append(num)
    if  num < 0:
        negative.append(num)
    if  num % 2 != 0:
        odd.append(num)
    if  num % 2 == 0:
        even.append(num)

command = input()
if command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)
elif command == 'even':
    print(even)
elif command == 'odd':
    print(odd)




