first_num=int(input())
second_num=int(input())

for num in range(first_num,second_num+1):
    num_as_str=str(num)

    even_sum=0
    odd_sum=0

    for index,digits in enumerate(num_as_str):
        if index%2==0:
            even_sum+=int(digits)
        else:
            odd_sum+=int(digits)
    if even_sum==odd_sum:
        print(num, end=' ')
