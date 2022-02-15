def password_function(password):
    password = list(password)
    result = ''
    digits = 0
    valid_password = True
    if len(password) > 10 or len(password) < 6:
        result += f"Password must be between 6 and 10 characters\n"
        valid_password = False
    for element in password:
        if ord(element) < 48 or 65 > ord(element) > 57 or 97 > ord(element) > 90 or ord(element) > 122:
            result += f"Password must consist only of letters and digits\n"
            valid_password = False
            break
    for digit in password:
        if 57 >= ord(digit) >= 48:
            digits += 1
    if digits < 2:
        result += f"Password must have at least 2 digits\n"
        valid_password = False
    if valid_password:
        result += f"Password is valid"
    return result


x = input()
print(password_function(x))
