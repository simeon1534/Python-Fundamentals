# num=int(input())
# print(list("{0:b}".format(num))[-2])
num=int(input())
bit=(num>>1) & 1
print(bit)
