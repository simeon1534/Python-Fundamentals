import re

data = input()
pattern = r"(?<=\b_)[a-zA-Z\d]+\b"
variables = re.findall(pattern, data)
print(','.join(variables))

