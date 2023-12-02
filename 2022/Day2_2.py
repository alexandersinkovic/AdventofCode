from aoc_fetcher import get_data

input = get_data(2022, 2)

input = input.splitlines()

scores = {  'A X': 3,
            'A Y': 4,
            'A Z': 8,
            'B X': 1,
            'B Y': 5,
            'B Z': 9,
            'C X': 2,
            'C Y': 6,
            'C Z': 7}

print(sum([scores[i] for i in input]))
