from math import log2
from sys import stdin, setrecursionlimit
input = lambda: stdin.readline().rstrip()
setrecursionlimit(10 ** 6)

N = int(input())

LOG = int(log2(N)) + 1
depths = [ 0 ] * (N + 1)
visited = [ False ] * (N + 1)
parents = [ [0] * LOG for _ in range(N + 1) ]

graph = [ [] for _ in range(N + 1) ]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node = 1, depth = 0):
    visited[node] = True
    depths[node] = depth

    for next in graph[node]:
        if visited[next]: continue
        parents[next][0] = node
        dfs(next, depth + 1)

def set_parents():
    dfs()
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1]

def lca(a, b):
    if depths[a] > depths[b]: a, b = b, a
    for i in range(LOG - 1, -1, -1):
        if depths[b] - depths[a] >= (2 ** i):
            b = parents[b][i]

    if a == b: return a
    
    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
    return parents[a][0]

set_parents()

M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))