DIRS4 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
DIRS9 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def splitTwice(input):
    return [[c for c in line] for line in input.split('\n')]

def add_to_dict(k, v, dict):
    if k in dict:
        dict[k].append(v)
    else:
        dict[k] = [v]