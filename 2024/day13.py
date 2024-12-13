from aocd import data

#data = open('day13test.txt', 'r').read()
machines = data.split('\n\n')


def calcPrize(ax, ay, bx, by, px, py, cx, cy, acount, bcount, minTokens, cache):
    if cache[acount][bcount] == 1 or cx > px or cy > py or acount > 100 or bcount > 100 or (acount*3 + bcount) > minTokens:
        return (minTokens, False)
    cache[acount][bcount] = 1
    if cx == px and cy == py and (acount*3 + bcount) < minTokens:
        return (acount*3 + bcount, True)
    pressATokens, successA = calcPrize(ax, ay, bx, by, px, py, cx+ax, cy+ay, acount+1, bcount, minTokens, cache)
    pressBTokens, successB = calcPrize(ax, ay, bx, by, px, py, cx+bx, cy+by, acount, bcount+1, minTokens, cache)
    if successA and successB:
        if pressATokens < pressBTokens:
            return (pressATokens, True)
        else:
            return (pressBTokens, True)
    if successA:
        return (pressATokens, True)
    return (pressBTokens, True)



def part1():
    resTokens = 0
    for machine in machines:
        cache = [[0 for _ in range(102)] for _ in range(102)]

        a, b, p = machine.split('\n')
        ax, ay = a.split(', ')
        ax = int(ax.split('+')[1])
        ay = int(ay.split('+')[1])
        
        bx, by = b.split(', ')
        bx = int(bx.split('+')[1])
        by = int(by.split('+')[1])

        px, py = p.split(', ')
        px = int(px.split('=')[1])
        py = int(py.split('=')[1])
        #print(ax, ay)
        #print(bx, by)
        #print(px, py)
        if ax*100 + bx*100 < px or ay*100 + by*100 < py:
            print("Skipping machine")
            continue
        tokens, success = calcPrize(ax, ay, bx, by, px, py, 0, 0, 0, 0, 400, cache)
        print(tokens, success)
        if success:
            resTokens += tokens

    print("Result:", resTokens)

part1()