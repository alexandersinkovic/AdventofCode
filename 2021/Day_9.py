from aoc_fetcher import get_data

input = get_data(2021, 9)
#input = open("Day_9_testInput.txt").read()

def part1():
    data = [[int(x) for x in line] for line in input.splitlines()]
    #print(data[-5:])

    risks = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            up_larger = False
            right_larger = False
            down_larger = False
            left_larger = False
            #print("Height:", data[i][j])
            #print(i-1,  0, data[i-1][j], data[i][j])
            if i-1 < 0 or data[i-1][j] > data[i][j]:
                up_larger = True
            if i+1 >= len(data) or data[i+1][j] > data[i][j]:
                down_larger = True
            if j-1 < 0 or data[i][j-1] > data[i][j]:
                left_larger = True
            if j+1 >= len(data[0]) or data[i][j+1] > data[i][j]:
                right_larger = True
            if up_larger and right_larger and left_larger and down_larger:
                #print(i, j)
                risks.append(data[i][j] + 1)

                #print("reached 1")
            #print(i+1,  len(data), data[i+1][j], data[i][j])
                #print("reached 2")
            #print(j-1,  0, data[i][j-1], data[i][j])
                #print("reached 3")
            #print(j+1,  len(data), data[i][j+1], data[i][j])
                #print("reached 4")
    print(sum(risks))

def part2():
    data = [[x for x in line] for line in input.splitlines()]
    map = [[x for x in line] for line in input.splitlines()]

    basin_sizes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '9' or map[i][j] == '#':
                continue
            basin_sizes.append(rec_search(i, j, 0, len(data), len(data[0]), map))
            #print(basin_sizes[-1])
            #for line in map:
                #print(''.join(line))

    #print(basin_sizes)
    #print(sorted(basin_sizes))
    res = sorted(basin_sizes)
    print(res[-1] * res[-2] * res[-3])

def rec_search(i, j, basin_size, height, width, map):
    if map[i][j] == '#' or map[i][j] == '9':
        #print(i, j, "rec-end: 0")
        return basin_size
    #print("Found valid coordinates: i=", i, ",j=", j)
    basin_size += 1
    map[i][j] = '#'
    if i-1 >= 0:
        #print("i-1")
        basin_size = rec_search(i-1, j, basin_size, height, width, map)
    if i+1 < height:
        #print("i+1")
        basin_size = rec_search(i+1, j, basin_size, height, width, map)
    if j-1 >= 0:
        #print("j-1")
        basin_size = rec_search(i, j-1, basin_size, height, width, map)
    if j+1 < width:
        #print("j+1")
        basin_size = rec_search(i, j+1, basin_size, height, width, map)
    #print(basin_size)
    return basin_size


#part1()
part2()
