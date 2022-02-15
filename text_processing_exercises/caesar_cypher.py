text=input()
result=""
for char in text:
    encrypted_char=chr(ord(char) + 3)
    result+=encrypted_char
print(result)