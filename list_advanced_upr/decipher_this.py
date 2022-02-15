ciphered_message=input().split()
message=''
for single_word in ciphered_message:
    single_word_list=list(single_word)
    ascii=''
    word_from_message=[]
    for el in single_word_list:
        if 48 <= ord(el) < 58:
            ascii+=el
        else:
            word_from_message.append(el)
    word_from_message.insert(0,(chr(int(ascii))))
    word_from_message[1], word_from_message[-1] = word_from_message[-1], word_from_message[1]
    message+=f"{''.join(word_from_message)} "
print(message)
