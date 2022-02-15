import re

sequence=""
while True:
    data = input()
    sequence+=data
    if data=="":
        break
pattern = r"\d+"
nums = re.findall(pattern, sequence)

print(*nums)
