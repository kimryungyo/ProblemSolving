from sys import stdin
input = lambda: stdin.readline().rstrip()

counts = list(map(int, input().split()))

box_count = min(counts)
counts = list(map(lambda x: x - box_count, counts))

for i in range(len(counts)):
    count = counts[i]
    use = count // 3
    box_count += use
    count -= use * 3

    if count == 2:
        box_count += 1
        count = 0

    counts[i] = count


remains = [ count for count in counts if count ]
if remains: box_count += 1

print(box_count)