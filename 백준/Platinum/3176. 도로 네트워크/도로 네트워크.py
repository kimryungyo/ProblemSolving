from math import log2
from sys import stdin, setrecursionlimit
input = lambda: stdin.readline().rstrip()
setrecursionlimit(10 ** 6)

N = int(input())

LOG = int(log2(N)) + 1
depths = [ 0 ] * (N + 1)
visited = [ False ] * (N + 1)
parents = [ [0] * LOG for _ in range(N + 1) ]

road_lengs = [ [] for _ in range(N + 1) ]
roads = [ [(0, 0) for _ in range(LOG) ] for _ in range(N + 1) ]

graph = [ [] for _ in range(N + 1) ]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    road_lengs[a].append( (b, c) )
    road_lengs[b].append( (a, c) )
    graph[a].append(b)
    graph[b].append(a)

def dfs(node = 1, depth = 0):
    visited[node] = True
    depths[node] = depth

    for next, leng in road_lengs[node]:
        if visited[next]: continue
        parents[next][0] = node
        roads[next][0] = (leng, leng)
        dfs(next, depth + 1)

def set_parents():
    dfs()
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1]

            min_1, max_1 = roads[j][i - 1]
            min_2, max_2 = roads[parents[j][i - 1]][i - 1]
            new_road = (min(min_1, min_2), max(max_1, max_2))
            roads[j][i] = new_road

def get_roads(a, b):
    if depths[a] > depths[b]: a, b = b, a

    def update_road(road, new_road):
        min_1, max_1 = new_road
        road[0] = min(road[0], min_1)
        road[1] = max(road[1], max_1)

    road = [1e16, 0]

    for i in range(LOG - 1, -1, -1):
        if depths[b] - depths[a] >= (2 ** i):
            update_road(road, roads[b][i])
            b = parents[b][i]

    if a == b: return road
    
    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            update_road(road, roads[a][i])
            a = parents[a][i]

            update_road(road, roads[b][i])
            b = parents[b][i]

    update_road(road, roads[a][0])
    update_road(road, roads[b][0])
    return road

set_parents()

M = int(input())

for i in range(M):
    a, b = sorted(map(int, input().split()))
    min_road, max_road = get_roads(a, b)
    print(min_road, max_road)