import re

demons_whitespaces = input().split(",")
demons = [demon.strip() for demon in demons_whitespaces]
demons.sort()

def finding_health(demon):
    pattern_health = r"[^\d\+\*\/\.\-]"
    match_list = re.findall(pattern_health, demon)
    health_letters = [ord(match) for match in match_list]
    health = sum(health_letters)
    return  health

def finding_dmg(demon):
    pattern_dmg=r"(?P<operation>\+?-?)(?P<cqla_chast>\d+)(?P<desetichna_chast>\.?\d+)?"
    match_objects=re.finditer(pattern_dmg,demon)
    result=0
    for match_object in match_objects:
        dict_obj=match_object.groupdict()
        if not dict_obj["desetichna_chast"]==None:
            chislo=float(dict_obj["cqla_chast"]+dict_obj["desetichna_chast"])
        else:
            chislo=int(dict_obj["cqla_chast"])
        if dict_obj["operation"]=="-":
            result -=chislo
        else:
            result+=chislo
    return result

def multiplying_dividing(demon):
    pattern_multi_divide=r"[\*/]"
    result=finding_dmg(demon)
    match_list=re.findall(pattern_multi_divide,demon)
    for match in match_list:
        if match=="*":
            result *=2
        elif match=="/":
            result /=2
    return result

for demon in demons:
    print(f"{demon} - {finding_health(demon)} health, {multiplying_dividing(demon):.2f} damage")

