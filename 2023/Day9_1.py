from aoc_fetcher import get_data

input = get_data(2023, 9).splitlines()
#input = open('Day9_test.txt', 'r').read().splitlines()

histories = [list(map(lambda x: int(x), line.split(' '))) for line in input]

res = 0

for history in histories:
    steps = [history]
    curr = history
    while (sum(map(lambda x : x != 0, curr)) != 0):
        next = []
        for i in range(len(curr)-1):
            next.append(curr[i+1] - curr[i])
        steps.append(next)
        curr = next
    extrapol = 0
    #Part1
    #for i in range(2, len(steps)+1):
    #    extrapol = extrapol + steps[-i][-1]
    #Part 2
    for i in range(2, len(steps)+1):
        extrapol = steps[-i][0] - extrapol
    res += extrapol
print(res)