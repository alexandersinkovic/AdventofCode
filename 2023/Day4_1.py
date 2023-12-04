from aoc_fetcher import get_data
import math

input = get_data(2023, 4).splitlines()
#input = open('Day4_test.txt', 'r').read().splitlines()

scores = [math.pow(2, i) for i in range(0,11)]
res = [0 for i in range(11)] 

for card in input:
    mynumbers, winner = card.split(' | ')
    mynumbers = mynumbers[10::]
    
    winner = [int(n) for n in winner.split(' ') if len(n) > 0]
    mynumbers = [int(n) for n in mynumbers.split(' ') if len(n) > 0]
    matches = 0
    for x in mynumbers:
        if x in winner:
            matches += 1
    res[matches] += 1

print(scores)
print(res)
final_score = 0    
for i in range(1, 11):
    matches = res[i]
    final_score += scores[i-1] * matches

print(final_score)