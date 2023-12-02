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
    for i in range(len(games)):
        game = games[i].split(',')
        possible = True
        counter = [0, 0, 0]
        for j in range(len(game)):
            cubes = game[j].split(' ')
            c = int(cubes[1])
            color = colorMap[cubes[2]]
            counter[color] = c
        print(counter)
        possible = checker(counter)
        print(possible)
        if not possible:
            break
    if possible:
        res += int(id)
print(res)