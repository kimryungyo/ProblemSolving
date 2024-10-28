from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

in_degree = { num: set() for num in range(1, N + 1) }
out_degree = { num: set() for num in range(1, N + 1) }

for _ in range(M):
    n, *order = map(int, input().split())
    for i in range(len(order) - 1):
        prior, num = order[i], order[i+1]
        out_degree[prior].add(num)
        in_degree[num].add(prior)

queue = deque()
for num in range(1, N + 1):
    if len(in_degree[num]) == 0:
        queue.append(num)

order = []
while queue:
    vertex = queue.popleft()
    order.append(vertex)
    
    for next in out_degree[vertex]:
        in_degree[next].remove(vertex)
        if len(in_degree[next]) == 0:
            queue.append(next)

if len(order) != N: print(0); quit()
print("\n".join(map(str, order)))