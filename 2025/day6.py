from aocd import get_data

DATA = get_data(day=6, year=2025)
#DATA = open('day6.input').read()

INPUT = DATA.splitlines()
OPS = list(filter(lambda f : len(f) >= 1, INPUT[-1].split(' ')))
NUMS = [list(filter(lambda f : len(f) >= 1, x.split(' '))) for x in INPUT[:-1]]

def p1():
    res = 0
    for idx in range(len(NUMS[0])):
        if OPS[idx] == '+':
            res += int(NUMS[0][idx]) + int(NUMS[1][idx]) + int(NUMS[2][idx]) + int(NUMS[3][idx])
        else:
            res += int(NUMS[0][idx]) * int(NUMS[1][idx]) * int(NUMS[2][idx]) * int(NUMS[3][idx])
    print(res)

def p2():
    my_input = [[c for c in line] for line in INPUT[:-1]]
    res = 0
    problems = []
    next_problem = []
    for col in range(len(my_input[0])):
        num = []
        for row in range(len(my_input)):
            if my_input[row][col] != ' ':
                num.append(my_input[row][col])
        if ''.join(num).isdigit():
            next_problem.append(int(''.join(num)))
        else:
            problems.append(next_problem)
            next_problem = []
    problems.append(next_problem)
    for idx in range(len(problems)):
        if OPS[idx] == '+':
            res += sum(problems[idx])
        else:
            prod = 1
            for n in problems[idx]:
                prod *= n
            res += prod
    print(res)


p1()
p2()