n = int(input())
points = [ tuple(map(int, input().split())) for _ in range(n) ]
points += [ points[0] ]

slash = backslash = 0

for i in range(n):
    slash += points[i][0] * points[i+1][1]
    backslash += points[i+1][0] * points[i][1]

area = abs(slash - backslash) * 0.5
print(f"{area:.1f}")