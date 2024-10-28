from heapq import heappush, heappop
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

in_degree = { num: 0 for num in range(1, N + 1) }
out_degree = { num: set() for num in range(1, N + 1) }

for _ in range(M):
    a, b = map(int, input().split())
    in_degree[b] += 1
    out_degree[a].add(b)

queue = []
for num in range(1, N + 1):
    if in_degree[num] == 0:
        heappush(queue, num)

order = []
while queue:
    vertex = heappop(queue)
    order.append(vertex)
    for next in out_degree[vertex]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            heappush(queue, next)

print(" ".join(map(str, order)))