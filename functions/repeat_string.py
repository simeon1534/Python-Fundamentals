
def repeat_string(randomstring, count):
    i = None
    for i in range(1, count ):
        print(randomstring, end='')

    return randomstring



string = input()
repeat_count = int(input())

print(repeat_string(string,repeat_count))
