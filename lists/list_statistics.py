numbers = int(input())

result_positive = []
result_negative = []
negative_sum = 0
for i in range(1, numbers + 1):
    number = int(input())
    if number >= 0:
        result_positive.append(number)
    else:
        result_negative.append(number)
        negative_sum += number

print(result_positive)
print(result_negative)
print(f'Count of positives: {len(result_positive)}. Sum of negatives: {negative_sum}')  # sum(result_negative)
