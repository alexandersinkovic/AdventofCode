input = open("Day19_test.txt", 'r').read()
#input = open("Day19_in.txt", 'r').read()

transformations, input = input.split('\n\n')
input = input.splitlines()
# key -> {letter -> [lower, value, dest]}
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

def applyMap2(kvranges: list[list[int]], node):
    t = myMap[node]
    for i in range(len(t)-1):
        letter, lower, val, dest = t[i]
        mvranges = kvranges[xmas[letter]]
        resranges = [j for j in kvranges]
        resranges[xmas[letter]] = []
        for r in mvranges:
            minr, maxr = r
            # max < als val oder min größer als val
            if not((maxr < int(val)) ^ lower) or not((minr > int(val)) ^ lower):
                resranges[xmas[letter]].append(r)
            else:
                #range aufteilen
                pass
            
    return t[-1][3]

def part2():
    init = [[0, 4000], [0, 4000], [0, 4000], [0, 4000]]
    print(applyMap2(init, 'in'))
    
#print(part1())
