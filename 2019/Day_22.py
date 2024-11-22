
f = open("Day_22_in.txt", "r")
f1 = open("Day_14_test1.txt", "r")
f2 = open("Day_14_test2.txt", "r")
f3 = open("Day_14_test3.txt", "r")
f4 = open("Day_14_test4.txt", "r")
f5 = open("Day_14_test5.txt", "r")

input = f.read()
input = input.replace('deal into new stack', 'a')
input = input.replace('cut', 'b')
input = input.replace('deal with increment', 'c')
input = input.split('\n')

STACK_SIZE = 10007

def deal_into_new_stack(cards: [int]):
    cards.reverse()

def cut(cards: [int], n: int):
    return sum([cards[n::], cards[0:n:]], [])

def deal_with_increment(cards: [int], n: int):
    new_stack = [0 for _ in range(0, len(cards))]
    idx = 0
    for i in range(0, len(cards)):
        new_stack[idx] = cards[i]
        idx = (idx + n) % len(cards)
    return new_stack

def part1(input):
    cards = [i for i in range(0, STACK_SIZE)]
    print(len(cards))
    input = [line.split(' ') for line in input]
    for line in input:
        print(line)
        n = line[-1]
        command = line[0]
        if command == 'a':
            deal_into_new_stack(cards)
        elif command == 'b':
            cards = cut(cards, int(n))
        else:
            cards = deal_with_increment(cards, int(n))

    print(cards.index(2019))

part1(input)
