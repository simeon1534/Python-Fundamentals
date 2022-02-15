two_words=input().split()

str1=two_words[0]
str2=two_words[1]

result_str1=[]
result_str2=[]

for char in str1:
    char=ord(char)
    result_str1.append(char)

for char in str2:
    char=ord(char)
    result_str2.append(char)

if len(result_str1)>len(result_str2):
    difference=len(result_str1)-len(result_str2)
    for i in range(0,difference):
        result_str2.append(1)
elif len(result_str1)<len(result_str2):
    difference=len(result_str2)-len(result_str1)
    for i in range(0,difference):
        result_str1.append(1)

final_result=0

for result_str1_char,result_str2_char in zip(result_str1,result_str2):
    final_result=final_result+(result_str1_char*result_str2_char)
# print(result_str1)
# print(result_str2)
print(final_result)