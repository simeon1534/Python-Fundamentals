num = int(input())
bonus_points=0
if num <= 100:
    points = 5
elif num > 100 and num <= 1000:
    points = num * 0.2
else:
    points = num * 0.1
if num % 2 == 0:
    bonus_points = 1
elif num % 10==5:
    bonus_points = 2

print(points + bonus_points)
print(num + points + bonus_points)
