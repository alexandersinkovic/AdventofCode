from aoc_fetcher import get_data

input = get_data(2023, 5).split('\n\n')
#input = open('Day5_test.txt', 'r').read().split('\n\n')

seeds = input[0].split(' ')[1::]
maps = input[1::]
maps = [sorted([list(map(lambda y: int(y), x.split(' '))) for x in m.split(':\n')[1].splitlines()], key= lambda x: int(x[1])) for m in maps]
lowest = -1
for seed in seeds:
    seed = int(seed)
    for i in range(len(maps)):
        m = maps[i]
        for j in range(len(m)):
            if m[j][1] <= seed and m[j][1] + m[j][2] > seed:
                seed = m[j][0] + (seed - m[j][1])
                break
    if lowest < 0 or lowest > seed:
        lowest = seed
print(lowest)