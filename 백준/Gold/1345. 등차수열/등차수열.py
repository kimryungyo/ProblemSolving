N, A = map(int, input().split())
if N == 0: print(0); quit()

nums = list(map(int, input().split()))

min_dist = None
max_dist = None
for idx, num in enumerate(nums):
    dist = num - A
    lower_dist = dist / (idx + 1)
    upper_dist = (dist + 1) / (idx + 1)

    if min_dist is None: min_dist = lower_dist
    if max_dist is None: max_dist = upper_dist
    if lower_dist > min_dist: min_dist = lower_dist
    if upper_dist < max_dist: max_dist = upper_dist

if min_dist >= max_dist: print(-1)
elif min_dist < 0: print(-1)
else: print(min_dist)