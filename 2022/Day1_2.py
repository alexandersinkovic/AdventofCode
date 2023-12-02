from aoc_fetcher import get_data

input = get_data(2022, 1)

input = input.splitlines()

index = 0
calories = [0]
for cal in input:
    if cal == '':
        index += 1
        calories.append(0)
    else:
        calories[index] += int(cal)

calories = sorted(calories)
print(calories[-1] + calories[-2] + calories[-3])
