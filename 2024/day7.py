#from aocd import data
from itertools import combinations_with_replacement
import math
import time

#data = data.split('\n')

f = open('day7in.txt', 'r').read()
#f = open('day7test.txt', 'r').read()
input = f.split('\n')

def test_equation(res, nums, use_binary):
    n = len(nums)-1
    if use_binary:
        ops = get_binary(n)
    else:
        ops = get_ternary(n)
    for op in ops:
        carry = nums[0]
        for i in range(len(op)):
            carry = sum_or_mul(carry, nums[i+1], op[i])
            if carry > res:
                break
        if res == carry:
            return True
    return False

def sum_or_mul(a, b, op):
    if op == '1':
        return a * b
    if op == '2':
        return int(str(a)+str(b))
    return a+b

def get_binary(exp):
    return [[c for c in bin(i)[2::].zfill(exp)] for i in range(int(math.pow(2,exp)))]

def get_ternary(exp):
    return list(filter(lambda x: '2' in x, [[c for c in get_base_3(i).zfill(exp)] for i in range(int(math.pow(3,exp)))]))

def get_base_3(n):
    if n==0:
        return '0'

    base_3 = ''
    while n > 0:
        base_3 = str(n%3) + base_3
        n //= 3
    return base_3

def part1(input):
    input = [x.split(': ') for x in input]
    input = [[op, num.split(' ')] for (op, num) in input]
    return sum(map(lambda x: int(x[0]), filter(lambda x: test_equation(int(x[0]), x[1]), input, True)))

def part2(input):
    start_time = time.time()
    input = [x.split(': ') for x in input]
    input = [[op, num.split(' ')] for (op, num) in input]
    res = 0
    for r, n in input:
        n = [int(c) for c in n]
        if test_equation(int(r), n, True):
            res += int(r)
        elif test_equation(int(r), n, False):
            res += int(r)
    print(time.time()-start_time)
    print(res)


#print(part1(input))
part2(input)