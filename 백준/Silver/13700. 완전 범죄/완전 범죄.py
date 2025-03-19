import sys
from collections import deque

input = sys.stdin.readline
N, S, D, F, B, K = map(int, input().split())

police = set()
if K > 0:
    police = set(map(int, input().split()))
    
visited = [False] * (N + 1)
dist = [0] * (N + 1)

queue = deque()
queue.append(S)
visited[S] = True

while queue:
    x = queue.popleft()
    
    if x == D:
        print(dist[x])
        quit()
        
    for nx in (x + F, x - B):
        if 1 <= nx <= N and not visited[nx] and nx not in police:
            visited[nx] = True
            dist[nx] = dist[x] + 1
            queue.append(nx)

print("BUG FOUND")