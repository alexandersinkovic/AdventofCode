from aoc_fetcher import get_data
import math

input = get_data(2023, 4).splitlines()
#input = open('Day4_test.txt', 'r').read().splitlines()

scores = [math.pow(2, i) for i in range(0,11)]
numofmatches = [0 for i in range(201)]
numofcards = [1 for i in range(201)]

for idx, card in enumerate(input):
    mynumbers, winner = card.split(' | ')
    mynumbers = mynumbers[10::]
    
    winner = [int(n) for n in winner.split(' ') if len(n) > 0]
    mynumbers = [int(n) for n in mynumbers.split(' ') if len(n) > 0]
    matches = 0
    for x in mynumbers:
        if x in winner:
            matches += 1
    numofmatches[idx] = matches

final_score = 0
for i in range(201):
    final_score+=numofcards[i]
    for j in range(0,numofmatches[i]):
        numofcards[i+j+1] += numofcards[i]

print(final_score)