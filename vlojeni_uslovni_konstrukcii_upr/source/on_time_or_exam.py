hours_exam = int(input())
mins_exam = int(input())
hours_arrival = int(input())
mins_arrival = int(input())

total_exam_mins = hours_exam * 60 + mins_exam
total_mins_arrival = hours_arrival * 60 + mins_arrival

diff = total_exam_mins - total_mins_arrival

if diff < 0:
    # Late
    diff *= -1
    if diff > 60:
        print_hours = diff // 60
        print_mins = diff % 60
        if print_mins < 10:
            print(f'Late')
            print(f'{print_hours}:0{print_mins} hours after the start')
        else:
            print(f'Late\n{print_hours}:{print_mins}  hours after the start')
    else:
        print(f'Late\n{diff} minutes after the start')
else:
    if diff > 30:
    # podranil
        if diff >= 60:
            print_hours = diff // 60
            print_mins = diff % 60
            if print_mins < 10:
                print(f'Early')
                print(f'{print_hours}:0{print_mins} hours before the start')
            else:
                print(f'Early\n{print_hours}:{print_mins}  hours before the start')
        else:
            print(f'Early\n{diff} minutes before the start')
    else:
        print(f'On time\n{diff} minutes before the start')

# on time
