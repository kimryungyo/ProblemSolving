from collections import deque

n, m = map(int, input().split())
if n == m == 1: print("Yes"); quit()

maps = []
for _ in range(m):
    line = list(map(int, input().split()))
    maps.append(line)

queue = deque([(0, 0)])
visited = set([(0, 0)])

while queue:
    y, x = queue.popleft()
    nexts = [(y + 1, x), (y, x + 1)]
    for next in nexts:
        if next in visited: continue
        next_y, next_x = next

        if (next_y == m - 1) and (next_x == n - 1):
            print("Yes")
            quit()

        if (next_y < m) and (next_x < n):
            if maps[next_y][next_x] == 1:
                visited.add(next)
                queue.append(next)

print("No")