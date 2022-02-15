lines_of_strings=int(input())

def name_years(string):

    name=string[string.index("@")+1:string.index("|")]
    years=string[string.index("#")+1:string.index("*")]

    print(f"{name} is {years} years old.")


for i in range (lines_of_strings):
    string=input()
    name_years(string)