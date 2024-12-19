from aocd import data
import functools

#data = open('day19test.txt', 'r').read()
patterns, designs = data.split('\n\n')
patterns = patterns.split(', ')
designs = designs.split('\n')


@functools.cache
def checkPossible(design):
    if design == '':
        return 1
    return sum([checkPossible(design[len(p):]) for p in patterns if p == design[:len(p)]])


def part1():
    print(sum([checkPossible(d) > 0 for d in designs]))
    

def part2():
    print(sum([checkPossible(d) for d in designs]))

part1()
part2()