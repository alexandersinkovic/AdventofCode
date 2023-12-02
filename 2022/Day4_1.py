from aoc_fetcher import get_data

input = get_data(2022, 4)

input = input.splitlines()
pairs = [pair.split(',') for pair in input]

count = 0

for pair in pairs:
    r1 = pair[0].split('-')
    r2 = pair[1].split('-')
    if int(r1[0]) >= int(r2[0]) and int(r1[1]) <= int(r2[1]):
        count += 1
    elif int(r1[0]) <= int(r2[0]) and int(r1[1]) >= int(r2[1]):
        count += 1

print(count)
