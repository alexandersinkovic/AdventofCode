from aoc_fetcher import get_data

#input = get_data(2023, 14).splitlines()
input = open("Day14_test.txt", "r").read().splitlines()

#print(input[:20])

res = 0
def tilt(rows, up):
    columns = []
    
    for i in range(len(rows[0])):
        columns.append(''.join([rows[x][i] for x in range(len(rows))]))


    newColumns = []
    for col in columns:
        parts = col.split('#')
        sortedParts = []
        for part in parts:
            sortedParts.append(''.join(sorted([c for c in part], reverse = up)))
        newColumns.append('#'.join(sortedParts))
    return newColumns

for line in input:
    print(line)
print()
field = input
for c in range(300):
    for i in range(4):
        field = tilt(field, i < 2)
    for line in field:
        print(line)
    print()

print(res)
