key_sequence = input()
key_sequence=key_sequence.replace(" ","")

def decrypt_func(some_string):
    decrypted_text=""
    key = ""
    while len(key) < len(some_string):
        key += key_sequence
    for i in range(len(some_string)):
        decrypted_text+=chr(ord(some_string[i])-int(key[i]))
    return decrypted_text

data=input()
result=[]
while not data=="find":
    result.append(decrypt_func(data))
    data=input()

#print(result)

for i in result:
    treasure = i.split("&")[1]
    coordinate=i[i.index("<")+1:i.index(">")]
    print(f"Found {treasure} at {coordinate}")
   # print(treasure)
    #print(coordinate)