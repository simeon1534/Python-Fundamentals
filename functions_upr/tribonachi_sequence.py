def tribonachi_squence(n):
    result=[]
    real_result=''
    for i in range(n):
        if i==0:
            result.append(1)
        elif i==1:
            result.append(1)

        elif i==2:
            result.append(2)

        else:
            result.append(result[-1]+result[-2]+result[-3])
    for i in range(n):
        real_result+=f'{result[0+i]} '
    return(real_result)

    #return (' '.join(result))




tribonachi_counter = int(input())
print(tribonachi_squence(tribonachi_counter))
