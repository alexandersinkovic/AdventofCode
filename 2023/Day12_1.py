from collections import defaultdict
import time

#input = open("Day12_test.txt", "r").read().splitlines()
input = open("Day12_in.txt", "r").read().splitlines()

#???#?????????# 1,6,4
#?????????????.#.. 4,3,1
#???????.??? 1,3
#?.????????.???????? 1,5,1,6


def getPossibleCombinations(possible, required, rangeidx):
    if (memory[len(possible), rangeidx]) >= 0:
        #print("MEMORY")
        #print(len(possible), rangeidx)
        #print(memory[len(possible), rangeidx])
        return memory[len(possible), rangeidx]
    if rangeidx == len(ranges) and len(required) == 0:
        memory[(len(possible), rangeidx)] = 1
        return 1
    if len(required) > 0 and rangeidx == len(ranges) or len(possible) < len(required) or (len(required) > 0 and possible[0] > required[0]):
        memory[(len(possible), rangeidx)] = 0
        return 0
    combs = 0
    myRange = ranges[rangeidx]
    #print(possible, required, rangeidx, myRange)
    myidx = 0
    while myidx <= len(possible) - myRange:
        if (len(required) > 0 and possible[myidx] > required[0]):
            break
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
    memory[(len(possible), rangeidx)] = combs
    return combs

def expandGears(gears):
    gears = '?'.join([gears for i in range(5)])
    return gears

def defaultValue():
    return -1

arrangements = 0
start = time.time()
for a in range(7,len(input)):
    if a%50 == 0:
        print(a)
    line = input[a]
    #print(line)
    gears, ranges = line.split(' ')
    gears = expandGears(gears)
    #print(gears)
    gears = [c for c in gears]
    #ranges = [int(x) for x in ranges.split(',')]
    ranges = ''.join([''.join(ranges.split(',')) for i in range(5)])
    ranges = [int(x) for x in ranges]
    #print(ranges)
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
    memory = defaultdict(defaultValue)
    res = getPossibleCombinations(possible, required, 0)
    #print(res)
    arrangements += res
end = time.time()
print("Runtime: ", end-start)
#print(memory)
print(arrangements)

#348217226263679 too high
#190408349368393601 also too high obviously