n = int(input())
q = sorted(map(int, input().split()))
for a in range(n, -1, -1):
    if a <= q[-a]: print(a); break