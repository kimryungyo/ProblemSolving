def dijkstra(start, graph, n):
    from heapq import heappop, heappush
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, u = heappop(heap)
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heappush(heap, (new_dist, v))
    return dist

def main():
    from sys import stdin
    input = stdin.readline
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        reverse_graph[b].append((a, t))

    dist_from_x = dijkstra(x, graph, n)
    dist_to_x = dijkstra(x, reverse_graph, n)

    max_time = 0
    for i in range(1, n + 1):
        max_time = max(max_time, dist_to_x[i] + dist_from_x[i])

    return max_time

print(main())