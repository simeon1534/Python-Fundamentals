n = int(input())
result=0
for i in range(1, n + 1):
    char = input()
    char_num=ord(char)
    result+=char_num

print(f'The sum equals: {result}')