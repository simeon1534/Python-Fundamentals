budget=float(input())
videocards_count=int(input())
processors_count=int(input())
ram_count=int(input())

cost_videocards=videocards_count*250
cost_processors=35/100*cost_videocards*processors_count
cost_ram=10/100*cost_videocards*ram_count

total=cost_videocards+cost_processors+cost_ram
if videocards_count>processors_count:
    total-=15/100*total

if budget<total:
    print(f'Not enough money! You need {total-budget:.2f} leva more!')
else:
    print(f'You have {budget-total:.2f} leva left!')
