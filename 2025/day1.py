from aocd import get_data

DATA = get_data(day=1, year=2025).splitlines()

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

    #test = [list(x) for x in list(zip(input, fullTurns))]

    #for x in test:
    #    x.append(getLast2Digits(x[0]))

    input = [getLast2Digits(x) for x in input]


    res = sum(fullTurns)

    curr = init
    for idx, n in enumerate(input):
        curr = curr + n
        #test[idx].append(curr)
        if curr <= 0 or curr >= 100:
            res += 1
        curr = curr % 100
    
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