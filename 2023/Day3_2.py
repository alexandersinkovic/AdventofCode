from aoc_fetcher import get_data

input = get_data(2023, 3).splitlines()
#input = open('Day3_test.txt', 'r').read().splitlines()

res = 0

control = [[c for c in ('.'*len(input[0]))]for k in range(len(input))]

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
            num = int(''.join(num))
            for a in range(0, numlen):
                control[y][x+a] = num
            x = x + numlen
        x += 1

for y in range(len(input)):
    line = input[y]
    x= 0
    for x in range(len(line)):
        if line[x] == '*':
            nums = set()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if control[y+i][x+j] != '.':
                        nums.add(control[y+i][x+j])
            lnums = list(nums)
            if len(lnums) == 2:
                res += lnums[0] * lnums[1]
                
print(res)