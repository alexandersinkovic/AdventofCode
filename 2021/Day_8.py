from aoc_fetcher import get_data

input = get_data(2021, 8)

def part1():
    print(sum([len([l for l in line.split(" | ")[1].split(" ") if len(l) in [2,3,4,7]]) for line in input.strip().splitlines()]))

#part1()

def part2():
    data = [[l for l in line.split(" | ")] for line in input.strip().splitlines()]
    res = 0
    for line in data:
        decoder = get_decoder(line[0].split(" "))
        nums = []

        for n in line[1].split(" "):
            for k, v in decoder.items():
                if sorted(n) == sorted(v):
                    nums.append(k)
        print(nums)
        print(int(''.join(nums)))
        res += int(''.join(nums))
    print(res)


def get_decoder(nums):
    decoder = {}

    five_chars = []
    six_chars = []

    for n in nums:
        if len(n) == 2:
            decoder["1"] = n
        elif len(n) == 3:
            decoder["7"] = n
        elif len(n) == 4:
            decoder["4"] = n
        elif len(n) == 7:
            decoder["8"] = n
        elif len(n) == 5:
            five_chars.append(n)
        else:
            six_chars.append(n)

    for n in five_chars:
        if len(diff(decoder["1"], n)) == 0:
            decoder["3"] = n
        elif len(diff(n, decoder["4"])) == 3:
            decoder["2"] = n
        else:
            decoder["5"] = n

    for n in six_chars:
        if len(diff(n, decoder["3"])) == 1:
            decoder["9"] = n
        elif len(diff(n, decoder["7"])) == 4:
            decoder["6"] = n
        else:
            decoder["0"] = n
    return decoder

def diff(lst1, lst2):
    return [l for l in lst1 if not l in lst2]

part2()
