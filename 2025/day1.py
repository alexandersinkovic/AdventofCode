from aocd import get_data

DATA = get_data(day=1, year=2025).splitlines()
TEST = "L68,L30,R48,L5,R60,L55,L1,L99,R14,L82".split(',')

def p1():

    init = 50

    input = [int(x.replace('R', '')) % 100 for x in [y.replace('L', '-') for y in DATA]]

    count = 0

    for t in input:
        init = (init + t) % 100
        if init == 0:
            count += 1
    print(count)

def p2():
    init = 50

    input = [int(x.replace('R', '')) for x in [y.replace('L', '-') for y in DATA]]

    fullTurns = [int(abs(x / 100)) for x in input]

    input = [getLast2Digits(x) for x in input]


    res = sum(fullTurns)

    curr = init
    for idx, n in enumerate(input):
        next = curr + n
        if (curr > 0 and next <= 0) or next >= 100:
            res += 1
        curr = next % 100
    
    print(res)
    
    
def getLast2Digits(n):
    s = str(n)
    if len(s) <=2:
        return n
    if s[0] == '-':
        return int('-' + s[-2:])
    else:
        return n % 100

p2()