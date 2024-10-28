n = int(input())
nums_a = list(map(int, input().split()))
nums_b = list(map(int, input().split()))
nums_a.sort()
nums_b.sort(reverse=True)

s = 0
for i in range(n):
    s += nums_a[i] * nums_b[i]

print(s)