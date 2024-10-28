N = int(input())
X, Y = map(int, input().split())

def process(N, X, Y):
    if N == 1: return 0
    if (X, Y) in [ (1, 1), (N, 1), (1, N), (N, N) ]:
        return 2
    if X == 1 or X == N: return 3
    if Y == 1 or Y == N: return 3
    return 4

print(process(N, X, Y))