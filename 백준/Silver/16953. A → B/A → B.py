from collections import deque

def bfs(A, B):
    queue = deque([(A, 1)])

    while queue:
        num, cnt = queue.popleft()

        if num == B:
            return cnt

        if num * 2 <= B:
            queue.append((num * 2, cnt + 1))
        if num * 10 + 1 <= B:
            queue.append((num * 10 + 1, cnt + 1))

    return -1

A, B = map(int, input().split())
result = bfs(A, B)
print(result)