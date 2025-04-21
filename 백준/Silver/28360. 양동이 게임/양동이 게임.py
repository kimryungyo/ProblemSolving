from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
outdeg = [0] * (N+1)

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    outdeg[v] += 1
    
water = [0.0] * (N+1)
water[1] = 100.0

for i in range(1, N+1):
    if outdeg[i] > 0:
        amount = water[i] / outdeg[i]
        for j in graph[i]:
            water[j] += amount
        water[i] = 0.0
        
print(max(water[1:]))
