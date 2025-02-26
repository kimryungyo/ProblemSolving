import sys, heapq
input = sys.stdin.readline

T, n = map(int, input().split())

heap = []
for _ in range(n):
    pid, runtime, priority = map(int, input().split())
    heapq.heappush(heap, (-priority, pid, runtime, priority))
    
for _ in range(T):
    neg_val, pid, remain, cur_val = heapq.heappop(heap)
    print(pid)
    remain -= 1
    new_val = cur_val - 1
    if remain > 0:
        heapq.heappush(heap, (-new_val, pid, remain, new_val))