import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
s = list(map(int, input().split()))
heapq.heapify(s)

for _ in range(m):
    d = heapq.heappop(s) + heapq.heappop(s)
    heapq.heappush(s, d)
    heapq.heappush(s, d)

print(sum(s))