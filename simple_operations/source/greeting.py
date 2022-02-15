first_name = input()
last_name = input()
age = int(input())
town = input()

# "You are {first_name} {last_name}, a {age}-years old person from {town}."

#print("You are" + first_name + " " + last_name + ", a " + str(age) + "-years old person from" + " " + town)
#print('---------')
#print(f'You are {first_name} {last_name}')
#print('---------')
print('You are %s %s, a %d-years old person from %s.' % (first_name,last_name,age,town))
#print('---------')
#print('You are {first_name} {last_name}'.format(first_name=first_name , last_name=last_name))