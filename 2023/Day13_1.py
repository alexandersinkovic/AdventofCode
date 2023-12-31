from aoc_fetcher import get_data

input = get_data(2023, 13)
#input = open("Day13_test.txt", "r").read()

def checkReflection(a, b):
    for i in range(len(a)):
        if (a[i] != b[i]):
            return False
    return True

def checkReflectionB(a, b):
    return sum(map(lambda x, y: x != y, a, b))


res = 0

patterns = [x.split('\n') for x in input[:len(input)-1].split('\n\n')]
for pattern in patterns:
    refFound = False
    #check horizontal

    for i in range(len(pattern)-1):
        j = 0
        horRef = 0
        while i - j >= 0 and i + j < len(pattern)-1:
            #horRef = horRef and checkReflection(pattern[i-j], pattern[i+j+1])
            horRef += checkReflectionB(pattern[i-j], pattern[i+j+1])
            j += 1
        if horRef == 1:
            res += (i+1)*100
            refFound = True
            break

    #check vertical
    if not refFound:
        for i in range(len(pattern[0])-1):
            j = 0
            verRef = 0
            while i - j >= 0 and i + j < len(pattern[0])-1:
                col1 = [pattern[x][i-j] for x in range(len(pattern))]
                col2 = [pattern[x][i+j+1] for x in range(len(pattern))]
                verRef += checkReflectionB(col1, col2)
                j+= 1
            if verRef == 1:
                res +=i+1
                break
print(res)