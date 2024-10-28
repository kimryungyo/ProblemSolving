from collections import deque

N = int(input())
queue = deque([N])

for num in range(N - 1, 0, -1):
    queue.appendleft(num)
    for j in range(num):
        queue.appendleft(queue.pop())

print(" ".join(map(str, queue)))