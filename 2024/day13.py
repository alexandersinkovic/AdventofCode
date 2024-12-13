from aocd import data

#data = open('day13test.txt', 'r').read()
machines = data.split('\n\n')

# a * x + b * y = p

def part1():
    resTokens = 0
    for machine in machines:

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
            #print("Skipping machine")
            continue
        possibleA = [a for a in range(0, 101) if (px - (a*ax)) % bx == 0 and (py - (a*ay)) % by == 0]
        ways = [[a, (px - (a*ax))/ bx] for a in possibleA if (px - (a*ax))/ bx == (py - (a*ay))/ by]
        #print(ax, ay)
        #print(bx, by)
        #print(px, py)
        #print(ways)
        ways = list(filter(lambda x: 0 <= x[1] <= 100, ways))
        #print(ways)
        if len(ways) >= 1:
            tokens = sorted(map(lambda x: x[0]*3 + x[1], ways))
            #print('tokens', tokens)
            #print(tokens[0])
            resTokens += tokens[0]

    print("Result:", resTokens)

part1()