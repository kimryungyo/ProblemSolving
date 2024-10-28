from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())

work_time = {}
in_count = { num: 0 for num in range(1, N + 1) }
in_degree = { num: set() for num in range(1, N + 1) }
out_degree = { num: set() for num in range(1, N + 1) }

for num in range(1, N + 1):
    time, count, *priors = map(int, input().split())
    work_time[num] = time
    for prior in priors:
        in_count[num] += 1
        out_degree[prior].add(num)
        in_degree[num].add(prior)

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

need_times = {}
for num in order:
    need_time = work_time[num]

    if in_degree[num]:
        prior_max_time = max(need_times[prior] for prior in in_degree[num])
    else:
        prior_max_time = 0

    need_time += prior_max_time
    need_times[num] = need_time

end_time = max(need_times.values())
print(end_time)