from sys import stdin
input = stdin.readline

N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]

tasks.sort(key=lambda x: x[1], reverse=True)

current = 10 ** 9
for T, S in tasks:
    current = min(current, S) - T

print(-1 if current < 0 else current)