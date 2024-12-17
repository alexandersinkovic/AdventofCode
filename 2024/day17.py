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
        #print(inst, opcode, operand)
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
            output.append(str(out(operand)))
        elif (opcode == 6):
            bdv(operand)
        elif (opcode == 7):
            cdv(operand)
        inst += incr
        incr = 2
    print('Output for A =',a ,'=>', ','.join(output))
    print(','.join(output))
    print(A, B, C)

#Min = 35184372088832
#Max = 281474976710656
def part2():
    for i in range(8,64):
        global A
        A = i
        part1(i)
    print(','.join([str(p) for p in program]))
#part1()
#part2()

# A % 8 => B ^ 011 => A // 2 ^^ 3 => 011 ^ 101 => A // 8 => B ^ C => Output B%8 => Go again
# B = A % 8 => 
# B =.. => 
# C = A // 2^B => 
# B =.. => 
# A = A//8 => 
# B = B ^ C
# Output

# XOR 3
# 000 => 011, 0, 3
# 001 => 010, 1, 2
# 010 => 001, 2, 1
# 011 => 000, 3, 0
# 100 => 111, 4, 7
#...

# XOR 5
# 000 => 101, 0, 5
# 001 => 100, 1, 4
# 010 => 111, 2, 7
# 011 => 110, 3, 6
# 100 => 001, 4, 1
# 101 => 000, 5, 0
# 110 => 011, 6, 3
# 111 => 010, 7, 2
print(9 ^ 11)