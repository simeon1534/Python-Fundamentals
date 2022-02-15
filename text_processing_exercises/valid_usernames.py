names=input().split(", ")

def redundantSymbol_check(symbol):
    pass

for name in names:
    if len(name)>3 and len(name)<16:
        no_print=0
        for char in name:
            if char.isalpha()==True or char.isdigit() ==True or char=="-" or char =="_":
                pass
            else:
                no_print=True
                break
        if no_print!=True:
            print(name)


