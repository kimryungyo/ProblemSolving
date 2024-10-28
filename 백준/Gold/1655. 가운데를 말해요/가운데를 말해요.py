from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

left, right = [], []

N = int(input())
for _ in range(N):
    num = int(input())

    if len(left) <= len(right): 
        heappush(left, -num)
    else: 
        heappush(right, num)

    if left and right:
        if -left[0] > right[0]:
            mini = -heappop(left)
            maxi = heappop(right)

            heappush(left, -maxi)
            heappush(right, mini)

    print(-left[0])