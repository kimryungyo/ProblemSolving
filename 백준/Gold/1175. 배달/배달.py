from collections import deque

n, m, answer = 0, 0, 0
grid = [['' for _ in range(50)] for _ in range(50)]
visited = [[[[[False for _ in range(2)] for _ in range(2)] for _ in range(5)] for _ in range(50)] for _ in range(50)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start = (0, 0)

idx = 0
n, m = map(int, input().split())
for i in range(n):
    inputed = input()

    for j in range(len(inputed)):
        grid[i][j] = inputed[j]

        if grid[i][j] == 'S':
            start = (i, j)
            grid[i][j] = '.'

        elif grid[i][j] == 'C':
            idx += 1
            if idx == 2: grid[i][j] = 'D'



queue = deque()
queue.append((start[0], start[1], 0, -1, False, False))
visited[start[0]][start[1]][4][0][0] = True

while queue:
    x, y, count, direction, c_visited, d_visited = queue.popleft()

    if c_visited and d_visited:
        print(count)
        quit()

    for i in range(4):
        if i == direction:
            continue

        nx = x + dx[i]
        ny = y + dy[i]
        new_c_visited = c_visited
        new_d_visited = d_visited

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny][i][c_visited][d_visited] and grid[nx][ny] != '#':

                if grid[nx][ny] == 'C':
                    new_c_visited = True

                if grid[nx][ny] == 'D':
                    new_d_visited = True

                visited[nx][ny][i][new_c_visited][new_d_visited] = True
                queue.append((nx, ny, count + 1, i, new_c_visited, new_d_visited))

if answer == 0: print(-1)
else: print(answer)