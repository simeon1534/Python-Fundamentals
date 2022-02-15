n = int(input())
prime=False
if n == 1:
    print('False')
else:

        if n % 2 != 0:

            if n % 3 != 0:

                if n % 5 != 0:
                    prime = True

if prime:
    print(f'True')
else:
    print(f'False')