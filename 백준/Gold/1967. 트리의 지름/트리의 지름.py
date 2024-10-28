from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()

N = int(input())
max_dist = 0
graph = [ [] for _ in range(N + 1) ]

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dfs(node, weight = 0, visited = None):
    if visited is None: visited = [False] * (N + 1)
    visited[node] = True

    max_node, max_dist = None, 0
    for next, wei in graph[node]:
        if visited[next] is False:
            child_node, dist = dfs(next, weight + wei, visited)
            if dist > max_dist:
                max_node = child_node
                max_dist = dist

    if max_node is None: return node, weight
    return max_node, max_dist

step1_node, step1_dist = dfs(1)
step2_node, step2_dist = dfs(step1_node)

print(step2_dist)