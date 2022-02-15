def multiplication_sign(x, y, z):
    negative = False
    if x == 0 or y == 0 or z == 0:
        return 'zero'



    if  (y < 0 and x < 0) or (y > 0 and x > 0):
        negative = False
        if z < 0:
            negative = True
    else:
        negative = True
        if z < 0:
            negative = False

    if negative == False:
        return 'positive'
    elif negative == True:
        return 'negative'

a=int(input())
b=int(input())
c=int(input())
print(multiplication_sign(a, b, c))