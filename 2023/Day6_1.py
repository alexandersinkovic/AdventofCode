from functools import reduce

times = [47, 84, 74, 67]
distances = [207, 1394, 1209, 1014]

ways = []

for i in range(len(times)):
    time = times[i]
    dist = distances[i]
    for j in range(time):
        traveldist = j * (time-j)
        if traveldist > dist:
            ways.append(time - (j*2) + 1)
            break

print(reduce(lambda x, y: x * y, ways,  1))