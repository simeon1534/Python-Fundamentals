steps_goal = 10000
total_steps = 0

while total_steps < steps_goal:
    next_command = input()

    if next_command == 'Going home':
        next_steps=int(input())
        total_steps += next_steps
        break


    next_steps = int(next_command)
    total_steps += next_steps
if total_steps>=steps_goal:
    print('Goal reached! Good job!')
    print(f'{ total_steps- steps_goal} steps over the goal!')
else:
    print(f'{steps_goal - total_steps} more steps to reach goal.')