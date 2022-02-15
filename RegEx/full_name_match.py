import re

data=input()
pattern="\\b[A-Z][a-z]+\\s+[A-Z][a-z]+\\b"

names=re.findall(pattern,data)

print(" ".join(names))