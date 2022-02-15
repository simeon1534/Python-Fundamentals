data = input()

user_position_points = {}
player_total_skill = {}
while not data == "Season end":
    splitted_data = data.split()
    if len(splitted_data) > 3:
        player, position, skill = data.split(" -> ")
        skill = int(skill)
        if not player in user_position_points:
            user_position_points[player] = {position: skill}
            player_total_skill[player] = {"total_skill": skill}
        # elif player in user_position_points and position not in user_position_points[player]:
        #     user_position_points[player].update({position: skill})
        #     player_total_skill[player]["total_skill"] += skill

        elif player in user_position_points:
            # Proverka dali tochkite trqbva da se updatnat ako sa poveche
            if position in user_position_points[player]:
                if user_position_points[player][position] < skill:
                    player_total_skill[player]["total_skill"] += skill - user_position_points[player][position]
                    user_position_points[player][position] = skill
            elif player in user_position_points and position not in user_position_points[player]:
                user_position_points[player][position] = skill
                player_total_skill[player]["total_skill"] += skill
    elif len(splitted_data) == 3:
        player1, player2 = data.split(" vs ")
        duel = False
        if player1 in user_position_points and player2 in user_position_points:
            for positions in user_position_points[player1]:
                if positions in user_position_points[player2].keys():
                    duel = True
                    break
            if duel:
                if sum(user_position_points[player1].values()) > sum(user_position_points[player2].values()):
                    user_position_points.pop(player2)
                    player_total_skill.pop(player2)
                elif user_position_points[player1]["total_skill"] < user_position_points[player2]["total_skill"]:
                    user_position_points.pop(player1)
                    player_total_skill.pop(player1)
    data = input()

# print(user_position_points)
# print(player_total_skill)
player_total_skill_copied = player_total_skill.copy()
for player, total_skill_dict in player_total_skill_copied.items():
    for string, total_skill in total_skill_dict.items():
        player_total_skill_copied[player] = total_skill

ordered_player_total_skill = sorted(player_total_skill_copied.items(), key=lambda x: (-x[1], x[0]))
# print(player_total_skill)
# print(player_total_skill_copied)
for player, total_skill in ordered_player_total_skill:
    print(f"{player}: {total_skill} skill")
    ordered_user_position_points_player = sorted(user_position_points[player].items(), key=lambda x: (-x[1], x[0]))
    for position, skill in ordered_user_position_points_player:
        print(f"- {position} <::> {skill}")
