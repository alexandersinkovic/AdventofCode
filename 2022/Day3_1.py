from aoc_fetcher import get_data

input = get_data(2022, 3)

input = input.splitlines()

letters = 'qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM'
scores = [c for c in letters]
scores.sort()
scores = scores[26::] + scores[0:26:]
eval_score = {}
for index, score in enumerate(scores):
    eval_score[score] = index + 1

result = 0
for line in input:
    first = line[0:int(len(line)/2):]
    second = line[int(len(line)/2)::]
    for c in first:
        if c in second:
            result += eval_score[c]
            break

print(result)
