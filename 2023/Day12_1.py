#input = open("Day12_test.txt", "r").read().splitlines()
input = open("Day12_in.txt", "r").read().splitlines()

#???#?????????# 1,6,4
#?????????????.#.. 4,3,1


def getPossibleCombinations(possible, required, rangeidx):
    if rangeidx == len(ranges) and len(required) == 0:
        return 1
    if len(required) > 0 and rangeidx == len(ranges) or len(possible) < len(required) or (len(required) > 0 and possible[0] > required[0]):
        return 0
    combs = 0
    myRange = ranges[rangeidx]
    #print(possible, required, rangeidx, myRange)
    myidx = 0
    while myidx <= len(possible) - myRange:
        fit = True
        for i in range(0, myRange-1):
            if possible[myidx + i] + 1 != possible[myidx + i + 1]:
                fit = False
        if fit:
            fitted = possible[myidx: myidx+myRange:]
            newrequired = [f for f in required if f not in fitted]
            newpossible = []
            if myidx+myRange == len(possible) or possible[myidx+myRange-1] +1 != possible[myidx+myRange]:
                newpossible = possible[myidx+myRange::]
            else:
                newpossible = possible[myidx+myRange+1::]
            combs += getPossibleCombinations(newpossible, newrequired, rangeidx+1)
        myidx += 1
    return combs

def expandGears(gears):
    gears = '?'.join([gears for i in range(5)])
    return gears

arrangements = 0
for line in input:
    #print(line)
    gears, ranges = line.split(' ')
    #gears = expandGears(gears)
    gears = [c for c in gears]
    ranges = [int(x) for x in ranges.split(',')]
    #ranges = ''.join([''.join(ranges.split(',')) for i in range(5)])
    #ranges = [int(x) for x in ranges]
    print(ranges)
    possible = []
    required = []
    for i in range(len(gears)):
        if gears[i] == '?':
            possible.append(i)
        if gears[i] == '#':
            possible.append(i)
            required.append(i)
    #print(possible)
    #print(required)
    #print(gears, ranges)
    res = getPossibleCombinations(possible, required, 0)
    #print(res)
    arrangements += res
print(arrangements)

303,121,579,983,974