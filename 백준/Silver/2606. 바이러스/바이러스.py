from collections import deque
n = int(input())
t = int(input())

graph = {}
for _ in range(t):
    a, b = map(int, input().split())
    
    if a not in graph: graph[a] = []
    graph[a].append(b)
    
    if b not in graph: graph[b] = []
    graph[b].append(a)

queue = deque([1])
visited = {1}

count = 0

while queue:
    now = queue.popleft()

    if now in graph:
        for next in graph[now]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
                count += 1

print(count)