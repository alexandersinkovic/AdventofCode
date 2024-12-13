from aocd import data

#data = open('day13test.txt', 'r').read()
machines = data.split('\n\n')

# a * x + b * y = p

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
        if ax*100 + bx*100 < px or ay*100 + by*100 < py:
            print("Skipping machine")
            continue
        possibleA = [a for a in range(0, 101) if (px - (a*ax)) % bx == 0 and (py - (a*ay)) % by == 0]
        ways = [[a, (px - (a*ax))/ bx] for a in possibleA]
        if len(ways) > 1:
            print(ax, ay)
            print(bx, by)
            print(px, py)
            print(ways)
            ways = list(filter(lambda x: 0 <= x[1] <= 100, ways))
            print(ways)
            if len(ways) >= 1:
                tokens = sorted(map(lambda x: x[0]*3 + x[1], ways))
                print('tokens', tokens)
                resTokens += tokens[0]
        #tokens, success = calcPrize(ax, ay, bx, by, px, py, 0, 0, 0, 0, 400, cache)
        #print(tokens, success)
        #if success:
        #    resTokens += tokens

    print("Result:", resTokens)

part1()