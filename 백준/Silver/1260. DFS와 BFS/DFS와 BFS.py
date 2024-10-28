from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

def dfs(graph, start, visited):
    visited[start] = True
    result.append(start)
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in sorted(graph[vertex]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return result

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = []
dfs(graph, v, visited)
print(' '.join(map(str, result)))

result = bfs(graph, v)
print(' '.join(map(str, result)))