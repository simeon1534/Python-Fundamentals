def char_in_range(a, b):
    c = ord(a)
    d = ord(b)
    i=None
    result=''
    for i in range(c + 1, d):
        result += chr(i)
        result+=' '
        #print(chr(i), end=' ')

    return result


x = input()
y = input()
print(char_in_range(x, y))
