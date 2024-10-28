from math import log2
from sys import stdin, setrecursionlimit
input = lambda: stdin.readline().rstrip()
setrecursionlimit(10 ** 6)

N = int(input())

LOG = int(log2(N)) + 1
depths = [ 0 ] * (N + 1)
visited = [ False ] * (N + 1)
parents = [ [0] * LOG for _ in range(N + 1) ]
distances = [ 0 ] * (N + 1)

graph = [ [] for _ in range(N + 1) ]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node = 1, depth = 0, distance = 0):
    visited[node] = True
    depths[node] = depth
    distances[node] = distance

    for next, leng in graph[node]:
        if visited[next]: continue
        parents[next][0] = node
        dfs(next, depth + 1, distance + leng)

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
    q, *query = map(int, input().split())

    if q == 1:
        a, b = query
        ancestor = lca(a, b)
        a_dist = abs(distances[ancestor] - distances[a])
        b_dist = abs(distances[ancestor] - distances[b])
        print(a_dist + b_dist)

    else:
        a, b, c = query
        ancestor = lca(a, b)
        dist_a = depths[a] - depths[ancestor]
        dist_b = depths[b] - depths[ancestor]
        dist = dist_a + dist_b + 1

        if c <= dist_a:
            if c - 1 == 0: print(a)
            else:

                moved = 0
                for i in range(LOG - 1, -1, -1):
                    if (moved + 2 ** i) <= c - 1:
                        a = parents[a][i]
                        moved += 2 ** i
                    if moved == c - 1: break
                
                print(a)

        else:
            if dist - c == 0: print(b)
            else:

                moved = 0
                for i in range(LOG - 1, -1, -1):
                    if (moved + 2 ** i) <= dist - c:
                        b = parents[b][i]
                        moved += 2 ** i
                    if moved == dist - c: break
                
                print(b)