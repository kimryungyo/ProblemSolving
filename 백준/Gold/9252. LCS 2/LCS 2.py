from sys import stdin as s
input=lambda:s.readline().rstrip()

str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j - 1] + 1 if str1[i - 1] == str2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

length = dp[n][m]

i, j = n, m
lcs = []

while i > 0 and j > 0:
    if str1[i - 1] == str2[j - 1]:
        lcs.append(str1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]: i -= 1
    else: j -= 1

lcs.reverse()
lcs = ''.join(lcs)

print(length)
if length > 0: print(lcs)