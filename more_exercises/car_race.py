numbers_list = list(map(int, input().split()))
finish_index = len(numbers_list) // 2
car1 = numbers_list[:finish_index]
car2 = numbers_list[finish_index + 1:]


def race(car):
    total_time = 0
    for time in car:
        total_time += time
        if time == 0:
            total_time *= 0.8
    return total_time


race(car1)
race(car2)

print(f"The winner is left with total time: {race(car1):.1f}" if race(car1) < race(
    car2) else f"The winner is right with total time: {race(car2):.1f}")
