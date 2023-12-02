f = open("Day_2_input.txt", "r")

input = [line[:-1:] for line in f]

submarine = {"depth": 0, "distance": 0, "aim": 0}

def part1():
    for com in input:
        com = com.split(" ")
        if com[0] == "forward":
            submarine["distance"] += int(com[1])
        elif com[0] == "down":
            submarine["depth"] += int(com[1])
        else:
            submarine["depth"] -= int(com[1])
    print(submarine["depth"] * submarine["distance"])

def part2():
    for com in input:
        com, increase = com.split(" ")
        increase = int(increase)
        if com == "forward":
            submarine["distance"] += increase
            submarine["depth"] += increase * submarine["aim"]
        elif com == "down":
            submarine["aim"] += increase
        else:
            submarine["aim"] -= increase
    print(submarine["depth"] * submarine["distance"])


part2()
