n=int(input())
l=int(input())
for symbol_1 in range(1,n):
    for symbol_2 in range(1, n ):
        for symbol_3 in range (97,97+l):
            symbol_3_str=chr(symbol_3)
            for symbol_4 in range(97, 97 + l ):
                symbol_4_str = chr(symbol_4)
                for symbol_5 in range(1,n+1):
                    if symbol_5>symbol_1 and symbol_5>symbol_2:
                        print(f'{symbol_1}{symbol_2}{symbol_3_str}{symbol_4_str}{symbol_5}', end=' ')



            

