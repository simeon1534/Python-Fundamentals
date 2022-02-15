broi_vnoski = int(input())
counter = 1

total = 0

while counter <= broi_vnoski:
    vnoski = float(input())
    if vnoski>0:
        print(f'Increase: {vnoski:.2f}')
        counter += 1
        total += vnoski
    if vnoski<0:
        print("Invalid operation!" )
        break

print(f'Total: {total:.2f}')
