import string
import math

data = input().split()
result = 0


# def rounding(DECIMAL_PART):
#     round_down = ["1", "2", "3", "4"]
#     round_up = ["5", "6", "7", "8", "9"]
#     if str(DECIMAL_PART)[4] in round_up:
#         return 0.001
#     return 0


for sequence in data:
    chisloto = int(sequence[1:-1])
    if sequence[0].isupper():
        first_operation = chisloto / (int(string.ascii_lowercase.index(sequence[0].lower())) + 1)
        result += first_operation
    elif sequence[0].islower():
        first_operation = chisloto * (int(string.ascii_lowercase.index(sequence[0].lower())) + 1)
        result += first_operation

    if sequence[-1].isupper():
        first_operation = (int(string.ascii_lowercase.index(sequence[-1].lower())) + 1)
        result -= first_operation
    elif sequence[-1].islower():
        first_operation = int(string.ascii_lowercase.index(sequence[-1].lower())) + 1
        result += first_operation
decimal_part = abs(result - round(result))


print(f"{result:.2f}")
