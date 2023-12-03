from aoc_fetcher import get_data

input = get_data(2023, 3).splitlines()
#input = open('Day3_test.txt', 'r').read().splitlines()

res = 0

for y in range(len(input)):
    line = input[y]
    x= 0
    while(x < len(line)):
        if line[x].isnumeric():
            numlen = 1
            num = [line[x]]
            while (line[x+numlen].isnumeric()):
                num.append(line[x+numlen])
                numlen+=1
                if (x + numlen >= len(line)):
                    break
            if x - 1 >= 0 and line[x-1] != '.':
                res += int(''.join(num))
            if x + numlen < len(line) and line[x+numlen] != '.':
                res += int(''.join(num))
            for i in range(-1, numlen+1):
                if x + i < 0 or x + i >= len(line):
                    continue
                for j in range(-1, 2, 2):
                    if y + j < 0 or y + j >= len(input):
                        continue
                    if input[y+j][x+i] != '.':
                        res += int(''.join(num))
            x = x + numlen
        x += 1

print(res)