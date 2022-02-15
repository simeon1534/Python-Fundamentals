num = int(input())
p = int(input())
mask=~(1<<p)
result=num & mask
# result.insert(0,'0')
# result[-(bit+1)]='0'
print(result)
