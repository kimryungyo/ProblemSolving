from collections import deque
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    dist = [[-1] * (M + 1) for _ in range(N + 1)]
    
    queue = deque([(N, M)])
    dist[N][M] = 0
    
    ans = -1
    while queue:
        a, b = queue.popleft()
        d = dist[a][b]
        if a == 0:
            ans = d
            break
            
        for y in range(1, b + 1):
            mx = min(a, K * y)
            for x in range(1, mx + 1):
                na, nb = a - x, b - y
                if dist[na][nb] == -1:
                    dist[na][nb] = d + 1
                    queue.append((na, nb))
                    
        c = N - a
        dm = M - b
        for w in range(1, dm + 1):
            mz = min(c, K * w)
            for z in range(1, mz + 1):
                na, nb = a + z, b + w
                if dist[na][nb] == -1:
                    dist[na][nb] = d + 1
                    queue.append((na, nb))
                    
    print(ans)