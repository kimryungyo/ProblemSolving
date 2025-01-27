from sys import stdin
input = stdin.readline

N, Q, U, V = map(int, input().split())
K = list(map(int, input().split()))

K = [0] + K  

S = [0] * (N+1)
X = [0] * (N+1)

def reprefix(start_index):
    for i in range(start_index, N+1):
        S[i] = S[i-1] + K[i]
        X[i] = U * S[i] + V * i

for i in range(1, N+1):
    S[i] = S[i-1] + K[i]
    X[i] = U * S[i] + V * i

for _ in range(Q):
    c, a, b = map(int, input().split())
    if c == 0:
        min_val = X[a-1]
        ans = -10 ** 15
        for j in range(a, b+1):
            
            candidate = X[j] - V - min_val
            if candidate > ans:
                ans = candidate
            if X[j] < min_val:
                min_val = X[j]
        print(ans)

    else:
        K[a] = b
        reprefix(a)