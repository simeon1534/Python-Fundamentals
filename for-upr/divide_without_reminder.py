n=int(input())

broi_p1=0
broi_p2=0
broi_p3=0

total5=0
for i in range(1,n+1):
    number=int(input())
    if number%2==0:
        broi_p1+=1
    if number%3==0:
        broi_p2+=1
    if number%4==0:
        broi_p3 += 1


p1=broi_p1/n*100
p2=broi_p2/n*100
p3=broi_p3/n*100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')

