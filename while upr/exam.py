bad_grades = int(input())
bad_grades_count=0

total = 0
problem_count = 0

last_problem=0
zadachi=0

while True:
    problem = input()
    if problem=='Enough':
        break

    last_problem=problem


    grade = int(input())
    total +=grade
    problem_count += 1

    if grade <= 4:
        bad_grades_count += 1

        if bad_grades_count==bad_grades:
            print(f'You need a break, {bad_grades_count} poor grades.')
            break

if bad_grades_count!=bad_grades:
    print(f'Average score: {total/problem_count:.2f}')
    print(f'Number of problems: {problem_count}')
    print(f'Last problem: {last_problem}')
