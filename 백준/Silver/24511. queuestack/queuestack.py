import sys
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Q = deque()

for i in range(N):
    if A[i] == 0:
        Q.append(B[i])
        
M = int(input())
C = list(map(int, input().split()))

res = []
if Q:
    for x in C:
        ans = Q.pop()
        Q.appendleft(x)
        res.append(ans)
else: res = C
    
print(" ".join(map(str, res)))