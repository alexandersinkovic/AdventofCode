from aoc_fetcher import get_data

input = get_data(2023, 2).splitlines()

colorMap = {'red': 0, 'green': 1, 'blue': 2}

def checker(cubes):
    return cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14

gameresults = []
res = 0


for line in input:
    line = line.split(':')
    id = line[0].split(' ')[1]
    games = line[1].split(';')
    counter = [0, 0, 0]
    for i in range(len(games)):
        game = games[i].split(',')
        for j in range(len(game)):
            cubes = game[j].split(' ')
            c = int(cubes[1])
            color = colorMap[cubes[2]]
            counter[color] = max(c, counter[color])
    gameresults.append(counter)

for g in gameresults:
    r = int(g[0]) * int(g[1]) * int(g[2])
    res += r

print(res)