num1=int(input())
num2=int(input())
result=list("{0:b}".format(num1))

print(result.count(str(num2)))
print(result)