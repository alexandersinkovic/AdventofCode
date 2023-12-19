from copy import deepcopy

#input = open("Day19_test.txt", 'r').read()
input = open("Day19_in.txt", 'r').read()

transformations, input = input.split('\n\n')
input = input.splitlines()
myMap = {}

xmas = {'x': 0, 'm': 1, 'a': 2, 's': 3}

for t in transformations.splitlines():
    key, value = t.split('{')
    value = value[:len(value)-1]
    cases = value.split(',')
    tMap = []
    for c in cases:
        if len(c.split(':')) == 2:
            b, r = c.split(':')
            if len(b.split('<')) == 2:
                k, v = b.split('<')
                tMap.append([k, True, v, r])
            else:
                k, v = b.split('>')
                tMap.append([k, False, v, r])
        else:
            tMap.append(['d', True, 0, c])
    myMap[key] = tMap

def applyMap1(kv, node):
    t = myMap[node]
    for i in range(len(t)-1):
        letter, lower, val, dest = t[i]
        mv = kv[xmas[letter]]
        if not((int(mv) < int(val)) ^ lower):
            return dest
    return t[-1][3]

def part1():
    res = 0
    for line in input:
        line = line[1:len(line)-1]
        pairs = list(map(lambda x: x.split('=')[1], line.split(',')))
        node = 'in'
        while(node not in ['R', 'A']):
            node = applyMap1(pairs, node)
        if node == 'A':
            res += sum(map(lambda x: int(x), pairs))

def combinationsOfRanges(kvranges: list[int]):
    print(kvranges)
    res = 1
    for r in kvranges:
        res = res * (r[1] - r[0] + 1)
    return res

def applyMap2(kvranges: list[list[int]], node):
    if node == 'A':
        return combinationsOfRanges(kvranges)
    if node == 'R':
        return 0
    t = myMap[node]
    remainingRanges = deepcopy(kvranges)
    combinations = 0
    for i in range(len(t)):
        letter, lower, val, dest = t[i]
        if letter == 'd':
            if dest == 'A':
                combinations += combinationsOfRanges(remainingRanges)
            elif dest != 'R':
                combinations += applyMap2(remainingRanges, dest)
            break
        affectedRanges = deepcopy(remainingRanges)
        minr, maxr = remainingRanges[xmas[letter]]
        # max < als val oder min größer als val
        if lower:
            if maxr > int(val) and minr < int(val):
                affectedRanges[xmas[letter]] = [minr, int(val)-1]
                remainingRanges[xmas[letter]] = [int(val), maxr]
        else:
            if minr < int(val) and maxr > int(val):
                affectedRanges[xmas[letter]] = [int(val) + 1, maxr]
                remainingRanges[xmas[letter]] = [minr, int(val)]
        combinations += applyMap2(affectedRanges, dest)   
    return combinations

def part2():
    init = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    print(applyMap2(init, 'in'))
    #print(202643964449156)
    #print(124167549767307)
    
#print(part1())
part2()
