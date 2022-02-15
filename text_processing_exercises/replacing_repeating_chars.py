text=input()

result=""
for i in range(0,len(text)):
    if not i==len(text)-1:
        if not  text[i]==text[i+1]:
            result+=text[i]
    elif i==len(text)-1:
        result += text[i]
print(result)

