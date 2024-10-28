n, *nums = map(int, open(0).read().split())

result = -1
for answer in range(n + 1):
    count = 0

    for num in nums:
        if num == answer:
            count += 1

    if count == answer:
        if count > result:
            result = count

print(result)