from aoc_fetcher import get_data

input = get_data(2021, 10)
#input = open("Day_10_testInput.txt").read()

def part1():
    data = [line for line in input.strip().splitlines()]

    #counter = {'(': 0, '[': 0, '{': 0, '<': 0}
    closing_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    score = {'(': 3, '[': 57, '{': 1197, '<': 25137}

    res = 0
    for line in data:
        #counter = {'(': 0, '[': 0, '{': 0, '<': 0}
        counter = []
        corrupted = 'X'
        for c in line:
            #print(counter)
            if c in closing_map.keys():

                if not counter.pop() == closing_map[c]:
                    corrupted = closing_map[c]
                    break
            else:
                counter.append(c)
        #print(counter)
        if not corrupted == 'X':
            res += score[corrupted]
    print(res)

def part2():
    data = [line for line in input.strip().splitlines()]

    closing_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    score_dict = {'(': 1, '[': 2, '{': 3, '<': 4}

    scores = []
    for line in data:
        counter = []
        corrupted = 'X'
        for c in line:
            if c in closing_map.keys():
                if not counter.pop() == closing_map[c]:
                    corrupted = closing_map[c]
                    break
            else:
                counter.append(c)
        if corrupted == 'X':
            score = 0
            while not len(counter) == 0:
                bracket = counter.pop()
                score *= 5
                score += score_dict[bracket]
            scores.append(score)
    scores = sorted(scores)
    print(scores)
    print(len(scores))
    print(round(len(scores)/2))
    print(scores[round(len(scores)/2)])


#part1()
part2()
