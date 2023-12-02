from aoc_fetcher import get_data
from time import sleep

input = get_data(2022, 9)
#f = open("Day9_test.txt", "r")
#input = [line for line in f]

input = input.splitlines()

rope = [(55,174), (55,174), (55,174), (55,174), (55,174), (55,174), (55,174), (55,174), (55,174), (55,174)]
#rope = [(55, 174), (55, 174)]
names = ['H', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#rope = [(5,5), (5,5)]

move = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)};

result = []
for i in range(299):
    result.append(['.'] * 300)

def isConnected(x1, y1, x2, y2):
    return (abs(x1-x2) < 2 and abs(y1-y2) < 2)


def motion(head, tail):
    if (head == tail):
        return head
    if (head < tail):
        return tail - 1
    else:
        return tail + 1

def printResult():
    sleep(0.1)
    field = []
    for i in range(305):
        field.append(['.'] * 300)

    for i in range(len(rope) - 1, -1, -1):
        r = rope[i]
        field[r[1]][r[0]] = names[i]
    for i in range(len(field) - 1, -1, -1):
        print(''.join(field[i]))
    print('')


for line in input:
    (dir, reps) = line.split(' ')
    for i in range(int(reps)):
        x, y = move[dir]
        rope[0] = (rope[0][0] + x, rope[0][1] + y)
        #printResult()
        for j in range(1, len(rope)):
            r1 = rope[j - 1]
            r2 = rope[j]
            if (not isConnected(r1[0], r1[1], r2[0], r2[1])):
                rope[j] = (motion(r1[0], r2[0]), motion(r1[1], r2[1]))
            #printResult()
        tail = rope[-1]
        result[tail[1]][tail[0]] = '#'

resCount = 0

for i in range(len(result) - 1, -1, -1):
    for j in range(len(result[0])):
        if result[i][j] == '#':
            resCount += 1
    print(''.join(result[i]))
print(resCount)
