grade = float(input())


def grade_function(grade_real):
    if 1.99<grade_real < 3:
        return 'Fail'
    elif 3.50 > grade_real >= 3:
        return 'Poor'
    elif 4.50 > grade_real >= 3.50:
        return 'Good'
    elif 5.50 > grade_real >= 4.50:
        return 'Very Good'
    elif 6>=grade_real >= 5.50:
        return 'Excellent'

print(grade_function(grade))