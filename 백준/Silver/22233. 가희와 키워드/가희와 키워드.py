from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
words = { input() for _ in range(N) }

for _ in range(M):
    for used in input().split(","):
        if used in words:
            words.remove(used)
    print(len(words))