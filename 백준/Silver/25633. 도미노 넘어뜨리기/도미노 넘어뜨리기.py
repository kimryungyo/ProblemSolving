n = int(input().strip())
a = list(map(int, input().split()))

dp = [1] * n
s = a[:]

for i in range(n):
    for j in range(i + 1, n):
        if s[i] >= a[j]:
            if dp[i] + 1 > dp[j]:
                dp[j] = dp[i] + 1
                s[j] = s[i] + a[j]
            elif dp[i] + 1 == dp[j]:
                s[j] = max(s[j], s[i] + a[j])

print(max(dp))