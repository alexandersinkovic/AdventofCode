from aocd import data

#data = open('day14test.txt', 'r').read()
robots = [l.split(' v=') for l in data.split('\n')]
Y = 103
YM = 51
X = 101
XM = 50
SECONDS = 100

def part1():
    q = [0,0,0,0]
    for robot in robots:
        rx, ry = robot[0].split(',')
        rx = int(rx.split('=')[1])
        ry = int(ry)

        vx, vy = robot[1].split(',')
        vx = int(vx)
        vy = int(vy)
        
        ry = (ry + vy * SECONDS) % Y
        rx = (rx + vx * SECONDS) % X

        if ry != YM and rx != XM:
            if ry > YM:
                if rx > XM:
                    q[3] += 1
                else:
                    q[2] += 1
            else:
                if rx > XM:
                    q[1] += 1
                else: 
                    q[0] += 1
    print(q[0], q[1], q[2], q[3])
    print(q[0] * q[1] * q[2] * q[3])

def part2():
    f = open('day14out.txt', 'w')
    for ridx in range(len(robots)):
        rx, ry = robots[ridx][0].split(',')
        rx = int(rx.split('=')[1])
        ry = int(ry)

        vx, vy = robots[ridx][1].split(',')
        vx = int(vx)
        vy = int(vy)
        robots[ridx] = [ry, rx, vy, vx]
            
    for s in range(SECONDS*100):
        if s % 1000 == 0:
            print('Simulating Second', s)
        bath = [['.' for _ in range(X)] for _ in range(Y)]
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % Y
            robot[1] = (robot[1] + robot[3]) % X

            bath[robot[0]][robot[1]] = '#'
        f.write('Second ' + str(s) + '\n')
        f.writelines([''.join(l) + '\n' for l in bath])
        f.write('\n')

part2()