from aoc_fetcher import get_data

input = get_data(2023, 8).splitlines()
#input = open('Day8_test.txt', 'r').read().splitlines()

sequence = input[0]
sequence = sequence.replace('L', '0')
sequence = sequence.replace('R', '1')
map = [line.split(' = ') for line in input[2::]]
step = {}
for line in map:
    print(line)
    step[line[0]] = line[1][1:-1:].split(', ')
#print(step.items())

count = 0
idx = 0
elem = 'AAA'
while(elem != 'ZZZ'):
    elem = step[elem][int(sequence[idx])]
    idx = (idx + 1)%(len(sequence))
    count+=1
print(count)