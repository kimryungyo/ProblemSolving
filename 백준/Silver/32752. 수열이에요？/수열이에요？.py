import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

L -= 1
R -= 1

ok = True

for i in range(L - 1):
    if A[i] > A[i + 1]:
        ok = False
        break

if ok:
    for i in range(R + 1, N - 1):
        if A[i] > A[i + 1]:
            ok = False
            break

if ok:
    sub_min = min(A[L:R + 1])
    sub_max = max(A[L:R + 1])

    if L > 0 and A[L - 1] > sub_min:
        ok = False
    if R < N - 1 and sub_max > A[R + 1]:
        ok = False

print(1 if ok else 0)