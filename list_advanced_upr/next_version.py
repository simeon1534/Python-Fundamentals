version_list=input().split(".")
result=''.join(version_list)

print('.'.join(str(int(result) + 1)))