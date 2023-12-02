from aoc_fetcher import get_data
from collections import defaultdict

input = get_data(2021, 12)

def part1():
    data = input.strip().splitlines()
    neighbors = defaultdict(lambda : [])

    for line in data:
        n1, n2 = line.split('-')
        neighbors[n1].append(n2)
        neighbors[n2].append(n1)

    all_paths = DFS("start", neighbors, ["start"], 0, True)

    print(all_paths)

def DFS(cur_node, neighbors, visited, all_paths, twice):
    #print("Methodenaufruf:")
    #print(cur_node)
    for n in neighbors[cur_node]:
        #print(visited)
        #print(n)
        if n == "end":
            all_paths += 1
        elif n == "start":
            continue
        elif n in visited and twice:
            all_paths = DFS(n, neighbors, visited, all_paths, False)
        elif not n in visited:
            new_visited = visited
            if n == n.lower():
                new_visited = visited[0:len(visited)]
                new_visited.append(n)
            #new_path = cur_path
            #new_path.append(n)
            all_paths = DFS(n, neighbors, new_visited, all_paths, twice)
    return all_paths


part1()
