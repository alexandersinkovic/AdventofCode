from collections import defaultdict
import time

#input = open("Day12_test.txt", "r").read().splitlines()
input = open("Day12_in.txt", "r").read().splitlines()

#???#?????????# 1,6,4
#?????????????.#.. 4,3,1
#???????.??? 1,3
#?.????????.???????? 1,5,1,6

#'#.???#?##.????.?#.???#?##.????. 1,1,2,1,1,1,2,1
#                                 0,1,2,3,4,5,6,7

# #  .  ?  ?  ?  ?  ? ? ? # . ? ? ? ? ? ?   1,1,2,1,1,2
#15,   14,13,12,11,10,9,8,7,  6,5,4,3,2,1   0,1,2,3,4,5

#.???????#.??????
#----------------
#xxxxxxx987 654321
##.#.##.#.#.##....
##.#.##.#.#..##...
##.#.##.#.#...##..
##.#.##.#.#....##.
##.#.##.#.#.....##
#5,
##.#.##...#.#.##..
##.#.##...#.#..##.
##.#.##...#.#...##
##.#.##...#..#.##.
##.#.##...#..#..##
##.#.##...#...#.##
#6
##.#..##..#.#.##..
##.#..##..#.#..##.
##.#..##..#.#...##
##.#..##..#..#.##.
##.#..##..#..#..##
##.#..##..#...#.##
#6
##.#...##.#.#.##..
##.#...##.#.#..##.
##.#...##.#.#...##
##.#...##.#..#.##.
##.#...##.#..#..##
##.#...##.#...#.##
##.#.....##.#.#.##
#7
##..#.##..#.#.##..
##..#.##..#.#..##.
##..#.##..#.#...##
##..#.##..#..#.##.
##..#.##..#..#..##
##..#.##..#...#.##
##..#..##.#.#.##..
##..#..##.#.#..##.
##..#..##.#.#...##
##..#..##.#..#.##.
##..#..##.#..#..##
##..#..##.#...#.##
##..#....##.#.#.##
##...#.##.#.#.##..
##...#.##.#.#..##.
##...#.##.#.#...##
##...#.##.#..#.##.
##...#.##.#..#..##
##...#.##.#...#.##
##...#...##.#.#.##
##....#..##.#.#.##
##.....#.##.#.#.##
#22
#22, 7, 6, 6, 5
#29, 17
#46

def getPossibleCombinations(possible, required, rangeidx):
    #print("call ", len(possible), rangeidx)
    if len(required) > 0 and rangeidx == len(ranges) or len(possible) < len(required) or (len(required) > 0 and possible[0] > required[0]):
        #memory[(len(possible), rangeidx)] = 0
        return 0
    if (memory[len(possible), rangeidx]) >= 0:
        #print(len(possible), rangeidx)
        #print('MEMORY ', memory[len(possible), rangeidx])
        return memory[len(possible), rangeidx]
    if rangeidx == len(ranges) and len(required) == 0:
        memory[(len(possible), rangeidx)] = 1
        return 1
    combs = 0
    myRange = ranges[rangeidx]
    #print(possible, required, rangeidx, myRange)
    myidx = 0
    while myidx <= len(possible) - myRange:
        #print(myidx)
        if (len(required) > 0 and possible[myidx] > required[0]):
            #print("required zahl not matched")
            break
        fit = True
        fit = not(myidx+myRange < len(possible) and possible[myidx+myRange] == possible[myidx] + 1 and possible[myidx+myRange] in required)
        #print("fit ", fit, myRange)
        for i in range(0, myRange-1):
            if possible[myidx + i] + 1 != possible[myidx + i + 1]:
                fit = False
        #print("fit ", fit)
        if fit:
            fitted = possible[myidx: myidx+myRange:]
            #print(rangeidx, myidx, fitted)
            newrequired = [f for f in required if f not in fitted]
            newpossible = []
            #print(fitted, newrequired)
            if myidx+myRange == len(possible) or possible[myidx+myRange-1] +1 != possible[myidx+myRange]:
                newpossible = possible[myidx+myRange::]
            else:
                newpossible = possible[myidx+myRange+1::]
            #print(newpossible, len(newpossible), newrequired, rangeidx+1, memory[(len(newpossible), rangeidx+1)])
            x = getPossibleCombinations(newpossible, newrequired, rangeidx+1)
            #print('Rekursion return')
            #print("combs: ", combs, "+ ", x, " x")
            combs += x
            #if len(possible) == 11:
            #    print("Combs")
            #    print(combs-x, x)
        myidx += 1
    #print(len(possible), rangeidx)
    #print("Return combs: ", combs, "für", len(possible), rangeidx)
    #if combs > 1:
    #    print(len(possible), rangeidx, combs)
    memory[(len(possible), rangeidx)] = combs
    return combs

def expandGears(gears):
    gears = '?'.join([gears for i in range(5)])
    return gears

def defaultValue():
    return -1

#def checkPoss(poss, req, gear):
    

arrangements = 0
start = time.time()
for a in range(len(input)):
    #if a%50 == 0:
    #    print(a)
    line = input[a]
    #print(line)
    gears, ranges = line.split(' ')
    gears = expandGears(gears)
    #print(gears)
    gears = [c for c in gears]
    #ranges = [int(x) for x in ranges.split(',')]
    ranges = [int(x) for x in ranges.split(',')*5]
    #print(ranges)
    #print(gears)
    possible = []
    required = []
    for i in range(len(gears)):
        if gears[i] == '?':
            possible.append(i)
        if gears[i] == '#':
            possible.append(i)
            required.append(i)
    #print(possible)
    #possible = checkPoss(possible, required, gears[0])
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

#TEST
#32
#2787504
#728086
#921999479
#1831120
#2402950
#512
#1024
#80000
#14406

#929845113

#348217226263679 too high
#1738259948652
#190408397248495573
#2607299733186757
#190408349368393601 also too high obviously