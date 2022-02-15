n = int(input())
salary = int(input())

for i in range(1, n + 1):
    site = input()
    if site == 'Facebook':
        salary = salary - 150
        if salary <= 0:
            print('You have lost your salary.')
            break
    elif site == 'Instagram':
        salary = salary - 100
        if salary <= 0:
            print('You have lost your salary.')
            break
    elif site == 'Reddit':
        salary = salary - 50
        if salary <= 0:
            print('You have lost your salary.')
            break

if salary>0:
    print(salary)
