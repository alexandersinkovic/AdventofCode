from aoc_fetcher import get_data

numbermap = {'six': '6', 'four': '4', 'eight': 'e8t', 'nine': 'n9', 'seven': '7', 'five': '5', 'one': 'o1', 'two': '2', 'three': '3'}

def myreplace(line: str):
    for key in numbermap:
        line = line.replace(key, str(numbermap[key]))
    return line

input = get_data(2023, 1).splitlines()
numbers = [list(filter(lambda x: x.isnumeric(), [c for c in myreplace(line)])) for line in input]
res = 0
for line in numbers:
    res += int(line[0])*10 + int(line[-1])

print(res)