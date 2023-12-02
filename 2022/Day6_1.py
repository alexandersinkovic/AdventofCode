from aoc_fetcher import get_data

input = get_data(2022, 6)

#input = input.splitlines()

for i in range(0, len(input) - 4):
    print([c for c in input[i:i + 4:]])
    if len(set([c for c in input[i:i + 4:]])) == 4:
        print(i + 4)
        break
