N, M, *nums = map(int, open(0).read().split())

sums = [ 0 ]
sum = 0
for num in nums:
    sum += num
    sums.append(sum)
sums_set = set(sums)

count = 0
for i in range(1, N + 1):
    remain = sums[i] - M
    if remain in sums_set:
        count += 1

print(count)