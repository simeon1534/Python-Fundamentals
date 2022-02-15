def order(product,quantity):
    coffee=1.50
    water=1.00
    coke=1.40
    snacks=2.00
    result=0
    if product=='coffee':
        result=coffee*quantity
        return result
    elif product=='water':
        result=water*quantity
        return result
    elif product=='coke':
        result=coke*quantity
        return result
    elif product=='snacks':
        result=snacks*quantity
        return result

product=input()
quantity=int(input())
print(f'{order(product,quantity):.2f}')