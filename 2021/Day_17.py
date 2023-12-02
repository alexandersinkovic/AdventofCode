from aoc_fetcher import get_data

input = get_data(2021, 17)

def part1():
    print(sum(range(225)))

def part2():
    xmax = 65
    xmin = 8
    possible_y = []
    for y in range(-225, 226):
        cur_pos = 0
        cur_y = y
        while (cur_pos >= -225):
            if cur_pos <= -177:
                possible_y.append(y)
                break
            cur_pos += cur_y
            cur_y = cur_y - 1

    print(xmin)
    initial_velos = []
    for x in range(xmin, xmax+1):
        for y in possible_y:
            cur_x = cur_y = steps = 0
            while cur_x <= 65 and cur_y >= -225:
                if cur_x >= 32 and cur_y <= -177:
                    initial_velos.append((x, y))
                    break
                cur_x += x - steps if x-steps >= 0 else 0
                cur_y += y - steps
                steps += 1
    print(len(initial_velos))

#part1()
part2()
