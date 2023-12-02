from aoc_fetcher import get_data

input = get_data(2021, 6)

def simulation(days):
    day = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = [int(i) for i in input.split(",")]
    for fish in data:
        day[fish] += 1
    for i in range(days):
        day0 = day[0]
        for j in range(len(day)-1):
            day[j] = day[j+1]
        day[6] += day0
        day[8] = day0
    print(day)
    print(sum(day))

#simulation(80)
simulation(256)
