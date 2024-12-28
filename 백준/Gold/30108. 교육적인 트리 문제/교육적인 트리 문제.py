from collections import deque
from sys import setrecursionlimit

def main():

    setrecursionlimit(1 << 25)
    N = int(input())
    p = list(map(int, input().split()))
    A = list(map(int, input().split()))

    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        adj[p[i - 2]].append(i)

    depth = [0] * (N + 1)
    queue = deque()
    queue.append(1)
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            depth[v] = depth[u] + 1
            queue.append(v)

    nodes = [(-A[i - 1], depth[i], i) for i in range(1, N + 1)]
    nodes.sort()

    prefix_sums = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sums[i] = prefix_sums[i - 1] + (-nodes[i - 1][0])

    for k in range(1, N + 1):
        print(prefix_sums[k])

main()