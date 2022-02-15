import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
nums=re.finditer(pattern,data)

nums=[n.group(0) for n in nums]

print(*nums)