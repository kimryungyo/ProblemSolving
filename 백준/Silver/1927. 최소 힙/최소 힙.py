from heapq import heappush, heappop
from sys import stdin
input = lambda: stdin.readline().rstrip()

n, *nums = map(int, open(0).read().split())
heap = []

for num in nums:
    if num == 0:
        if not heap: print(0)
        else: print(heappop(heap))
        
    else: heappush(heap, num)