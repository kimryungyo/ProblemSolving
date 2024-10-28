from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()

N = int(input())

graph = [ [] for _ in range(N + 1) ]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [ 0 ] * (N + 1)

def dfs(node, parent):
    for next in graph[node]:
        if next == parent: continue
        parents[next] = node
        dfs(next, node)

dfs(1, 0)

for i in range(2, N + 1):
    print(parents[i])