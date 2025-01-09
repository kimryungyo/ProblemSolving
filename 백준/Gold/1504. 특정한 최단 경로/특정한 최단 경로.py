import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, graph, N):
    INF = float('inf')
    
    distances = [INF] * (N + 1)
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distances[u]:
            continue

        for neighbor, weight in graph[u]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1, graph, N)
dist_v1 = dijkstra(v1, graph, N)
dist_v2 = dijkstra(v2, graph, N)

INF = float('inf')

option1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
option2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

min_distance = min(option1, option2)

if min_distance >= INF:
    print(-1)
else:
    print(int(min_distance))