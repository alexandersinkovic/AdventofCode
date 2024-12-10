from aocd import data
from aoc_utils import add_to_dict
import time


def part1(input):
    files = {}
    space = []
    fileID = 0
    spaceIDx = 0
    for i in range(len(input)):
        if i%2 ==0:
            for j in range(int(input[i])):
                add_to_dict(fileID, spaceIDx, files)
                spaceIDx += 1
            fileID+=1
        else:
            for j in range(int(input[i])):
                space.append(spaceIDx)
                spaceIDx+=1
    freeSpace = space.pop(0)
    filesW = list(files.items())
    filesW.reverse()
    for file in filesW:
        newIdx = []
        if file[1][0] > freeSpace:
            for _ in range(len(file[1])):
                highest = file[1].pop()
                if highest > freeSpace:
                    newIdx.append(freeSpace)
                else:
                    newIdx.append(highest)
                    for p in file[1]:
                        newIdx.append(p)
                    break
                freeSpace = space.pop(0)
            files[file[0]] = newIdx
    checksum = list(map(lambda x: [x[0]*f for f in x[1]], list(files.items())))
    checksumFlat = []
    for l in checksum:
        checksumFlat.extend(l)
    print(sum(checksumFlat))

def part2(input):
    s_t = time.time()
    files = {}
    space = []
    fileID = 0
    spaceIDx = 0
    for i in range(len(input)):
        if i%2 ==0:
            for j in range(int(input[i])):
                add_to_dict(fileID, spaceIDx, files)
                spaceIDx += 1
            fileID+=1
        else:
            for j in range(int(input[i])):
                space.append(spaceIDx)
                spaceIDx+=1
    filesW = list(files.items())
    filesW.reverse()
    for file in filesW:
        fSize = len(file[1])
        for i in range(len(space)-fSize):
            if space[i+fSize-1] > file[1][-1]:
                break
            if space[i+fSize-1] - space[i] == fSize-1:
                files[file[0]] = space[i:i+fSize]
                for f in files[file[0]]:
                    space.remove(f)
                break
    print(files.items())

    checksum = list(map(lambda x: [x[0]*f for f in x[1]], list(files.items())))
    checksumFlat = []
    for l in checksum:
        checksumFlat.extend(l)
    print(sum(checksumFlat))
    print(time.time() - s_t)


part2(data)