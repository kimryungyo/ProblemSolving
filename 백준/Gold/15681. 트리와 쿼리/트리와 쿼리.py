import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

dp = [1] * 100001
visited = [False] * 100001
graph = defaultdict(list)
isleaf = False
nodes, root, queries = 0, 0, 0

def dfs(node, parent):
    visited[node] = True
    for next_node in graph[node]:
        if visited[next_node]: continue
        dfs(next_node, node)
    if parent != -1: dp[parent] += dp[node]

data = open(0).read().split()
nodes = int(data[0])
root = int(data[1])
queries = int(data[2])
idx = 3

for _ in range(nodes-1):
    a = int(data[idx])
    idx += 1
    b = int(data[idx])
    idx += 1
    graph[a].append(b)
    graph[b].append(a)

dfs(root, -1)

results = []
for _ in range(queries):
    q = int(data[idx])
    idx += 1
    print(dp[q])