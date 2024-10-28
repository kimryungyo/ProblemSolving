from collections import deque
dp = {}

for num in range(1, 11):

    count = 0
    queue = deque([ 0 ])

    while queue:
        size = queue.popleft()
        if size > num: continue

        if size == num: count += 1
        else:
            queue.append(size + 1)
            queue.append(size + 2)
            queue.append(size + 3)

    dp[num] = count

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])