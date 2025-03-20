from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
V = list(map(int, input().split()))

S = sum(V)
T = (S + 1) // 2

V.sort(reverse=True)
s = 0
k = 0
for x in V:
    s += x
    k += 1
    if s >= T:
        break
        
print(M // (k + 1))