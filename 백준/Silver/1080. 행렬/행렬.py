from sys import stdin
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
count = 0

original = []
for _ in range(n):
    line = list(map(int, input()))
    original.append(line)

changed = []
for _ in range(n):
    line = list(map(int, input()))
    changed.append(line)

if n < 3 or m < 3:
    if original != changed: print(-1)
    else: print(0)
    quit()

for r in range(n - 2):
    for c in range(m - 2):

        if original[r][c] != changed[r][c]:
            for y in range(r, r + 3):
                for x in range(c, c + 3):
                    value = original[y][x]
                    original[y][x] = 1 if value == 0 else 0

            count += 1

if original != changed:
    print(-1)
    quit()

print(count)