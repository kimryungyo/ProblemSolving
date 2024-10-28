from sys import stdin
input = lambda: stdin.readline().rstrip()

from collections import Counter

n = int(input())
count = 0
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A_C = Counter(A)
B_C = Counter(B)
C_C = Counter(C)
D_C = Counter(D)
A = set(A)
B = set(B)
C = set(C)
D = set(D)

ab_sum = {}
for a in A:
    for b in B:
        sum_ = a + b
        if sum_ not in ab_sum: ab_sum[sum_] = 0
        ab_sum[sum_] += A_C[a] * B_C[b]

for c in C:
    for d in D:
        sum_ = c + d
        if -sum_ in ab_sum: 
            count += ab_sum[-sum_] * C_C[c] * D_C[d]

print(count)