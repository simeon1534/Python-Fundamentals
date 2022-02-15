path=input().split(f"{chr(92)}")

file=path[-1]
print(f"File name: {file.rpartition('.')[0]}")
print(f"File extension: {file.rpartition('.')[2]}")
