string = input()
result = ""
temp_characters = ""

for index in range(len(string)):
    if index>0 and chr(48) <= string[index-1] <= chr(57) and chr(48) <= string[index] <= chr(57):
        pass
    else:
        if chr(48) <= string[index] <= chr(57):
            if index<len(string)-1:
                if chr(48) <= string[index+1] <= chr(57):
                    result += temp_characters.upper() * int(string[index]+string[index+1])
                    temp_characters = ""
                else:
                    result += temp_characters.upper() * int(string[index])
                    temp_characters = ""
            else:
                result += temp_characters.upper() * int(string[index])
                temp_characters = ""
        else:

            temp_characters += string[index]

# print(set(result))
print(f"Unique symbols used: {len(set(result))}")
print(result)
