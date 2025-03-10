from sys import stdin
input = stdin.readline

_ = input()
N = int(input())
data = []

for _ in range(N):
    m = int(input())
    s = list(map(int, input().split()))
    b = int(input())
    data.append((s, b))

ans = []

for cand in range(1, N + 1):
    ok = True
    for idx, (s, b) in enumerate(data, 1):
        if idx == cand:
            if b == 1 and cand in s: ok = False
            if b == 0 and cand not in s: ok = False
        else:
            if b == 1 and cand not in s: ok = False
            if b == 0 and cand in s: ok = False
        if not ok: break
    if ok: ans.append(cand)

print(" ".join(map(str, ans)) if ans else "swi")