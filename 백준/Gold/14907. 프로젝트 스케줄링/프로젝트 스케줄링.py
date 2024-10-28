from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

work_time = {}
in_count = {}
in_degree = {}
out_degree = {}

while True:
    try:
        splited = input().split()
        if len(splited) == 2: code, time, priors = *splited, []
        else: code, time, priors = splited

        work_time[code] = int(time)

        if code not in out_degree: out_degree[code] = set()
        if code not in in_degree: in_degree[code] = set()
        if code not in in_count: in_count[code] = 0

        for prior in priors:
            if prior not in out_degree: out_degree[prior] = set()
            out_degree[prior].add(code)
            in_degree[code].add(prior)
            in_count[code] += 1

    except: break

queue = deque()
for code in work_time.keys():
    if in_count[code] == 0:
        queue.append(code)

order = []
while queue:
    vertex = queue.popleft()
    order.append(vertex)
    
    for next in out_degree[vertex]:
        in_count[next] -= 1
        if in_count[next] == 0:
            queue.append(next)

need_times = {}
for code in order:
    need_time = work_time[code]

    if in_degree[code]:
        prior_max_time = max(need_times[prior] for prior in in_degree[code])
        need_time += prior_max_time

    need_times[code] = need_time

end_time = max(need_times.values())
print(end_time)