data=input().split()

result=""

for word in data:
    result+=word * len(word)

print(result)
print("".join([el * len(el) for el in data]))