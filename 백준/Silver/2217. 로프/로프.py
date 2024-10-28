n, *ropes = map(int, open(0).read().split())
ropes.sort(reverse=True)

max_weight = 0
count = 0
for rope in ropes:
    count += 1
    weight = rope * count
    if weight > max_weight:
        max_weight = weight

print(max_weight)