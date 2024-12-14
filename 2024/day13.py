from aocd import data

#data = open('day13test.txt', 'r').read()
machines = data.split('\n\n')

# a * x + b * y = p

def checkInt(n):
    n = n % 1
    return n >= 0.9999 or n <= 0.0002
    


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
        #if ax*100 + bx*100 < px or ay*100 + by*100 < py:
        #    print("Skipping machine")
        #    continue
        #possibleA = [a for a in range(0, 101) if (px - (a*ax)) % bx == 0 and (py - (a*ay)) % by == 0]
        #ways = [[a, (px - (a*ax))/ bx] for a in possibleA if (px - (a*ax))/ bx == (py - (a*ay))/ by]
        #mathA = ((px/ax)-((py * bx)/(ax * by))) / (1 + ((ay * bx) / (ax * by)))
        #b = ((py/ay)-(px/ax))//((by/ay) - (bx/ax))
        b = ((py*ax)-(px*ay))//((by * ax) - (bx*ay))
        if b == ((py*ax)-(px*ay))/((by * ax) - (bx*ay)):
            a = (py - (b * by)) // ay
            if a == (py - (b * by)) / ay:
                resTokens += a*3 + b
        #print(ax, ay)
        #print(bx, by)
        #print(px, py)
        #print(round(a))
        #print(round(b))
        #print(round(a) * round(b))
        #print(a, b)
        #if (0 <= round(a) <= 100 and 0 <= round(b) <= 100 and checkInt(a)):
        #if (0 <= round(a)*3 + round(b) <= 400 and checkInt(a)):
        #if (checkInt(a)):
        #    resTokens += round(a)*3 + round(b)
        #print(mathA * ax + mathB * bx)
        #print(ways)
        #ways = list(filter(lambda x: 0 <= x[1] <= 100, ways))
        #print(ways)
        #if len(ways) >= 1:
        #    tokens = sorted(map(lambda x: x[0]*3 + x[1], ways))
            #print('tokens', tokens)
        #    print(tokens[0])
        #    resTokens += tokens[0]
        #if (0 <= round(a) <= 100 and 0 <= round(b) <= 100 and checkInt(a) and tokens[0] != round(a)*3 + round(b)):
        #    print('Error, ', ax, ay, bx, by, px, py, a, b, ways)

    print("Result1:", resTokens)

def part2():
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
        px = int(px.split('=')[1]) + 10000000000000
        py = int(py.split('=')[1]) + 10000000000000

        b = ((py*ax)-(px*ay))//((by * ax) - (bx*ay))
        if b == ((py*ax)-(px*ay))/((by * ax) - (bx*ay)):
            a = (py - (b * by)) // ay
            if a == (py - (b * by)) / ay:
                resTokens += a*3 + b

    print("Result2:", resTokens)

part1()
part2()

# a* (ax) + b * (bx) = (px)  
# a* (ay) + b * (by) = (py)

# a = (px - (b*bx)) / ax
# b = py - (a*ay)/ by