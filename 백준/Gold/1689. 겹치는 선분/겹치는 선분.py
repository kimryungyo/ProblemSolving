from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
lines = []
for _ in range(n):
    s, e = map(int, input().split())
    lines.append((s, True))
    lines.append((e, False))

lines.sort()

active = 0
max_active = 0
for line in lines:
    pos, type = line
    if type is True: active += 1
    else:
        if active > max_active:
            max_active = active
        active -= 1

print(max_active)