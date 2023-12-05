from aoc_fetcher import get_data

input = get_data(2023, 5).split('\n\n')
#input = open('Day5_test.txt', 'r').read().split('\n\n')

ranges = input[0].split(' ')[1::]
ranges = [[int(ranges[r]), int(ranges[r+1])] for r in range(0, len(ranges), 2)]
maps = input[1::]
maps = [sorted([list(map(lambda y: int(y), x.split(' '))) for x in m.split(':\n')[1].splitlines()], key= lambda x: int(x[1])) for m in maps]

def getNewRanges(ranges, mymap):
    newranges = []
    for range in ranges:
        start, length = range
        i = 0
        while length > 0:
            if i == len(mymap):
                newranges.append([start, length])
                break
            if mymap[i][1] > start:
                if mymap[i][1] > start + length:
                    newlength = length
                    length = 0
                    newstart = start
                else:
                    newlength = mymap[i][1] - start
                    length = length - newlength
                    newstart = start
                    start = mymap[i][1]
                newranges.append([newstart, newlength])
            if mymap[i][1] <= start and mymap[i][1] + mymap[i][2] > start:
                newstart = mymap[i][0] + (start - mymap[i][1])
                newlength = 0
                if length >= (mymap[i][1] + mymap[i][2]) - start:
                    newlength = mymap[i][2] - (start - mymap[i][1])
                    start += newlength 
                    length -= newlength
                else:
                    newlength = length
                    length = 0
                newranges.append([newstart, newlength])
            i+=1
    return newranges

for m in maps:
    ranges = getNewRanges(ranges, m)
print(min([x[0] for x in ranges]))