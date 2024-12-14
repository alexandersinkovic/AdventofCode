from aocd import data

#data = open('day13test.txt', 'r').read()
machines = data.split('\n\n')

def calcTokens(incr):
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
        px = int(px.split('=')[1]) + incr
        py = int(py.split('=')[1]) + incr

        b = ((py*ax)-(px*ay))//((by * ax) - (bx*ay))
        if b == ((py*ax)-(px*ay))/((by * ax) - (bx*ay)):
            a = (py - (b * by)) // ay
            if a == (py - (b * by)) / ay:
                resTokens += a*3 + b
    print("Result:", resTokens)

def part1():
    calcTokens(0)


def part2():
    calcTokens(10000000000000)

part1()
part2()