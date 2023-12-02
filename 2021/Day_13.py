from aoc_fetcher import get_data

input = get_data(2021, 13)
#input = open('Day_13_testInput.txt').read()


def part1():
    data, folds = input.split('\n\n')
    data = [[int(x) for x in line.split(',')] for line in data.split()]
    folds = folds.split()[2::3]
    picture = []
    for r in range(0, 895):
        picture.append(['.' for _ in range(0, 1311)])
    #print(picture)
    for x, y in data:
        #print(x, y)
        picture[y][x] = '#'
    #print()
    #print(picture)
    for x, y in data:
        if x >= 655:
            picture[y][655 - (x - 655)] = '#'
    #print()
    #print(picture)
    picture = [line[:655] for line in picture]
    #print()
    #print(picture)
    count = 0
    for line in picture:
        for x in line:
            if x == '#':
                count += 1
    print(count)

def part2():
    data, folds = input.split('\n\n')
    data = [[int(x) for x in line.split(',')] for line in data.split()]
    folds = folds.split()[2::3]
    picture = []
    for r in range(0, 895):
        picture.append(['.' for _ in range(0, 1311)])
    for x, y in data:
        picture[y][x] = '#'
    for fold in folds:
        #print(picture)
        axis, thr = fold.split('=')
        thr = int(thr)
        if axis == 'x':
            for x, y in data:
                if x >= thr:
                    #print(x, y)
                    #print(thr)
                    #print(thr - (x - thr))
                    picture[y][thr - (x - thr)] = '#'
                    data.append([thr - (x - thr), y])
            picture = [line[:thr] for line in picture]
            data = list(filter(lambda point: point[0] < thr, data))
        else:
            for x, y in data:
                if y >= thr:
                    picture[thr - (y - thr)][x] = '#'
                    data.append([x, thr - (y - thr)])
            picture = picture[:thr]
            #print(data)
            #print('Filter:')
            data = list(filter(lambda point: point[1] < thr, data))
            #print(data)
            #[print(line) for line in picture]
    [print(''.join(line)) for line in picture]

part2()
