import sys
sys.setrecursionlimit(1 << 25)

n = int(input())
cross = list(map(int, input().split()))
left = list(map(int, input().split()))
right = list(map(int, input().split()))

left_prefix = [0] * (n)
for i in range(1, n):
    left_prefix[i] = left_prefix[i-1] + left[i-1]

right_suffix = [0] * (n+1)
for i in range(n-1, 0, -1):
    right_suffix[i] = right_suffix[i+1] + right[i-1]

min_distance = float('inf')
min_i = 1
for i in range(1, n+1):
    total = left_prefix[i-1] + cross[i-1] + right_suffix[i]
    if total < min_distance:
        min_distance = total
        min_i = i
        
print(min_i, min_distance)