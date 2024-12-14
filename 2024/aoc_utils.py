import re

DIRS4 = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
DIRS_ADJ = list(DIRS4.values())
TURNLEFT = {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'}
TURNRIGHT = {'U': 'R', 'L': 'U', 'D': 'L', 'R': 'D'}
DIRS9 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def splitTwice(input):
    return [[c for c in line] for line in input.split('\n')]

def add_to_list_dict(k, v, dict):
    if k in dict:
        dict[k].append(v)
    else:
        dict[k] = [v]

def add_to_num_dict(k, v, dict):
    if k in dict:
        dict[k] += v
    else:
        dict[k] = v

def getIntFromString(s: str):
    return [int(x) for x in re.findall(r'[\+|-]?[0-9]+', s)]