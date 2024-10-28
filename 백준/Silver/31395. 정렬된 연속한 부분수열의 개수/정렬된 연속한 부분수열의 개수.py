from math import comb
n, *nums = map(int, open(0).read().split())
count = 0

stack = 0
before = 0
for num in nums:
    if num > before:
        stack += 1

    else:
        count += comb(stack, 2)
        count += stack
        stack = 1

    before = num

else:
    count += comb(stack, 2)
    count += stack

print(count)