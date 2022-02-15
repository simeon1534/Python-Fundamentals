n = int(input())
key_word = input()
unfiltered = []
filtered = []
for i in range(1, n + 1):
    text = input()
    unfiltered.append(text)
    text_splitted=text.split(' ')                # if key_word in text
    for index in range(0,len(text_splitted)):    # filtered.append(text)
        if text_splitted[index]==key_word:
            filtered.append(text)
print(unfiltered)
print(filtered)