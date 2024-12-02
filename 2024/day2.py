from aoc_fetcher import get_data

input = get_data(2024, 2).splitlines()
#f = open('day2in.txt', 'r')
#f = open('day2test.txt', 'r')
#input = [line[:-1:] for line in f]
input = [[int(c) for c in line.split(' ')] for line in input]

def getMonotonie(l):
    return [l1 > l2 for l1, l2 in zip(l[:-1], l[1:])]
    

def getDifferences(l):
    return [abs(l1 - l2) for l1, l2 in zip(l[:-1], l[1:])]

def removeError(l: list[int], isAscending):
    m = getMonotonie(l)
    l.pop(m.index(isAscending)+1)
    return l
    
def checkSafety(line):
    monotonie = getMonotonie(line)
    isMonoton = 0 == sum(monotonie) or len(line)-1 == sum(monotonie)
    differences = getDifferences(line)
    return isMonoton and max(differences) <= 3 and min(differences) >= 1

def part1(line):
    safe = 0

    for line in input:
        monotonie = getMonotonie(line)
        isMonoton = 0 == sum(monotonie) or len(line)-1 == sum(monotonie)
        differences = getDifferences(line)
        if isMonoton and max(differences) <= 3 and min(differences) >= 1:
            safe += 1
    print(safe)

def part2():
    safe = 0
    for line in input:
        if checkSafety(line):
            safe += 1
        else:
            for i in range(len(line)):
                linecopy = [line[x] for x in range(len(line)) if x != i]
                if checkSafety(linecopy):
                    safe += 1
                    break
            
    print(safe)
        

#part1()
part2()