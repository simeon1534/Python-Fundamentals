
film=input()

standard_tickets=0
student_tickets=0
kid_tickets=0

#total_tickets_all=0
#total_tickets_1_cinema=0
while film !='Finish':
    svobodni_mesta=int(input())
    sold_tickets=0
    tickets = input()
    while tickets!='End':
        sold_tickets+=1
        if tickets == 'standard':
            standard_tickets += 1
        elif tickets == 'student':
            student_tickets += 1
        elif tickets == 'kid':
            kid_tickets += 1
        if sold_tickets==svobodni_mesta:
            break

        tickets = input()


    print(f'{film} - {(sold_tickets / svobodni_mesta) * 100:.2f}% full.')
    film=input()

total=standard_tickets+student_tickets+kid_tickets
print(f'Total tickets: {total}')
print(f'{student_tickets / total*100:.2f}% student tickets.')
print(f'{standard_tickets / total*100:.2f}% standard tickets.')
print(f'{kid_tickets / total*100:.2f}% kids tickets.')


