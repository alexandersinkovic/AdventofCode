from collections import defaultdict
import time

#input = open("Day12_test.txt", "r").read().splitlines()
input = open("Day12_in.txt", "r").read().splitlines()


def getPossibleCombinations(possible, required, rangeidx):
    if len(required) > 0 and rangeidx == len(ranges) or len(possible) < len(required) or (len(required) > 0 and possible[0] > required[0]):
        return 0
    if (memory[len(possible), rangeidx]) >= 0:
        return memory[len(possible), rangeidx]
    if rangeidx == len(ranges) and len(required) == 0:
        memory[(len(possible), rangeidx)] = 1
        return 1
    combs = 0
    myRange = ranges[rangeidx]
    myidx = 0
    while myidx <= len(possible) - myRange:
        if (len(required) > 0 and possible[myidx] > required[0]):
            break
        fit = True
        fit = not(myidx+myRange < len(possible) and possible[myidx+myRange] == possible[myidx] + 1 and possible[myidx+myRange] in required)
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
    memory[(len(possible), rangeidx)] = combs
    return combs

def expandGears(gears):
    gears = '?'.join([gears for i in range(5)])
    return gears

def defaultValue():
    return -1
    

arrangements = 0
start = time.time()
for a in range(len(input)):
    line = input[a]
    gears, ranges = line.split(' ')
    gears = expandGears(gears)
    gears = [c for c in gears]
    ranges = [int(x) for x in ranges.split(',')*5]
    possible = []
    required = []
    for i in range(len(gears)):
        if gears[i] == '?':
            possible.append(i)
        if gears[i] == '#':
            possible.append(i)
            required.append(i)
    memory = defaultdict(defaultValue)
    res = getPossibleCombinations(possible, required, 0)
    arrangements += res
end = time.time()
print("Runtime: ", end-start)
print(arrangements)
