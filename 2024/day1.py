from aoc_fetcher import get_data

input = get_data(2024, 1).splitlines()

input = [x.split('   ') for x in input]

def day1():
    lst1 = []
    lst2 = []

    for a, b in input:
        lst1.append(int(a))
        lst2.append(int(b))

    lst1.sort()
    lst2.sort()

    sum = 0

    for i in range(len(lst1)):
        sum += abs(lst1[i] - lst2[i])

    print(sum)

    similarity = 0

    for x in lst1:
        similarity += lst2.count(x) * x

    print(similarity)

day1()