#from aoc_fetcher import get_data
f = open("Day8_input.txt", "r")

#input = get_data(2022, 6)

input = [[int(c) for c in line[:-1:]] for line in f]
result = [[c for c in line] for line in input]
visible_trees = len(input) * 2 + len(input[0] * 2) - 4
print(visible_trees)

for y in range(1, len(input) - 1):
    for x in range(1, len(input[0]) - 1):
        tree = input[y][x]
        visible = False
        i = x - 1
        while(i > -1):
            if (input[y][i] >= tree):
                break
            if (i == 0):
                visible = True
            i -= 1
        i = x + 1
        while(i < len(input[0])):
            if (input[y][i] >= tree):
                break
            if (i == len(input[0]) - 1):
                visible = True
            i += 1
        i = y - 1
        while(i > -1):
            if (input[i][x] >= tree):
                break
            if (i == 0):
                visible = True
            i -= 1
        i = y + 1
        while(i < len(input)):
            if (input[i][x] >= tree):
                break
            if (i == len(input) - 1):
                visible = True
            i += 1

        if (visible):
            visible_trees += 1
        else:
            result[y][x] = '.'

print(visible_trees)
