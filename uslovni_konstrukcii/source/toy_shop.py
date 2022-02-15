holiday = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_sum = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
# suma_discount = suma - (suma * 0.25)
# discount =  suma * 0.25
total_toys = puzzles + dolls + bears + minions + trucks

if total_toys >= 50:
    total_sum -= total_sum * 0.25

total_sum -= total_sum * 0.1


if  total_sum  >= holiday:
    print(f'Yes! {total_sum  - holiday:.2f} lv left.')
elif total_sum  < holiday:
    nujni_pari = holiday - total_sum
    print(f'Not enough money! {nujni_pari:.2f} lv needed.')

