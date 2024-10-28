from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
v = []
inp = []
ans = 0
pos = 0

for _ in range(n):
    a, b = map(int, input().split())
    v.append((a, True))
    v.append((b, False))
    inp.append((a, b))

v.sort(key=lambda x: (x[0], not x[1]))

curr = 0
for i in range(len(v)):
    if v[i][1]:
        curr += 1
    else:
        curr -= 1
    if curr > ans:
        ans = curr
        pos = v[i][0]

print(ans)
for i in range(len(inp)):
    if inp[i][0] <= pos and inp[i][1] >= pos:
        print(i + 1, end=' ')