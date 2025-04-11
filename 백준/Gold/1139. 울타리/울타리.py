from math import sqrt

N = int(input().strip())
fences = list(map(int, input().split()))
fences.sort()

valids = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a, b, c = fences[i], fences[j], fences[k]

            if a + b > c:
                s = (a + b + c) / 2
                area = sqrt(s * (s - a) * (s - b) * (s - c))
                mask = (1 << i) + (1 << j) + (1 << k)
                valids.append((mask, area))

dp = [-1] * (2 ** N)
dp[0] = 0

for mask in range(2 ** N):
    if dp[mask] < 0:
        continue

    for tmask, area in valids:
        if mask & tmask == 0:
            new_mask = mask | tmask
            if dp[new_mask] < dp[mask] + area:
                dp[new_mask] = dp[mask] + area

answer = max(dp)
print(answer)