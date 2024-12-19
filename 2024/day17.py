from aocd import data
import aoc_utils as au

#data = open('day17test.txt', 'r').read()
input = data.split('\n\n')
program = au.getIntFromString(input[1])
global A 
global B 
global C 
A, B, C = au.getIntFromString(input[0])

def parseCombo(com):
    values = [0, 1, 2, 3, A, B, C]
    return values[com]

#0
def adv(combo):
    com = parseCombo(combo)
    global A
    A = A // (2 ** com)

#1
def bxl(lit):
    global B
    B = B ^ lit

#2
def bst(combo):
    com = parseCombo(combo)
    global B
    B = com % 8

#3
def jnz(inst, lit):
    if A != 0:
        if inst != lit:
            return lit, 0
    return inst, 2

#4
def bxc():
    global B
    B = B ^ C

#5
def out(combo):
    com = parseCombo(combo)
    return com % 8

#6
def bdv(combo):
    global B
    com = parseCombo(combo)
    B = A // (2 ** com)

#7
def cdv(combo):
    global C
    com = parseCombo(combo)
    C = A // (2 ** com)

def part1(a):
    inst = 0
    output = []
    incr = 2
    while(inst < len(program)):
        opcode = program[inst]
        operand = program[inst+1]
        if (opcode == 0):
            adv(operand)
        elif (opcode == 1):
            bxl(operand)
        elif (opcode == 2):
            bst(operand)
        elif (opcode == 3):
            inst, incr = jnz(inst, operand)
        elif (opcode == 4):
            bxc()
        elif (opcode == 5):
            output.append(out(operand))
        elif (opcode == 6):
            bdv(operand)
        elif (opcode == 7):
            cdv(operand)
        inst += incr
        incr = 2
    print('Output for A =',a ,'=>', ','.join([str(c) for c in output]))
    print(','.join([str(c) for c in output]))
    print(A, B, C)
    return(output)

#Min = 35184372088832
#Max = 281474976710656
def part2():
    goal = program
    check = [0]
    for k in range(1,17):
        nextCheck = []
        for c in check:
            for i in range(c*8,(c+1)*8):
                global A
                A = i
                output = part1(i)
                if goal[-k:] == output:
                    nextCheck.append(i)
        check = nextCheck
    print(check)
#part1()
part2()

