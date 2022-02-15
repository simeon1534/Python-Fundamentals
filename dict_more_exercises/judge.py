user_contest_points = input()

contest_user_points = {}
user_total_points = {}
while not user_contest_points == "no more time":
    name, contest, points = user_contest_points.split(" -> ")
    points = int(points)
    if not contest in contest_user_points:
        contest_user_points[contest] = {name: points}
    else:
        contest_user_points[contest][name] = points

    if not name in user_total_points:
        user_total_points[name] = points
    else:
        if contest in contest_user_points and points > user_total_points[name]:
            user_total_points[name] = points
        elif not contest in contest_user_points:
            user_total_points[name] += points
    user_contest_points = input()

for contest, user_points_dict in contest_user_points.items():
    print(f"{contest}: {len(user_points_dict)} participants")
    counter = 1
    ordered_user_points_dict = sorted(user_points_dict.items(), key=lambda x: (-x[1], x[0]))
    for user, points in ordered_user_points_dict:
        print(f"{counter}. {user} <::> {points} ")
        counter += 1

print(f"Individual standings:")
counter = 1
ordered_user_total_points = sorted(user_total_points.items(), key=lambda x: (-x[1], x[0]))
for name, total_points in ordered_user_total_points:
    print(f"{counter}. {name} -> {total_points} ")
    counter += 1

# print(contest_user_points)
# print(user_total_points)
