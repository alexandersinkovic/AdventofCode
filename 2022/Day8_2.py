#from aoc_fetcher import get_data
f = open("Day8_input.txt", "r")

#input = get_data(2022, 6)

input = [[int(c) for c in line[:-1:]] for line in f]
result = [[c for c in line] for line in input]
scenic_score = 1
max = 0

for y in range(0, len(input)):
    for x in range(0, len(input[0])):
        tree = input[y][x]
        i = 1
        while(x - i > 0 and input[y][x - i] < tree):
            i += 1
        scenic_score = scenic_score * i
        i = 1
        while(x + i < len(input[0]) - 1 and input[y][x + i] < tree):
            i += 1
        scenic_score = scenic_score * i
        i = 1
        while(y - i > 0 and input[y - i][x] < tree):
            i += 1
        scenic_score = scenic_score * i
        i = 1
        while(y + i < len(input) - 1 and input[y + i][x] < tree):
            i += 1
        scenic_score = scenic_score * i

        result[y][x] = scenic_score
        if (max < scenic_score):
            max = scenic_score
        scenic_score = 1


print(max)
