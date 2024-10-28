from collections import deque

N = int(input())
queue = deque([(N, 0)])
visited = {}

while queue:
    num, count = queue.popleft()

    if num == 1: print(count); break

    if num % 3 == 0:
        next = num // 3
        if visited.get(next, float("inf")) > count + 1:
            queue.append((next, count + 1))
            visited[next] = count + 1

    if num % 2 == 0:
        next = num // 2
        if visited.get(next, float("inf")) > count + 1:
            queue.append((next, count + 1))
            visited[next] = count + 1

    next = num - 1
    if visited.get(next, float("inf")) > count + 1:
        queue.append((next, count + 1))
        visited[next] = count + 1