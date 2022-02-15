import math

people = int(input())
taksa_vhod = float(input())
shezlong_cena = float(input())
chadyr_cena = float(input())

people_taxes = people * taksa_vhod
hora_iskashti_shezlong = math.ceil(75 / 100 * people)
hora_platili_shezlong = hora_iskashti_shezlong * shezlong_cena
hora_iskashti_chadyr=math.ceil(50 / 100 * people)
hora_platili_chadyr=hora_iskashti_chadyr*chadyr_cena

total=people_taxes+hora_platili_chadyr+hora_platili_shezlong
print(f'{total:.2f} lv.')

