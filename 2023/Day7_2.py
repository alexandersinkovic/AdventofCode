from aoc_fetcher import get_data
from collections import defaultdict
from functools import reduce

input = get_data(2023, 7).replace('A', 'Z')
input = input.replace('K', 'Y')
input = input.replace('T', 'B')
input = input.replace('J', '1')
input = [game.split(' ') for game in input.splitlines()]
scores = {5: 1, 4: 2, 3: 0, 2: 0, 1: 7}
values = []

for card, bid in input:
    parts = set([c for c in card])
    score = scores[len(parts)]
    dist = defaultdict(int)
    for c in card:
        dist[c] += 1
    if dist['1'] > 0:
        jokers = dist['1']
        dist['1'] = 1
        dist[max(dist, key=lambda x: dist[x])] += jokers
        if dist[max(dist, key=lambda x: dist[x])] == 5:
            score = 7
        elif dist[max(dist, key=lambda x: dist[x])] == 4:
            score = 6
        elif dist[max(dist, key=lambda x: dist[x])] == 3:
            if len(dist.keys()) == 3:
                score = 5
            else:
                score = 4
        elif dist[max(dist, key=lambda x: dist[x])] == 2:
            score = 2
    elif len(parts) == 2:
        if dist[max(dist, key=lambda x: dist[x])] == 4:
            score = 6
        else:
            score = 5
    elif len(parts) == 3:
        if dist[max(dist, key=lambda x: dist[x])] == 3:
            score = 4
        else:
            score = 3
    values.append([card, bid, score])
values.sort(key=lambda x: (x[2], x[0]))
res = 0
for i in range(1, len(values)+1):
    res += int(values[i-1][1]) * i
print(res)        
    