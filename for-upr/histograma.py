n=int(input())

broi_p1=0
broi_p2=0
broi_p3=0
broi_p4=0
broi_p5=0
total5=0
for i in range(1,n+1):
    number=int(input())
    if number<200:
        broi_p1+=1
    if 199<number<400:
        broi_p2+=1
    if 399 < number < 600:
        broi_p3 += 1
    if 599 < number < 800:
        broi_p4 += 1
    if 799 <number  < 1001:
        broi_p5 += 1

p1=broi_p1/n*100
p2=broi_p2/n*100
p3=broi_p3/n*100
p4=broi_p4/n*100
p5=broi_p5/n*100
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

