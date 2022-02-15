import math

# input

zaplata = float(input())
uspeh = float(input())
min_zaplata = float(input())

# dohodyt po-malyk li e ot min rabotna zaplata?

socialna_stipendiq = False
otl_stipendiq = False

if min_zaplata > zaplata and uspeh > 4.50:
    socialna_stipendiq = True
    socialna_stipendiq = min_zaplata * 0.35

# uspeha nad 5.50 li e?

if uspeh >= 5.50:
    otl_stipendiq = True
    otl_stipendiq = uspeh * 25

#if zaplata > min_zaplata and uspeh < 5.50:
 #   print('You cannot get a scholarship!')

# uchenika ima i dvete stipendii,ot koito poluchva po visokata
if socialna_stipendiq and otl_stipendiq:
    if socialna_stipendiq > otl_stipendiq:
     print(f'You get a Social scholarship {math.floor(socialna_stipendiq)} BGN')
    else:
     print(f'You get a scholarship for excellent results  {math.floor(otl_stipendiq)} BGN')
# print(f'You get a scholarship for excellent results {math.floor(otl_stipendiq)} BGN')
elif socialna_stipendiq :
    print(f'You get a Social scholarship {math.floor(socialna_stipendiq)} BGN')

elif otl_stipendiq :
    print(f'You get a scholarship for excellent results {math.floor(otl_stipendiq)} BGN')
else:
    print('You cannot get a scholarship!')
