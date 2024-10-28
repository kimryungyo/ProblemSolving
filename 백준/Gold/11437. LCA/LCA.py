def bfs(N, depths, parents, graph, node = 1):
    import collections

    visited = [ False ] * (N + 1)
    queue = collections.deque([ (1, 0) ])

    while queue:
        node, depth = queue.popleft()
        visited[node] = True
        depths[node] = depth
        
        for next in graph[node]:
            if visited[next]: continue
            parents[next][0] = node
            queue.append( (next, depth + 1) )

def set_parents(LOG, N, parents, range):
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1]

def lca(depths, LOG, parents, a, b):
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

def main():
        
    import math
    import sys
    input = sys.stdin.readline
    m, i, r, p, l = map, int, range, print, lca

    N = int(input())

    LOG = int(math.log2(N)) + 1
    depths = [ 0 ] * (N + 1)
    parents = [ [0] * LOG for _ in r(N + 1) ]

    graph = [ [] for _ in r(N + 1) ]
    for _ in r(N - 1):
        a, b = m(i, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bfs(N, depths, parents, graph)
    set_parents(LOG, N, parents, r)

    M = i(input())

    for _ in r(M):
        a, b = m(i, input().split())
        p(l(depths, LOG, parents, a, b))

main()