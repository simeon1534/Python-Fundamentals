def odd_even_sum(a):
    odd = 0
    even = 0

    for count,element in enumerate(a):

        if count % 2 != 0:
            even += int(element)
        elif count % 2 == 0:
            odd += int(element)
    result= f'Odd sum = {odd}, Even sum = {even}'
    return result
x=input()
print(odd_even_sum(x))

