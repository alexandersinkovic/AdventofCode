from aoc_fetcher import get_data

input = get_data(2022, 6)

#input = input.splitlines()

for i in range(0, len(input) - 14):
    if len(set([c for c in input[i:i + 14:]])) == 14:
        print(i + 14)
        break
