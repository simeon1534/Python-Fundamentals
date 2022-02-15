import  re
data=input()
pattern=r"\bwww\.[a-zA-Z\d-]+\.[a-z]+(\.[a-z]+)*\b"


while not data=="":
    valid_links = re.finditer(pattern, data)
    for link in valid_links:
        print(link.group(0))
    data = input()



