n=int(input())
for num_1 in range (1,10):
    if n%num_1==0:
        for num_2 in range(1, 10):
            if n % num_2 == 0:
                for num_3 in range(1, 10):
                    if n % num_3 == 0:
                        for num_4 in range(1, 10):
                            if n % num_4 == 0:
                                print(f'{num_1}{num_2}{num_3}{num_4}' , end=' ')

