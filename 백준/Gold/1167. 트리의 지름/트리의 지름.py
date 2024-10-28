from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)
input = lambda: stdin.readline().rstrip()

N = int(input())
max_dist = 0
graph = [ [] for _ in range(N + 1) ]

for _ in range(N):
    node, *edges, _ = map(int, input().split())
    for i in range(len(edges) // 2):
        other, weight = edges[i * 2], edges[i * 2 + 1]
        graph[node].append((other, weight))

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