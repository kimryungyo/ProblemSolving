from bisect import insort_right
from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
heap = []
for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        insort_right(heap, -num)
        if len(heap) > n: heap.pop()

print(-heap[n-1])