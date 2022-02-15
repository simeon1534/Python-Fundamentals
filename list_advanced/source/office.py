employee_happiness = input().split(' ')
happiness_factor = int(input())

unfiltered_result = [int(employee) * happiness_factor for employee in employee_happiness]

obshto_employee=0
counter=0

for el in unfiltered_result:
    obshto_employee+=el
    counter+=1
avg=obshto_employee/counter

filtered_result = [employee1 for employee1 in unfiltered_result if employee1>=avg   ]

if len(employee_happiness) / 2 <= len(filtered_result):
    print(f"Score: {len(filtered_result)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_result)}/{len(employee_happiness)}. Employees are not happy!")
