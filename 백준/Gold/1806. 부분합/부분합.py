n, s = map(int, input().split())
nums = list(map(int, input().split()))

p1 = p2 = 0
length = 1
min_length = None

total = nums[0]

while p1 < n:

    if total >= s:

        if not min_length: min_length = length
        if length < min_length: min_length = length

        p1 += 1
        length -= 1
        total -= nums[p1 - 1]

    elif p2 < n - 1:

        p2 += 1
        length += 1
        total += nums[p2]

    else: 

        p1 += 1
        length -= 1
        total -= nums[p1 - 1]

if min_length is None: min_length = 0
print(min_length)