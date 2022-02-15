# text=input()
#
#
# while not text=="":
#     if  ":" in text:
#         emoticon=text.find(":")
#         emoticon2=text.find(":")+1
#         #if not  text[emoticon2]==" " and not ord("0")<=ord(f"{text[emoticon2]}")<=ord("9") :
#         print(f"{text[emoticon]}{text[emoticon2]}")
#
#     #print(f"{text[emoticon2]}  {ord('0')} {ord(text[emoticon2])} {ord('9')}")
#         text=text.replace(text[:emoticon2+1],"")
#     else:
#         break

text = input()
for i in range(len(text)):
    if text[i] == ':':
        print(f":{text[i + 1]}")