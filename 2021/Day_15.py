from aoc_fetcher import get_data
import heapq

input = get_data(2021, 15)
#input = open("Day_15_testInput.txt").read()

def part1():
    graph = input.strip().splitlines()
    dijkstra(graph)

def part2():
    graph = input.strip().splitlines()
    #for idx, v in enumerate(graph*5):
        #print(idx, v)
        #print(v, str(int(idx/len(graph))))
    #graph = graph*5
    #graph = [[int(val) + int(index/len(line)) if int(val) + int(index/len(line)) <= 9 else 1 for index, val in enumerate(line*5)] for line in graph]
    graph = [[(int(val) + int(index/len(line)) + int(idy/len(graph))) % 9 if not (int(val) + int(index/len(line)) + int(idy/len(graph))) % 9 == 0 else 9 for index, val in enumerate(line*5)] for idy, line in enumerate(graph*5)]

    #print(graph)

    dijkstra(graph)

def dijkstra(graph):
    nodes = {}
    work_queue = []
    done_nodes = set()
    infinity = len(graph) * len(graph[0]) * 9 + 1
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            node = f"{i},{j}"
            nodes[node] = (infinity, "X")
    nodes["0,0"] = (0, "Start")
    heapq.heappush(work_queue, (0, "0,0"))

    while not len(work_queue) == 0:
        cur_node = heapq.heappop(work_queue)
        #print("while", cur_node)
        cur_node_dist = cur_node[0]
        cur_node_y, cur_node_x = [int(x) for x in cur_node[1].split(",")]
        done_nodes.add(cur_node[1])
        if cur_node_x-1 >= 0:
            relax(nodes, cur_node_y, cur_node_x-1, graph, cur_node_dist, cur_node[1], work_queue)
        if cur_node_x+1 < len(graph[0]):
            relax(nodes, cur_node_y, cur_node_x+1, graph, cur_node_dist, cur_node[1], work_queue)
        if cur_node_y-1 >= 0:
            relax(nodes, cur_node_y-1, cur_node_x, graph, cur_node_dist, cur_node[1], work_queue)
        if cur_node_y+1 < len(graph[0]):
            relax(nodes, cur_node_y+1, cur_node_x, graph, cur_node_dist, cur_node[1], work_queue)
    print(nodes[f"{len(graph)-1},{len(graph[0])-1}"])


def relax(nodes, y, x, graph, cur_dist, prev_node, work_queue):
    #print(int(graph[y][x]) + cur_dist, nodes[f"{y},{x}"][0])
    cur_node = f"{y},{x}"
    if cur_node == f"{len(graph)-1},{len(graph[0])-1}":
        work_queue = []
        print(int(graph[y][x]) + cur_dist)
    if int(graph[y][x]) + cur_dist < nodes[cur_node][0]:
        nodes[cur_node] = (int(graph[y][x]) + cur_dist, prev_node)
        heapq.heappush(work_queue, (int(graph[y][x]) + cur_dist, cur_node))

#part1()
part2()
