from aoc_fetcher import get_data

input = get_data(2022, 2)

input = input.splitlines()
matches = [line.split(' ') for line in input]

scoresMap = {'X': 1, 'Y': 2, 'Z': 3}
X = 1
Y = 2
Z = 3

def rpsMap(xyz):
    if xyz == 'X': return 'A'
    if xyz == 'Y': return 'B'
    return 'C'

def rpsComparator(other, you):
    if other == you: return 3
    if (other == 'A' and you == 'B') or (other == 'B' and you == 'C') or (other == 'C' and you == 'A'): return 6
    return 0

scores = [rpsComparator(other, rpsMap(you)) + scoresMap[you] for other, you in matches]

print(sum(scores))
