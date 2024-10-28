from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
heard = { input() for _ in range(N) }
seen = { input() for _ in range(M) }
all = heard & seen
print(len(all))
print("\n".join(sorted(all)))