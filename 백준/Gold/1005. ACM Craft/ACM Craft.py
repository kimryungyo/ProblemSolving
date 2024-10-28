from graphlib import TopologicalSorter
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    buildings = list(map(int, input().split()))

    sorting = TopologicalSorter()
    conditions = { vertex: [] for vertex in range(N) }
    for _ in range(K):
        x, y = map(int, input().split())
        sorting.add(y - 1, x - 1)
        conditions[y - 1].append(x - 1)

    W = int(input()) - 1

    order = list(sorting.static_order())
    if W not in order: print(buildings[W]); continue
    needs = order[:order.index(W) + 1]

    need_times = {}
    for need in needs:
        need_time = buildings[need]

        prior_max_time = 0
        for prior in conditions[need]:
            prior_time = need_times[prior]
            if prior_time > prior_max_time:
                prior_max_time = prior_time

        need_time += prior_max_time
        need_times[need] = need_time

    print(need_times[W])