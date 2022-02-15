fav_book=input()
counter=0
while True:
    book=str(input())
    if book==fav_book:
        print(f'You checked {counter} books and found it.')
        break
    elif book=='No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
        break

    counter += 1

