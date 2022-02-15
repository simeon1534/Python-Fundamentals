def data_type(type, value):
    if type == 'int':
        result = int(value) * 2
        return result

    elif type == 'real':
        result = f'{(int(value) * 1.5):.2f}'
        return result

    elif type == 'string':
        result = f'${value}$'
        return result

command=input()
data=input()
print(data_type(command,data))


