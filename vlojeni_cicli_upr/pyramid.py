num = int(input())  # 7
counter = 1
row_index = 0

while True:
    for col_index in range(row_index + 1):
        print(counter, end=" ")
        counter += 1
        if counter > num:
            break

    if counter > num:
        break
    row_index += 1
    print()
