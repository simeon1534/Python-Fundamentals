num=int(input())
p=int(input())
mask=7<<p
print("{0:b}".format(mask))
result=num^mask
print(result)