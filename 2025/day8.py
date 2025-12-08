from aocd import get_data
import math

DATA = open('2025/day8.input').read()
DATA = get_data(day=8, year=2025)
INPUT = DATA.splitlines()

COORDS = [list(map(int, c.split(','))) for c in INPUT]

def euclid_dist1D(a, b):
    return abs(a-b)

def euclid_dist3D(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def get_circuit(idx, circuits):
    for circuit in circuits:
        if idx in circuit:
            return circuit
    return [idx]

def get_shortest_dists():
    shortest_dists = []
    for idx in range(len(COORDS)):
        for idy in range(idx+1, len(COORDS)):
            dist = euclid_dist3D(COORDS[idx], COORDS[idy])
            shortest_dists.append((dist, idx, idy))
    shortest_dists.sort(key=lambda x: x[0])
    return shortest_dists

def p1():
    shortest_dists = get_shortest_dists()
    circuits = []
    check_range = 1000
    check_idx = 0
    while check_idx < check_range and check_idx < len(shortest_dists):
        #print('---')
        #print(check_idx, check_range)
        _, box_a_idx, box_b_idx = shortest_dists[check_idx]
        #print(box_a_idx, box_b_idx)
        #print(circuits)
        new_circuit = True
        for circuit in circuits:
            if box_a_idx in circuit and box_b_idx in circuit:
                #check_range += 1
                new_circuit = False
                break
            elif box_a_idx in circuit:
                circuit_b = get_circuit(box_b_idx, circuits)
                if len(circuit_b) > 1:
                    circuits.remove(circuit_b)
                for x in circuit_b:
                    circuit.append(x)
                new_circuit = False
                break
            elif box_b_idx in circuit:
                circuit_a = get_circuit(box_a_idx, circuits)
                if len(circuit_a) > 1:
                    circuits.remove(circuit_a)
                for x in circuit_a:
                    circuit.append(x)
                new_circuit = False
                break
        if new_circuit:
            circuits.append([box_a_idx, box_b_idx])
        check_idx += 1

    sizes = [len(c) for c in circuits]
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])


def p2():
    shortest_dists = get_shortest_dists()
    _, initial_a, initial_b = shortest_dists[0]
    circuits = [[initial_a, initial_b]]
    check_idx = 1
    while len(circuits[0]) < len(COORDS) and check_idx < len(shortest_dists):
       # print('---')
        _, box_a_idx, box_b_idx = shortest_dists[check_idx]
        #print(box_a_idx, box_b_idx)
        #print(circuits)
        new_circuit = True
        for circuit in circuits:
            if box_a_idx in circuit and box_b_idx in circuit:
                #check_range += 1
                new_circuit = False
                break
            elif box_a_idx in circuit:
                circuit_b = get_circuit(box_b_idx, circuits)
                if len(circuit_b) > 1:
                    circuits.remove(circuit_b)
                for x in circuit_b:
                    circuit.append(x)
                new_circuit = False
                break
            elif box_b_idx in circuit:
                circuit_a = get_circuit(box_a_idx, circuits)
                if len(circuit_a) > 1:
                    circuits.remove(circuit_a)
                for x in circuit_a:
                    circuit.append(x)
                new_circuit = False
                break
        if new_circuit:
            circuits.append([box_a_idx, box_b_idx])
        if len(circuits[0]) == len(COORDS):
            print(COORDS[box_a_idx][0] * COORDS[box_b_idx][0])
            break
        check_idx += 1

p1()
#5472 too low
p2()