from decimal import Decimal, getcontext
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
getcontext().prec = 256

def dijkstra(edges, start, power):
    distances = [ [ float('inf') ] * C for _ in range(R) ]
    distances[0][0] = Decimal("0")

    queue = []
    heappush(queue, (0, start, power))

    while queue:
        curr_dist, (y, x), power = heappop(queue)

        if curr_dist > distances[y][x]:
            continue

        for ny, nx, weight in edges[y][x]:
            new_power = power + weight
            new_dist = curr_dist + speeds[64+power]
            
            if new_dist < distances[ny][nx]:
                distances[ny][nx] = new_dist
                heappush(queue, (new_dist, (ny, nx), new_power))
    
    return distances

V, R, C = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(R) ]
edges = [ [ [] for _ in range(C) ] for _ in range(R) ]

speeds = [ None ] * 128
for i in range(-64, 64):
    speeds[i+64] = (Decimal(2) ** -i) / Decimal(V)

dys, dxs = [0, 0, 1, -1], [1, -1, 0, 0]
for y in range(R):
    for x in range(C):
        for k in range(4):
            dy, dx = dys[k], dxs[k]
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                weight = graph[y][x] - graph[ny][nx]
                edges[y][x].append( (ny, nx, weight) )

result = dijkstra(edges, (0, 0), 0)

answer = result[R-1][C-1]
answer_str = answer

print(answer)