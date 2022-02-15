text = input()
left_strength = 0
for i in range(len(text)):
    first_part=0
    second_part=0

    if text[i] == '>':
        strength = int(text[i + 1])
        text = text.replace(text[i + 1], " ", 1)
        left_strength = left_strength + (strength - 1)
    if not text[i] == '>' and left_strength>0 and not text[i]==" ":
        first_part=text[:i]
        second_part=text[i:]
        second_part = second_part.replace(text[i], " ", 1)
        text=first_part+second_part
        left_strength -= 1

result=text.split(" ")
print("".join(result))


