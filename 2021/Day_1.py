f = open("Day_1_input.txt", "r")
input = [int(line[:-1:]) for line in f]

def part1():
    increases = 0
    for i in range(1, len(input)):
        if input[i] > input [i-1]:
            increases += 1
    print(increases)

def part2():
    increases = 0
    for i in range(1, len(input)-2):
        #print(input[i-1:i+2:], "Sum:", sum(input[i-1:i+2:]), "> Sum:", sum(input[i:i+3:]), input[i:i+3:])
        if sum(input[i-1:i+2:]) < sum(input[i:i+3:]):
            increases += 1
    print(increases)

part2()
