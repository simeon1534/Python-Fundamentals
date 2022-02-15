array = input().split()
out = array[0]
for i in range(1, len(array)):
    out = int(out) ^ int(array[i])
print (str(out))