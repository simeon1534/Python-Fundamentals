command_contests = input()

courses_pass_dict = {}
while not command_contests == "end of contests":
    course, password = command_contests.split(":")
    courses_pass_dict[course]=password
    command_contests = input()

command_submissions=input()

names_course_points={}
while not command_submissions=="end of submissions":
    course, password ,name,points=command_submissions.split("=>")
    points=int(points)
    if course in courses_pass_dict and courses_pass_dict[course]==password:
        if not name in names_course_points:
            names_course_points[name]={course:points}
        else:
            #Proverka dali tochkite trqbva da se updatnat ako sa poveche
            if course in names_course_points[name]:
                if names_course_points[name][course] < points:
                    names_course_points[name][course] = points
            else:
                names_course_points[name][course]=points
    command_submissions = input()

best_candidate=""
best_candidate_points=0
for name,course_points_dict in names_course_points.items():
    points_for_name=0
    for course,points in course_points_dict.items():
        points_for_name+=points
    if points_for_name>best_candidate_points:
        best_candidate_points=points_for_name
        best_candidate=name


ordered_names_course_points=sorted(names_course_points.items(),key=lambda x:x[0])
print(f"Best candidate is {best_candidate} with total {best_candidate_points} points.")
print("Ranking:")
for name,course_points_dict in ordered_names_course_points:
    print(name)
    ordered_course_points_dict = sorted(course_points_dict.items(),key=lambda x:x[1],reverse=True)
    for course,points in ordered_course_points_dict:
        print(f"#  {course} -> {points} ")

