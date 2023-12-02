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
for i in range(0, len(input), 3):

    first = input[i]
    second = input[i+1]
    third = input[i+2]
    for c in first:
        if c in second and c in third:
            result += eval_score[c]
            break

print(result)
