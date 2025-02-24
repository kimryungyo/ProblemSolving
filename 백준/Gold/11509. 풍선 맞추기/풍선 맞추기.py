from collections import defaultdict

n = int(input())
balloon_heights = list(map(int, input().split()))

arrow_counts = defaultdict(int)
arrow_total = 0

for height in balloon_heights:
    if arrow_counts[height + 1] > 0:
        arrow_counts[height + 1] -= 1
        arrow_counts[height] += 1
    else:
        arrow_total += 1
        arrow_counts[height] += 1

print(arrow_total)