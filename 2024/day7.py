from aocd import data
from itertools import combinations_with_replacement

data = data.split('\n')

#f = open('day7in.txt', 'r').read()
f = open('day7test.txt', 'r').read()
input = f.split('\n')

def test_equation(res , nums):
    print(res, nums)
    ops = list(combinations_with_replacement('*+', len(nums)-1))
    for op in ops:
        print(op)
        carry = int(nums[0])
        for i in range(len(op)):
            carry = sum_or_mul(carry, int(nums[i+1]), op[i])
        print(carry)
        if int(res) == carry:
            return True
    return False

def sum_or_mul(a, b, op):
    if op == '*':
        return a * b
    return a+b

def part1(input):
    res = 0
    input = [x.split(': ') for x in input]
    input = [[op, num.split(' ')] for (op, num) in input]
    return sum(map(lambda x: int(x[0]), filter(lambda x: test_equation(x[0], x[1]), input)))

def part2(input):
    pass


print(part1(input))
#part2(data)