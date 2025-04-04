from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

def dijkstra(speed, start):
    distances = [ [ float('inf') ] * C for _ in range(R) ]
    distances[0][0] = 0

    queue = []
    heappush(queue, (0, start, speed))

    dys, dxs = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        curr_dist, (y, x), speed = heappop(queue)

        if curr_dist > distances[y][x]:
            continue

        for k in range(4):
            dy, dx = dys[k], dxs[k]
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                weight = graph[y][x] - graph[ny][nx]

                new_speed = speed * (2 ** weight)
                new_dist = curr_dist + (1 / speed)
                
                if new_dist < distances[ny][nx]:
                    distances[ny][nx] = new_dist
                    heappush(queue, (new_dist, (ny, nx), new_speed))
    
    return distances

V, R, C = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(R) ]

result = dijkstra(V, (0, 0))
answer = result[R-1][C-1]
print(f"{answer:.32f}")