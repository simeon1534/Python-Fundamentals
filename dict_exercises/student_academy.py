pairs = int(input())

dictionary = {}
for i in range(1, pairs + 1):
    name = input()
    grade = float(input())
    if name in dictionary:
        dictionary[name].append(grade)
    else:
        dictionary[name] = []
        dictionary[name].append(grade)

average_dictionary = {}

for name, grade_list in dictionary.items():
    average_grade = sum(grade_list) / len(grade_list)
    if average_grade >= 4.50:
        average_dictionary[name] = average_grade
        #print(f"{name} -> {average_grade:.2f}")

ordered_average_dictionary=sorted(average_dictionary.items(),key=lambda x:x[1],reverse=True)

for name,avg_grade in ordered_average_dictionary:
    print(f"{name} -> {avg_grade:.2f}")