import sys

n=int(input())
max=-sys.maxsize
sum=0
for i in range(1,n+1):
    number=int(input())
    if number>max:
        max=number
    sum+=number

if max==sum-max:
    print(f'Yes\nSum = {sum-max}')
else:
    print(f'No\nDiff = {abs(max-(sum-max))}')
