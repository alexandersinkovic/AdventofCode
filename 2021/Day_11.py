from aoc_fetcher import get_data

input = get_data(2021, 11)
#input = open("Day_11_testInput.txt").read()

def part1():
    data = [[int(x) for x in line] for line in input.strip().splitlines()]

    total = 0
    #part1
    #for loop in range(100)
    for loop in range(1000):
        data = [[x+1 for x in line] for line in data]
        flashes = []
        flash_check = []
        for i in range(10):
            for j in range(10):
                if data[i][j] > 9:
                    flashes.append((i, j))
                    flash_check.append((i, j))
        while len(flashes) != 0:
            flashY, flashX = flashes.pop()
            for x in range(-1,2,1):
                if flashX + x < 0 or flashX + x >= 10:
                    continue
                for y in range(-1,2,1):
                    if x == y == 0 or flashY + y < 0 or flashY + y >= 10:
                        continue
                    data[flashY + y][flashX + x] += 1
                    #print(data[flashY + y][flashX + x], (flashY + y, flashX + x))
                    #print(flash_check)
                    if data[flashY + y][flashX + x] > 9 and not (flashY + y, flashX + x) in flash_check:
                        #print("If True")
                        flashes.append((flashY + y, flashX + x))
                        flash_check.append((flashY + y, flashX + x))
        #print(flash_check)
        #Part1
        #total += len(flash_check)
        #part2
        if len(flash_check) == 100:
            print(sorted(flash_check))
            print(loop)
            break
        data = [[x if x < 10 else 0 for x in line] for line in data]
        #print()
        #[print(line) for line in data]
    print(total)


part1()
