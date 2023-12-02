from aoc_fetcher import get_data
from collections import defaultdict

input = get_data(2021, 5)

#input = open("Day_5_Test_Input.txt", "r").read()

def part1():
    lines = input.split("\n")[:-1]
    lines = [line.split(" -> ") for line in lines]
    #print("All Vectors")
    #print(lines[-5:])
    vecs = []
    for line in lines:
        vecs.append([line[0].split(","), line[1].split(",")])
    #print(vecs[-5:])
    h_and_v_vecs = []
    for vec in vecs:
        #print()
        #print(vec)
        #print(vec[0][1])
        #print(vec[1][1])
        #print(vec[0][1] == vec[1][1])
        #print((vec[0][0] == vec[1][0]) or (vec[0][1] == vec[1][1]))
        if (vec[0][0] == vec[1][0]) or (vec[0][1] == vec[1][1]):
            h_and_v_vecs.append(vec)
    #print(h_and_v_vecs[-5:])
    count_points = defaultdict(lambda: 0)
    #print("All straight vectors")
    #print(h_and_v_vecs)
    for vec in h_and_v_vecs:
        #print(vec)
        #print()
        #print(vec[0][0], "==", vec[1][0])
        #print(vec[0][0] == vec[1][0])
        if vec[0][0] == vec[1][0]:
            #print(vec[0][1], ">", vec[1][1])
            #print(vec[0][1] > vec[1][1])
            if int(vec[0][1]) > int(vec[1][1]):
                for y in range(int(vec[1][1]), int(vec[0][1])+1):
                    #print(y)
                    count_points[f"{vec[0][0]},{y}"] += 1
                    #print(f"{vec[0][0]},{y}")
            else:
                #print(int(vec[0][1]))
                #print(int(vec[1][1]))
                for y in range(int(vec[0][1]), int(vec[1][1])+1):
                    #print(y)
                    count_points[f"{vec[0][0]},{y}"] += 1
                    #print(f"{vec[0][0]},{y}")
        else:
            if int(vec[0][0]) > int(vec[1][0]):
                for x in range(int(vec[1][0]), int(vec[0][0])+1):
                    #print(x)
                    count_points[f"{x},{vec[0][1]}"] += 1
                    #print(f"{x},{vec[0][1]}")
            else:
                for x in range(int(vec[0][0]), int(vec[1][0])+1):
                    #print(x)
                    count_points[f"{x},{vec[0][1]}"] += 1
                    #print(f"{x},{vec[0][1]}")
        #print(count_points)
    #h_and_v_vecs = list(map(lambda v: list(filter(lambda p1, p2: (p1[0] == p2[0]) or (p1[1] == p2[1]) , (v[0], v[1]))), vecs ))
    #print(count_points)
    res = 0
    for key in count_points.keys():
        if count_points[key] > 1:
            #print(key)
            res += 1
    print("h_and_v_vecs: ", len(h_and_v_vecs))
    print(h_and_v_vecs[:4])
    print(len(count_points.keys()))
    print(res)
    #test = defaultdict(lambda: 0)
    #test["t"] += 1
    #test["t"] += 1
    #print(test)

def part2():
    lines = input.split("\n")[:-1]
    lines = [line.split(" -> ") for line in lines]
    vecs = []
    for line in lines:
        vecs.append([line[0].split(","), line[1].split(",")])
    count_points = defaultdict(lambda: 0)
    for vec in vecs:
        if vec[0][0] == vec[1][0]:
            if int(vec[0][1]) > int(vec[1][1]):
                for y in range(int(vec[1][1]), int(vec[0][1])+1):
                    count_points[f"{vec[0][0]},{y}"] += 1
            else:
                for y in range(int(vec[0][1]), int(vec[1][1])+1):
                    count_points[f"{vec[0][0]},{y}"] += 1
        elif vec[0][1] == vec[1][1]:
            if int(vec[0][0]) > int(vec[1][0]):
                for x in range(int(vec[1][0]), int(vec[0][0])+1):
                    count_points[f"{x},{vec[0][1]}"] += 1
            else:
                for x in range(int(vec[0][0]), int(vec[1][0])+1):
                    count_points[f"{x},{vec[0][1]}"] += 1
        else:
            xs = -1 if int(vec[0][0]) > int(vec[1][0]) else 1
            ys = -1 if int(vec[0][1]) > int(vec[1][1]) else 1
            for i in range(abs(int(vec[1][0]) - int(vec[0][0]))+1):
                x = i * xs
                y = i * ys
                #print(f"{int(vec[0][0]) + x}, {int(vec[0][1]) + y}")
                count_points[f"{int(vec[0][0]) + x},{int(vec[0][1]) + y}"] += 1
            #print(vec)
    res = 0
    for key in count_points.keys():
        if count_points[key] > 1:
            res += 1
    print(len(count_points))
    print(res)


#part1()
part2()
