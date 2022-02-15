n1 = int(input())
n2 = int(input())
operator = input()
n3 = 0
chetnost = 0
if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        n3 = n1 + n2
    elif operator == "-":
        n3 = n1 - n2
    elif operator == "*":
        n3 = n1 * n2
    if n3 % 2 == 0:
        chetnost = 'even'
    else:
        chetnost = 'odd'
    print(f"{n1} {operator} {n2} = {n3} - {chetnost}")
if operator == "/":

    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    if n2!=0:
        n3 = n1 / n2
        print(f'{n1} / {n2} = {n3:.2f}')
if operator == "%":

    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    if n2!=0:
        n3 = n1 % n2
        print(f"{n1} % {n2} = {n3}")
