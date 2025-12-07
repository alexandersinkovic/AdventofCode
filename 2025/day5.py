from aocd import get_data

DATA = get_data(day=5, year=2025)

FRESH_RANGES, IDS = DATA.split('\n\n')

FRESH_RANGES = [list(map(int, x.split('-'))) for x in FRESH_RANGES.splitlines()]
#FRESH_RANGES = [[3,5], [10, 14], [16,20], [12,18]]

IDS = list(map(lambda x: int(x), IDS.splitlines()))

def p1():
    count = 0
    for id in IDS:
        for range in FRESH_RANGES:
            if range[0] <= id <= range[1]:
                count += 1
                break
    print(count)


def p2():
    sorted_ranges = sorted(FRESH_RANGES)
    optimized_ranges = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        prev = optimized_ranges[-1]
        if prev[1] >= r[0]:
            if prev[1] <= r[1]:
                optimized_ranges[-1] = [prev[0], r[1]]
        else:
            optimized_ranges.append(r)
    total_range = 0
    for r in optimized_ranges:
        total_range += r[1] - r[0] + 1

#p1()
p2()