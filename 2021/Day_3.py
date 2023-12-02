from aoc_fetcher import get_data

input = get_data(2021, 3)

def part1():
    counter = [0]*12
    for i in range(len(input)):
        if i%13 == 12:
            continue
        counter[i%13] += int(input[i])
    print("Number of 1s found:", counter)
    print(len(input)/13)
    gamma_rate = list(map(lambda n1: '1' if n1/(len(input)/13) > 0.5 else '0', counter))
    epsilon_rate = list(map(lambda n1: str(1-int(n1)), gamma_rate))
    #print(res)
    print("Gamma_rate:", ''.join(gamma_rate))
    print(int(''.join(gamma_rate), 2))
    print("Epsilon_rate:", ''.join(epsilon_rate))
    print(int(''.join(epsilon_rate), 2))
    power_consumption = int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2)
    print(power_consumption)

def part2():
    data = []
    for i in range(0, len(input), 13):
        data.append(''.join(input[i:i+12]))
    bit = 0
    while(len(data)>1):
        cnt = counter(data, bit)
        cmp = '1' if cnt/len(data)>=0.5 else '0'
        data = [b for b in data if b[bit]==cmp]
        bit += 1
    oxygen_rate = int(data[0], 2)
    data = []
    for i in range(0, len(input), 13):
        data.append(''.join(input[i:i+12]))
    bit = 0
    while(len(data)>1):
        cnt = counter(data, bit)
        cmp = '0' if cnt/len(data)>=0.5 else '1'
        data = [b for b in data if b[bit]==cmp]
        bit += 1
        print(data)
        print(" ")
    co2_rate = int(data[0], 2)
    print(oxygen_rate*co2_rate)

def counter(report, bit):
    res = 0
    for b in report:
        res += int(b[bit])
    return res

part2()
