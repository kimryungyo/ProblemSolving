n, m, k = map(int, input().split())
max = min(k, m) + min(n - m, n - k)
print(max)