from itertools import combinations
from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M, K = map(int, input().split())
execution = list(map(int, input().split()))

in_count = { num: 0 for num in range(1, N + 1) }
in_degree = { num: set() for num in range(1, N + 1) }
out_degree = { num: set() for num in range(1, N + 1) }

for _ in range(M):
    a, b = map(int, input().split())
    in_count[b] += 1
    in_degree[b].add(a)
    out_degree[a].add(b)

queue = deque()
for num in range(1, N + 1):
    if in_count[num] == 0:
        queue.append(num)

order = []
while queue:
    vertex = queue.popleft()
    order.append(vertex)
    
    for next in out_degree[vertex]:
        in_count[next] -= 1
        if in_count[next] == 0:
            queue.append(next)

first, last = order[0], order[-1]
min_time = float("inf")

for immediately in combinations(order[1:-1], K):
    immediately = set(immediately)

    need_times = {}
    for num in order:
        need_time = execution[num - 1]
        if num in immediately: need_time = 0

        if in_degree[num]:
            prior_max_time = max(need_times[prior] for prior in in_degree[num])
        else:
            prior_max_time = 0

        need_time += prior_max_time
        need_times[num] = need_time

    end_time = max(need_times.values())
    if end_time < min_time:
        min_time = end_time

print(min_time)