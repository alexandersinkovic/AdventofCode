from aoc_fetcher import get_data
import math
from collections import defaultdict
import itertools

#input = get_data(2021, 19)
#input = open("Day_19_testInput.txt").read()
input = open("Day_19_robertInput.txt").read()

rotations = {
    1: lambda x: x, #(X, Y, Z) #
    2: lambda x: [x[0], x[2], -x[1]], #(X, Z, -Y) #
    3: lambda x: [x[0], -x[1], -x[2]], #(X, -Y, -Z) #
    4: lambda x: [x[0], -x[2], x[1]], #(X, -Z, Y) #
    5: lambda x: [-x[0], x[1], -x[2]], #(-X, Y, -Z) #
    6: lambda x: [-x[0], -x[2], -x[1]], #(-X, -Z, -Y) #
    7: lambda x: [-x[0], -x[1], x[2]], #(-X, -Y, Z) #
    8: lambda x: [-x[0], x[2], x[1]], #(-X, Z, Y) #
    9: lambda x: [x[1], -x[0], x[2]], #(Y, -X, Z) #
    10: lambda x: [x[1], -x[2], -x[0]], #(Y, -Z, -X) #
    11: lambda x: [x[1], x[0], -x[2]], #(Y, X, -Z) #
    12: lambda x: [x[1], x[2], x[0]], #(Y, Z, X) #
    13: lambda x: [-x[1], x[0], x[2]], #(-Y, X, Z) #
    14: lambda x: [-x[1], x[2], -x[0]], #(-Y, Z, -X) #
    15: lambda x: [-x[1], -x[0], -x[2]], #(-Y, -X, -Z) #
    16: lambda x: [-x[1], -x[2], x[0]], #(-Y, -Z, X) #
    17: lambda x: [x[2], x[0], x[1]], #(Z, X, Y) #
    18: lambda x: [x[2], x[1], -x[0]], #(Z, Y, -X) #
    19: lambda x: [x[2], -x[0], -x[1]], #(Z, -X, -Y) #
    20: lambda x: [x[2], -x[1], x[0]], #(Z, -Y, X) #
    21: lambda x: [-x[2], x[0], -x[1]], #(-Z, X, -Y) #
    22: lambda x: [-x[2], -x[1], -x[0]], #(-Z, -Y, -X) #
    23: lambda x: [-x[2], -x[0], x[1]], #(-Z, -X, Y) #
    24: lambda x: [-x[2], x[1], x[0]] #(-Z, Y, X) #
    }

def part1():
    data = input.strip().split("\n\n")
    values = [[[int(x) for x in vec.split(",")] for vec in line.splitlines()[1:] ] for line in data]
    #print(values)
    data = [[line.splitlines()[0][12:-4]] for line in data]
    #print(data)
    for idx, scanners in enumerate(values):
        for i in scanners:
            data[idx].append(i)

    #print(data[:2])
    source_scanner = data[0][1:]
    solved_scanners = defaultdict(lambda : [])
    solved_scanners['0'] = source_scanner

    unknown_scanners = data[1:]
    scn_map = {}
    scn_map['0'] = [1, [0,0,0]]

    while(not len(scn_map) == len(data)):
        print("infinity loop?")
        print("DONE:", len(scn_map), "   TODO:", len(data))
        #print(scn_map)
        #print(unknown_scanners)
        #print(scn_map)
        #print("Go through unknown_scanners")
        delete_scanners = []
        #print([x[0] for x in unknown_scanners])
        for scn in unknown_scanners:
            scn_name = scn[0]
            #print(scn_name)
            scn = scn[1:]
            scn_translation = [0,0,0]
            #print(solved_scanners.keys())
            for i in range(1,25):
                #print(scn)
                #print(i)
                scn_transformed = [rotations[i](point) for point in scn]
                #print(scn_transformed)
                for solved_scanner in solved_scanners.values():
                    scn_transformed_dists = defaultdict(lambda : [])
                    #print("Check against solved Scanner:")
                    #print(solved_scanner)
                    match_found = False
                    for p_trans in scn_transformed:
                        for p_origin in solved_scanner:
                            #if i == 4 and scn_name == '21':
                                #print(rotations[16](p_origin), rotations[2](p_trans))
                                #print()
                            scn_transformed_dists[math.sqrt((p_origin[0] - p_trans[0])**2 + (p_origin[1] - p_trans[1])**2 + (p_origin[2] - p_trans[2])**2)].append((p_origin, p_trans))
                    for key,val in scn_transformed_dists.items():
                        if len(val) >= 12:
                            p1 = scn_transformed_dists[key][0][0]
                            p2 = scn_transformed_dists[key][0][1]
                            #print(p1, p2)
                            scn_translation = [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]
                            #print(scn_translation)
                            #print(i)
                            scn_map[scn_name] = [i, scn_translation]
                            delete_entry = [scn_name]
                            #print(delete_entry)
                            for entry in scn:
                                delete_entry.append(entry)
                            delete_scanners.append(delete_entry)
                            for p_new in scn_transformed:
                                #print([p_new[0], scn_translation[0], p_new[1],  scn_translation[1], p_new[2],  scn_translation[2]])
                                p_new_translated = [p_new[0] + scn_translation[0], p_new[1] + scn_translation[1], p_new[2] + scn_translation[2]]
                                #print(p_new_translated)
                                solved_scanners[scn_name].append(p_new_translated)
                            match_found = True
                            break
                    if match_found:
                        break
                if not scn_translation == [0,0,0]:
                    break
        #print(solved_scanners['1'])
        #print("Deleting:")
        #print(delete_scanners)
        for i in delete_scanners:
            unknown_scanners.remove(i)
    all_beacons = []
    for name, scn in solved_scanners.items():
        for beacon in scn:
            translation = scn_map[name][1]
            #print(translation)
            all_beacons.append(beacon)
    all_beacons.sort()
    all_beacons = list(all_beacons for all_beacons, _ in itertools.groupby(all_beacons))
    #print()
    print(len(all_beacons))

    #part2
    scn_pos = [x[1] for x in scn_map.values()]
    max_manhatten_dist = 0
    for s1 in scn_pos:
        for s2 in scn_pos:
            if sum([abs(s1[0] - s2[0]), abs(s1[1] - s2[1]), abs(s1[2] - s2[2])]) > max_manhatten_dist:
                max_manhatten_dist = sum([abs(s1[0] - s2[0]), abs(s1[1] - s2[1]), abs(s1[2] - s2[2])])
    print(max_manhatten_dist)
    #for line in all_beacons:
        #print(line)


part1()
