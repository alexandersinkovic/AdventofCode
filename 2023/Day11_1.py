from aoc_fetcher import get_data

input = get_data(2023, 11).splitlines()
#input = open('Day11_test.txt', 'r').read().splitlines()

def has_galaxy(listOfStars):
    for c in listOfStars:
        if c == '#':
            return True
    return False

def calcExp(isX, a, b):
    res = 0
    if isX:
        return len(list(filter(lambda x: a < x < b, xexp))) #* 999999 # part2
    else:
        return len(list(filter(lambda y: a < y < b, yexp))) #* 999999 # part2

yexp = []
xexp = []
for y in range(len(input)):
    if not has_galaxy(input[y]):
        yexp.append(y)
for x in range(len(input[0])):
    myList = [input[y][x]for y in range(len(input))]
    if not has_galaxy(myList):
        xexp.append(x)

galaxies = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == '#':
            galaxies.append((y,x))

res = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        y1, x1 = galaxies[i]
        y2, x2 = galaxies[j]
        xinc = 0
        if x2 > x1:
            xinc = calcExp(True, x1, x2)
        else:
            xinc = calcExp(True, x2, x1)
        res += abs(y2 - y1) + abs(x2 - x1) + calcExp(False, y1, y2) + xinc
print(res)