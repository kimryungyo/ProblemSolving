from heapq import heappop, heappush
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, L = map(int, input().split())
nums = list(map(int, input().split()))

heap = []
added = set()
removes = {}
for i in range(1, N + 1):
    s = max(1, i - L + 1)
    e = i

    if s > 1:
        r = s - 1
        if nums[r-1] not in removes: removes[nums[r-1]] = 0
        removes[nums[r-1]] += 1

    if s not in added: heappush(heap, nums[s-1])
    added.add(s)
    if e not in added: heappush(heap, nums[e-1])
    added.add(e)

    while removes.get(heap[0], 0) > 0:
        removes[heap[0]] -= 1
        heappop(heap)

    print(heap[0], end = " ")