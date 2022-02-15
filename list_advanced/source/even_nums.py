nums = [int(el) for el in input().split(', ')]
even_nums = [index for index in range(len(nums)) if nums[index] % 2 == 0 ]
print(even_nums)

# nums = list(map(int, input().split(', ')))
# even_nums = list(filter(lambda index: num[index] %2 == 0, range(len(nums))))