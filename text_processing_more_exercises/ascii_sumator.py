char_1=input()
char_2=input()

nomer_char_1=ord(char_1)
nomer_char_2=ord(char_2)

string=input()
result=0
for char in string:
    if nomer_char_2>ord(char)>nomer_char_1:
        result+=ord(char)

print(result)

