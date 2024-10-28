from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
visited[N] = 0
queue = deque([N])

while queue:
    x = queue.popleft()
    
    if x == K:
        print(visited[x])
        quit()

    nx = x * 2
    if 0 <= nx < 100001 and visited[nx] is False:
        visited[nx] = visited[x]
        queue.append(nx)
        
    for nx in (x - 1, x + 1):
        if 0 <= nx < 100001 and visited[nx] is False:
            visited[nx] = visited[x] + 1
            queue.append(nx)
