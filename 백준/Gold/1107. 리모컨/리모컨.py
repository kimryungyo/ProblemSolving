N = int(input())
M = int(input())
if M == 0: BROKEN = set()
else: BROKEN = set(input().split())

min_count = abs(N - 100)

for num in range(0, 10000000 + 1):
    numbers = set(str(num))
    if numbers.isdisjoint(BROKEN):
        diff = abs(N - num)
        button = len(str(num))

        count = diff + button
        if count < min_count:
            min_count = count

print(min_count)