import re
data=input()
#(?<=<title>).*(?=</title>)
pattern_title=r"(?<=<title>).*(?=</title>)"

match_title=re.findall(pattern_title,data)
print(f"Title: {''.join(match_title)}")

pattern_body=r"(?<=<body>).*(?=</body>)"
match_body=re.findall(pattern_body,data)
match_body=''.join(match_body)
#print(match_body)

pattern_content=r"<.*?>"
match_substings=re.findall(pattern_content,match_body)
#print(match_substings)

for substring in match_substings:
        match_body = match_body.replace(substring, " ")


match_body= match_body.replace("\\n",' ')
match_body= match_body.replace("\\t",' ')

match_content=match_body.split()
print(match_content)
print(f"Content: {' '.join(match_content)}")

